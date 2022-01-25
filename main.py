import os
import sys
import logging

from dotenv import load_dotenv
from configparser import ConfigParser
from classes.element import position
from classes.element.weather import Weather as weather

from views.MainFrame import MainFrame
from views.MyItem import MyItem

from workers.CitiesWorker import CitiesWorker
from workers.WeatherWorker import WeatherWorker

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread

# Variables globales utilises par tous les threads
hasToReadWeather = True
logger = logging.getLogger("WeatherApp")

def cleanUp():
    """
        Fonction de nettoyage a la mort de l'application
    """
    weatherWorker.setHasToReadWeather(False)
    with open("settings.ini", encoding="utf8", mode="w") as file:
        configur.write(file)

def loadLogger():
    """
        Charge les informations du logger
    """
    # Creation des informations de logging
    #logging.basicConfig(filename=configur.get('logging', 'filename'), level=configur.getint('logging', 'level'), format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')

    # Le formattage des logs
    formatter = logging.Formatter("%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")

    # Les handlers pour les messages critiques et d'infos et de debug
    handler_critic = logging.FileHandler("logs/critic.log", mode="a", encoding="utf-8")
    handler_info = logging.FileHandler("logs/info.log", mode="a", encoding="utf-8")
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
    """
        Fonction execute a la reception d'une nouvelle meteo depuis le weatherWorker
    """
    if weather == None:
        logger.error("No weather provided")
    else:
        logger.debug(weather)

def finishedWeatherWorker() -> None:
    """
        Fonction executee a la fin du weatherWorker
    """
    logger.info("Weather worker has finished")

def progressCitiesWorker(item : MyItem) -> None:
    """
        Fonction executee a la reception d'une nouvelle information du cityWorker

        :param item: L'item recu
        :type item: MyItem
    """
    if(item != None):
        ex.getCitiesList().addItem(item)
        if(item.isChoosen()):
            ex.getCitiesList().setCurrentItem(item)
            newCityChoosen(item.getPosition())
    else:
        logger.error("Cities can't load properly")

def finishedCitiesWorker() -> None:
    """
        Fonction executee a la fin du cityWorker
    """
    ex.update()
    logger.debug("Cities loading finished")

def newCityChoosen(position : position.Position) -> None:
    """
        Fonction executee quand on clic sur une nouvelle ville dans la liste
    """
    logger.debug("New city choosen : "+str(position))
    configur.set('cities', 'choosen', value=str(position.getId()))
    weatherWorker.setCurrentPosition(position)

if __name__=="__main__":
    # Ouverture des informations dans les fichiers .env et .ini
    load_dotenv('conf/.env')
    configur = ConfigParser()
    configur.read('conf/settings.ini')

    # Chargement du logger
    loadLogger()

    # Creation de l'application principale et ajout de la fonction de cleanup pour arreter les threads notamment
    app=QApplication(sys.argv)
    app.aboutToQuit.connect(cleanUp)

    # Creation de la fenetre principale
    ex=MainFrame()
    ex.clickedSig.connect(newCityChoosen)

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

    sys.exit(app.exec_())