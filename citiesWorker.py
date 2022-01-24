import json

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QListWidget
from views.cityList import CityList as cities
from views.myItem import MyItem
from classes.element import position

class CitiesWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(MyItem)
    __citiesFileName = None
    __citiesList = None
    __cities = None
    __choosenCity = -1

    def setCitiesFileName(self, citiesFileName : str) -> None:
        self.__citiesFileName = citiesFileName

    def getCitiesList(self) -> cities:
        return self.__citiesList

    def setChoosenCity(self, choosenCity : int) -> None:
        self.__choosenCity = choosenCity
    
    def loadNewCitiesList(self) -> None:
        """
        Ouvre une liste de ville au format JSON formate OpenWeatherMap
        """
        if(self.__citiesFileName != None):
            with open(self.__citiesFileName, encoding="utf8") as file:
                self.__cities = json.load(file)
        else:
            self.__cities = None

    def run(self):
        if(self.__citiesFileName != None):
            self.loadNewCitiesList()
            for data in self.__cities:
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
        else:
            self.progress.emit(1)