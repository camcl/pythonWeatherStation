import os
import sys
import i18n
import getopt

from dotenv import load_dotenv
from classes.element.Miscellaneous import Miscellaneaous
from modules.logger.logger import Logger
from modules.settings.settings import Settings

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

# Default values for options
confFileName = "./conf/settings.ini"
envFileName = "./conf/.env"
logInfo = "./logs/info.log"
logCritical = "./logs/critical.log"
logLevel = 20

def cleanUp():
    """
        Cleaning function at application death
    """
    weatherWorker.setHasToReadWeather(False)
    Settings.getInstance().write()

def progressWeatherWorker(weather : Weather) -> None:
    """
        Function to be executed when the progress signal of weather worker is sent

        :param weather: The new weather
        :type weather: Weather
    """
    if weather == None:
        Logger.getInstance().error("No weather provided")
    else:
        # Print the weather to debug for information
        Logger.getInstance().debug(weather)

        # Default to Kelvin
        current = weather.getTemperature().getCurrent()
        feelsLike = weather.getTemperature().getFeelsLike()
        minT = weather.getTemperature().getMin()
        maxT = weather.getTemperature().getMax()
        unit = i18n.t('translate.temperature.kelvin')

        # If configuration ask for celsius or fahrenheit
        if(Settings.getInstance().get('weather', 'tempUnit', 'c') == "c"):
            current = Temperature.fromKelvinToCelsius(current)
            feelsLike = Temperature.fromKelvinToCelsius(feelsLike)
            minT = Temperature.fromKelvinToCelsius(minT)
            maxT = Temperature.fromKelvinToCelsius(maxT)
            unit = i18n.t('translate.temperature.celsius')
        elif(Settings.getInstance().get('weather', 'tempUnit', 'c') == "f"):
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
        ex.getSunHours().setSunriseValue(weather.getMisc().getSunrise(), Settings.getInstance().get('time','timezone', 'Etc/UTC'))
        ex.getSunHours().setSunsetValue(weather.getMisc().getSunset(), Settings.getInstance().get('time','timezone', 'Etc/UTC'))

        # Set the atmospheric data
        ex.getAtm().setWindSpeedValue(weather.getWind().getSpeed())
        ex.getAtm().setWindDirectionValue(i18n.t("translate.wind."+Miscellaneaous.convertDirectionDegreesInDirectionString(weather.getWind().getDirection())))
        ex.getAtm().setPressureValue(weather.getMisc().getPressure())
        ex.getAtm().setHumidityValue(weather.getMisc().getHumidity())
        
def finishedWeatherWorker() -> None:
    """
        Function to be executed when the finished signal of the weather worker is sent
    """
    Logger.getInstance().info("Weather worker has finished")

def progressCitiesWorker(item : MyItem) -> None:
    """
        Function to be executed when the progress signal of city worker is sent

        :param item: Received item
        :type item: MyItem
    """
    if(item != None):
        ex.getCitiesList().addItem(item)
        if(item.isChoosen()):
            ex.getCitiesList().setCurrentItem(item)
            newCityChoosen(item.getPosition())
    else:
        Logger.getInstance().error("Cities can't load properly")

def finishedCitiesWorker() -> None:
    """
        The function to executed when the finished signal of the cities worker is called
    """
    ex.update()
    Logger.getInstance().debug("Cities loading finished")

def newCityChoosen(position : Position.Position) -> None:
    """
        This function set a new position in the weather worker and the config file to be saved
    """
    Logger.getInstance().debug("New city choosen : "+str(position))
    Settings.getInstance().set('cities', 'choosen', value=str(position.getId()))
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

def startApp() -> None:

    # Default values for options
    confFileName = "./conf/settings.ini"
    envFileName = "./conf/.env"
    logInfo = "./logs/info.log"
    logCritical = "./logs/critical.log"
    logLevel = 20
    
    # Process command line options
    opts, args = getopt.getopt(sys.argv[1:], "", ["settings=","env=","log_level=", "log_info_file=", "log_crit_file="])

    for opt, arg in opts:
        if opt in ['-s', "--settings"]:
            confFileName = arg
        elif opt in ['-e', "--env"]:
            envFileName = arg
        elif opt in ["--log_level"]:
            logLevel = int(arg)
        elif opt in ["--log_info_file"]:
            logInfo = arg
        elif opt in ["--log_crit_file"]:
            logCritical = arg
        else:
            print("Option not handled")
    
    # Logger loading
    Logger.getInstance().loadLogger(infoFile=logInfo, criticalFile=logCritical, level=logLevel)
    
    # Printing options for debug purposes in the logger (i.e in files and console if wanted)
    Logger.getInstance().info("Given options : ")
    Logger.getInstance().info("--settings={}".format(confFileName))
    Logger.getInstance().info("--env={}".format(envFileName))
    Logger.getInstance().info("--log_level={}".format(logLevel))
    Logger.getInstance().info("--log_info_file={}".format(logInfo))
    Logger.getInstance().info("--log_crit_file={}".format(logCritical))

    # Opening informations in .env and .ini files
    load_dotenv(envFileName)

    # Load settings
    Settings.getInstance().loadSettings(confFileName)

if __name__=="__main__":

    # Loading all necessary infos
    startApp()

    # Loading the translations
    i18nLoading(Settings.getInstance().get('language', 'folder', "./resources/translation"), Settings.getInstance().get('language', 'locale', 'en'))

    # Application starting and cleanup adding
    app=QApplication(sys.argv)
    app.aboutToQuit.connect(cleanUp)
    with open(Settings.getInstance().get('style', 'file', './resources/main.qss')) as styleFile:
        app.setStyleSheet(styleFile.read())

    # Main window creation and signals adding
    ex=MainFrame(x=0,y=0,width=app.primaryScreen().size().width(),height=app.primaryScreen().size().height())
    ex.clickedSig.connect(newCityChoosen) # Add a signal on a list item click

    # Starting the weather reading thread
    t1 = QThread()
    weatherWorker = WeatherWorker()
    weatherWorker.setHasToReadWeather(True)
    weatherWorker.setApiKey(os.getenv("API_KEY"))
    weatherWorker.setDelayTime(Settings.getInstance().getint('weather', 'delay', 60))
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
    citiesWorker.setCitiesFileName(Settings.getInstance().get('cities', 'filename', './resources/filtered.list.json'))
    citiesWorker.setChoosenCity(Settings.getInstance().getint('cities', 'choosen', 0))
    citiesWorker.moveToThread(t2)

    t2.started.connect(citiesWorker.run) # Connecting the main loop of the thread
    citiesWorker.progress.connect(progressCitiesWorker) # Conencting to the event of a new city
    citiesWorker.finished.connect(t2.quit) # Connecting to the end of the thread
    citiesWorker.finished.connect(t2.deleteLater) # Connecting to delete the thread
    citiesWorker.finished.connect(citiesWorker.deleteLater) # Connecting to clean up the worker
    citiesWorker.finished.connect(finishedCitiesWorker) # Connecting the main thread function on thread ending
    t2.start() # Starting the thread

    sys.exit(app.exec()) # Starting the application