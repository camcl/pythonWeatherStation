from email.encoders import encode_noop
import os
import sys
import logging

from dotenv import load_dotenv
from configparser import ConfigParser
from classes.element import position
from classes.element.weather import Weather as weather

from views.mainFrame import MainFrame as App
from views.myItem import MyItem
from views.cityList import CityList as cities

from citiesWorker import CitiesWorker
from weatherWorker import WeatherWorker

from PyQt5.QtWidgets import QApplication, QListWidget
from PyQt5.QtCore import QThread


# Variables globales utilises par tous les threads
hasToReadWeather = True
logger = logging.getLogger("WeatherApp")


def loadCities() -> None:
    ex.printListOfCities(os.getenv("CITY_FILE"))
    logger.debug("Cities list is loaded")
        
def cleanUp():
    weatherWorker.setHasToReadWeather(False)
    with open("settings.ini", encoding="utf8", mode="w") as file:
        configur.write(file)

def loadLogger():
    # Creation des informations de logging
    #logging.basicConfig(filename=configur.get('logging', 'filename'), level=configur.getint('logging', 'level'), format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')

    # Le formattage des logs
    formatter = logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")

    # Les handlers pour les messages critiques et d'infos et de debug
    handler_critic = logging.FileHandler("critic.log", mode="a", encoding="utf-8")
    handler_info = logging.FileHandler("info.log", mode="a", encoding="utf-8")
    handler_debug = logging.StreamHandler(sys.stdout)

    handler_critic.setFormatter(formatter)
    handler_info.setFormatter(formatter)
    handler_debug.setFormatter(formatter)

    handler_debug.setLevel(logging.DEBUG)
    handler_info.setLevel(logging.INFO)
    handler_critic.setLevel(logging.CRITICAL)

    logger.setLevel(configur.getint('logging', 'level'))
    logger.addHandler(handler_critic)
    logger.addHandler(handler_info)
    logger.addHandler(handler_debug)

def progressWeatherWorker(weather : weather) -> None:
    if weather == None:
        logger.error("No weather provided")
    else:
        logger.debug(weather)

def finishedWeatherWorker() -> None:
    logger.info("Weather worker has finished")

def progressCitiesWorker(item : MyItem) -> None:
    if(item != None):
        citiesList.addItem(item)
        if(item.isChoosen()):
            citiesList.setCurrentItem(item)
            newCityChoosen(item.getPosition())
    else:
        logger.error("Cities can't load properly")

def finishedCitiesWorker() -> None:
    ex.update()
    logger.debug("Cities loading finished")

def newCityChoosen(position : position.Position) -> None:
    logger.debug("New city choosen : "+str(position))
    configur.set('cities', 'choosen', value=str(position.getId()))
    weatherWorker.setCurrentPosition(position)

if __name__=="__main__":
    # Ouverture des informations dans les fichiers .env et .ini
    load_dotenv()
    configur = ConfigParser()
    configur.read('settings.ini')

    # Chargement du logger
    loadLogger()

    # Creation de l'application principale et ajout de la fonction de cleanup pour arreter les threads notamment
    app=QApplication(sys.argv)
    app.aboutToQuit.connect(cleanUp)

    # Creation de la fenetre principale
    ex=App()
    ex.clickedSig.connect(newCityChoosen)

    # On cree une liste vide pour la remplir
    citiesList = cities()
    ex.setCitiesList(citiesList)

    # Creation du thread de lecture des informations de meteo et demarrage du dit-thread
    t1 = QThread()
    weatherWorker = WeatherWorker()
    weatherWorker.setHasToReadWeather(True)
    weatherWorker.setApiKey(os.getenv("API_KEY"))
    weatherWorker.setDelayTime(configur.getint('weather', 'delay'))
    weatherWorker.moveToThread(t1)

    t1.started.connect(weatherWorker.run) # On connecte la fonction principale du worker de meteo
    weatherWorker.progress.connect(progressWeatherWorker) # On connecte la fonction de suivi de la meteo avec l'evenement progress qui est emis
    weatherWorker.finished.connect(t1.quit) # On connecte la fonction d'arret du thread 
    weatherWorker.finished.connect(t1.deleteLater) # On connecte la fonction de suppression du thread a l'arret
    weatherWorker.finished.connect(weatherWorker.deleteLater) # On connecte la fonction de suppression du worker a l'arret du thread
    weatherWorker.finished.connect(finishedWeatherWorker) # On connecte notre propre fonction de suivi d'arret du thread
    t1.start() # On demarre le thread

    # Creation du thread de lecture des villes
    t2 = QThread()
    citiesWorker = CitiesWorker()
    citiesWorker.setCitiesFileName(configur.get('cities', 'filename'))
    citiesWorker.setChoosenCity(configur.getint('cities', 'choosen'))
    citiesWorker.moveToThread(t2)

    t2.started.connect(citiesWorker.run) # On connecte la fonction principale du worker de meteo
    citiesWorker.progress.connect(progressCitiesWorker) # On connecte la fonction de suivi de la meteo avec l'evenement progress qui est emis
    citiesWorker.finished.connect(t2.quit) # On connecte la fonction d'arret du thread 
    citiesWorker.finished.connect(t2.deleteLater) # On connecte la fonction de suppression du thread a l'arret
    citiesWorker.finished.connect(citiesWorker.deleteLater) # On connecte la fonction de suppression du worker a l'arret du thread
    citiesWorker.finished.connect(finishedCitiesWorker) # On connecte notre propre fonction de suivi d'arret du thread
    t2.start() # On demarre le thread

    # Lancement de la boucle principale
    ex.show()
    sys.exit(app.exec_())