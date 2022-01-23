import json

from PyQt5.QtWidgets import QWidget, QListWidget, QPushButton, QListWidgetItem

from views.myItem import MyItem
from classes.element import position

class CityList(QListWidget):
    """
        Classe qui gere l'affichage de la liste de la liste des villes

        :author: Delmas Pierre <panda@delmasweb.net>
        :date: 30 Août 2021
        :version: 0.3
    """

    def __init__(self, filePath : str = "city.list.json", x : int = 100, y : int = 100, width : int = 400, height : int = 400) -> None:
        """
        Constructeur

        :param filePath: Le chemin de la liste des villes disponible
        :return filePath: str
        :param x: La position du coin en haut a gauche en x
        :type x: int
        :param y: La position du coin en haut a gauche en y
        :type y: int
        :param width: La largeur de la fenetre
        :type width: int
        :param height: La hauteur de la fenetre
        :type height: int
        """
        super().__init__()
        self.__xPos = x
        self.__yPos = y
        self.__width = width
        self.__height = height 
        self.loadNewCitiesList(filePath)
        self.resize(self.__width, self.__height)
        self.move(self.__xPos, self.__yPos)

    def loadNewCitiesList(self, filePath: str = None) -> None:
        """
        Ouvre une liste de ville au format JSON formate OpenWeatherMap
        """
        if(filePath != None):
            with open(filePath, encoding="utf8") as file:
                self.cities = json.load(file)
                self.__turnCitiesToQList()
        else:
            self.cities = None
    
    def __turnCitiesToQList(self) -> QListWidget:
        """
        Formate la liste des villes au format QListWidget de Position et la retourne

        :return: La liste des villes au format QListWidget
        :rtype: QListWidget
        """
        for data in self.cities:
            qitem = MyItem(
                position.Position(
                    name=data['name'], 
                    country=data['country'], 
                    id=data['id'], 
                    longitude=data['coord']['lon'], 
                    latitude=data['coord']['lat'])
                )
            self.addItem(qitem)