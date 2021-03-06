import json

from PyQt6.QtCore import QObject, pyqtSignal
from views.lists.myItem import MyItem
from classes.element.position import Position

class CitiesWorker(QObject):
    """
        Cities list worker

        :author: Panda <panda@delmasweb.net>
        :date: January 15, 2022
        :version: 1.0
    """

    """
        pyqtSignal to be sent if the worker is over 
    """
    finished = pyqtSignal()
    
    """
        pyqtSignal to be sent while the worker is in progress
    """
    progress = pyqtSignal(MyItem)

    """
        Cities file name
    """
    __citiesFileName = None

    """
        Choosen city id. To be used with the value of the settings file
    """
    __choosenCity = -1

    def setCitiesFileName(self, citiesFileName : str) -> None:
        """
            Cities file name setter

            :param citiesFileName: Path of the file 
            :type citiesFileName: str
        """
        self.__citiesFileName = citiesFileName

    def setChoosenCity(self, choosenCity : int) -> None:
        """
            Choosen city identifier

            :param choosenCity: City identifier
            :type choosenCity: int
        """
        self.__choosenCity = choosenCity
    
    def loadNewCitiesList(self) -> dict:
        """
            Function that opens the file from a JSON and return it as a dictionnary

            :return: The cities list 
            :rtype: dict
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
            Main loop of the worker
        """
        if(self.__citiesFileName != None):
            citiesList = self.loadNewCitiesList()
            for data in citiesList:
                if(data['country'] == "FR"):
                    qitem = MyItem(
                        Position(
                            name=str(data['name']), 
                            country=str(data['country']), 
                            id=int(data['id']), 
                            longitude=float(data['coord']['lon']), 
                            latitude=float(data['coord']['lat'])),
                        isChoosen=int(data['id'])==self.__choosenCity
                        )
                    self.progress.emit(qitem)
        self.finished.emit()