import json

from typing import Any

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QListWidget
from views.cityList import CityList as cities
from views.myItem import MyItem
from classes.element import position

class CitiesWorker(QObject):

    """
        Signal de fin du worker 
    """
    finished = pyqtSignal()
    
    """
        Signal du worker en cours de travail
    """
    progress = pyqtSignal(MyItem)

    """
        Nom du fichier
    """
    __citiesFileName = None

    """
        Ville choisie
    """
    __choosenCity = -1

    def setCitiesFileName(self, citiesFileName : str) -> None:
        """
        Setter du nom du fichier des villes

        :param citiesFileName: Le nom du fichier 
        :type citiesFileName: str
        """
        self.__citiesFileName = citiesFileName

    def setChoosenCity(self, choosenCity : int) -> None:
        """
        Setter de l'identifiant de la ville choisi préalablement choisie

        :param choosenCity: L'identifiant de la ville
        :type choosenCity: int
        """
        self.__choosenCity = choosenCity
    
    def loadNewCitiesList(self) -> Any:
        """
        Ouvre une liste de ville au format JSON formate OpenWeatherMap

        :return: La liste des villes
        :rtype: Any
        """
        citiesList = {}
        if(self.__citiesFileName != None):
            with open(self.__citiesFileName, encoding="utf8") as file:
                citiesList = json.load(file)
        else:
            citiesList = None
        return citiesList

    def run(self):
        """
        Fonction principale du thread qui sera executee
        """
        if(self.__citiesFileName != None):
            citiesList = self.loadNewCitiesList()
            for data in citiesList:
                if(data['country'] == "FR"):
                    qitem = MyItem(
                        position.Position(
                            name=data['name'], 
                            country=data['country'], 
                            id=data['id'], 
                            longitude=data['coord']['lon'], 
                            latitude=data['coord']['lat']),
                        isChoosen=int(data['id'])==self.__choosenCity
                        )
                    self.progress.emit(qitem)
            self.finished.emit()
        self.finished.emit()