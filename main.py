import os
import sys
import logging
import i18n

from dotenv import load_dotenv
from configparser import ConfigParser
from classes.element import Position
from classes.element.Temperature import Temperature
from classes.element.Weather import Weather

from views.MainFrame import MainFrame
from views.lists.MyItem import MyItem

from workers.CitiesWorker import CitiesWorker
from workers.WeatherWorker import WeatherWorker

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QThread

# Globals used by all threads
hasToReadWeather = True
confFileName = "conf/settings.ini"
envFileName = "conf/.env"
logger = logging.getLogger("WeatherApp")

def cleanUp():
    """
        Cleaning function at application death
    """
    weatherWorker.setHasToReadWeather(False)
    with open(confFileName, encoding="utf8", mode="w") as file:
        configur.write(file)

def loadLogger():
    """
        Loading loggers data
    """
    # Logs Formatting
    formatter = logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")

    # Handler for messages (critical and errors in one file, info in another and eventually debug in the stdout)
    handler_critic = logging.FileHandler(configur.get('logging', 'critical'), mode="a", encoding="utf-8")
    handler_info = logging.FileHandler(configur.get('logging', 'standard'), mode="a", encoding="utf-8")
    handler_debug = logging.StreamHandler(sys.stdout)

    # Setting the format for every handler
    handler_critic.setFormatter(formatter)
    handler_info.setFormatter(formatter)
    handler_debug.setFormatter(formatter)

    # Configuring the levels
    handler_debug.setLevel(logging.DEBUG)
    handler_info.setLevel(logging.INFO)
    handler_critic.setLevel(logging.CRITICAL)

    # Set the current level in conformity with the settings and add all handlers
    logger.setLevel(configur.getint('logging', 'level'))
    logger.addHandler(handler_critic)
    logger.addHandler(handler_info)
    logger.addHandler(handler_debug) # HACK : TO BE COMMENTED IN FINAL VERSION

def progressWeatherWorker(weather : Weather) -> None:
    """
        Function to be executed when the progress signal of weather worker is sent

        :param weather: The new weather
        :type weather: Weather
    """
    if weather == None:
        logger.error("No weather provided")
    else:
        # Default to Kelvin
        current = weather.getTemperature().getCurrent()
        feelsLike = weather.getTemperature().getFeelsLike()
        minT = weather.getTemperature().getMin()
        maxT = weather.getTemperature().getMax()
        unit = i18n.t('translate.temperature.kelvin')

        # If configuration ask for celsius or fahrenheit
        if(configur.get('weather', 'tempUnit') == "c"):
            current = Temperature.fromKelvinToCelsius(current)
            feelsLike = Temperature.fromKelvinToCelsius(feelsLike)
            minT = Temperature.fromKelvinToCelsius(minT)
            maxT = Temperature.fromKelvinToCelsius(maxT)
            unit = i18n.t('translate.temperature.celsius')
        elif(configur.get('weather', 'tempUnit') == "f"):
            current = Temperature.fromKelvinToFahrenheit(current)
            feelsLike = Temperature.fromKelvinToFahrenheit(feelsLike)
            minT = Temperature.fromKelvinToFahrenheit(minT)
            maxT = Temperature.fromKelvinToFahrenheit(maxT)
            unit = i18n.t('translate.temperature.fahrenheit')
        
        # Set the temperatures text
        ex.getTemp().setCurrentTempText(current, unit)
        ex.getTemp().setFeelsLikeTempText(feelsLike, unit)
        ex.getTemp().setMinTempText(minT, unit)
        ex.getTemp().setMaxTempText(maxT, unit)

        # Set the sunrise/sunset values
        ex.getSunHours().setSunriseValue(weather.getMisc().getSunrise(), configur.get('time','timezone'))
        ex.getSunHours().setSunsetValue(weather.getMisc().getSunset(), configur.get('time','timezone'))

        # Set the atmospheric data
        ex.getAtm().setWindSpeedValue(weather.getWind().getSpeed())
        ex.getAtm().setWindDirectionValue(weather.getWind().getDirection())
        ex.getAtm().setPressureValue(weather.getMisc().getPressure())
        ex.getAtm().setHumidityValue(weather.getMisc().getHumidity())

        # Print the weather to debug for information
        logger.debug(weather)

def finishedWeatherWorker() -> None:
    """
        Function to be executed when the finished signal of the weather worker is sent
    """
    logger.info("Weather worker has finished")

def progressCitiesWorker(item : MyItem) -> None:
    """
        Function to be executed when the progress signal of city worker is sent

        :param item: Received item
        :type item: MyItem
    """
    if(item != None):
        #ex.getCitiesList().addItem(item)
        lat = item.getPosition().getLatitude()
        lon = item.getPosition().getLongitude()
        name = item.getPosition().getName()
        ex.getMap().addACityOnMap(
            lat=lat, 
            lon=lon, 
            name=name)
        if(item.isChoosen()):
            #ex.getCitiesList().setCurrentItem(item)
            newCityChoosen(item.getPosition())
    else:
        logger.error("Cities can't load properly")

def finishedCitiesWorker() -> None:
    """
        The function to executed when the finished signal of the cities worker is called
    """
    ex.getMap().printTheMap()
    ex.update()
    logger.debug("Cities loading finished")

def newCityChoosen(position : Position.Position) -> None:
    """
        This function set a new position in the weather worker and the config file to be saved
    """
    logger.debug("New city choosen : "+str(position))
    configur.set('cities', 'choosen', value=str(position.getId()))
    weatherWorker.setCurrentPosition(position)

def i18nLoading(translationPath : str, locale : str) -> None:
    """
        This function loads the translation file

        :param translationPath: The folder path
        :type translationPath: str
        :param locale: The locale to load
        :type locale: str
    """    
    i18n.load_path.append(translationPath)
    i18n.set('locale', locale)
    i18n.set('fallback', 'en')

if __name__=="__main__":

    # TODO Add options command lines with getopt. For example settings file path or .env file path

    # Opening informations in .env and .ini files
    load_dotenv(envFileName)
    configur = ConfigParser()
    configur.read(confFileName)

    # Logger loading
    loadLogger()

    # Loading the translations
    i18nLoading(configur.get('language', 'folder'), configur.get('language', 'locale'))

    # Application starting and cleanup adding
    app=QApplication(sys.argv)
    app.aboutToQuit.connect(cleanUp)

    # Main window creation and signals adding
    # x=0,y=0,width=app.primaryScreen().size().width(),height=app.primaryScreen().size().height()
    ex=MainFrame()
    ex.clickedSig.connect(newCityChoosen) # Add a signal on a list item click

    # Starting the weather reading thread
    t1 = QThread()
    weatherWorker = WeatherWorker()
    weatherWorker.setHasToReadWeather(True)
    weatherWorker.setApiKey(os.getenv("API_KEY"))
    weatherWorker.setDelayTime(configur.getint('weather', 'delay'))
    weatherWorker.moveToThread(t1)

    t1.started.connect(weatherWorker.run) # Connect the main loop of the thread
    weatherWorker.progress.connect(progressWeatherWorker) # Connecting the function to the new weather signal
    weatherWorker.finished.connect(t1.quit) # Connecting the end of the thread
    weatherWorker.finished.connect(t1.deleteLater) # Connecting thread cleaning
    weatherWorker.finished.connect(weatherWorker.deleteLater) # Connecting worker cleaning
    weatherWorker.finished.connect(finishedWeatherWorker) # Connecting main thread function on thread ending
    t1.start() # Starting the thread

    # City reading thread (for reading through the quite long resources file)
    t2 = QThread()
    citiesWorker = CitiesWorker()
    citiesWorker.setCitiesFileName(configur.get('cities', 'filename'))
    citiesWorker.setChoosenCity(configur.getint('cities', 'choosen'))
    citiesWorker.moveToThread(t2)

    t2.started.connect(citiesWorker.run) # Connecting the main loop of the thread
    citiesWorker.progress.connect(progressCitiesWorker) # Conencting to the event of a new city
    citiesWorker.finished.connect(t2.quit) # Connecting to the end of the thread
    citiesWorker.finished.connect(t2.deleteLater) # Connecting to delete the thread
    citiesWorker.finished.connect(citiesWorker.deleteLater) # Connecting to clean up the worker
    citiesWorker.finished.connect(finishedCitiesWorker) # Connecting the main thread function on thread ending
    t2.start() # Starting the thread

    sys.exit(app.exec()) # Starting the application