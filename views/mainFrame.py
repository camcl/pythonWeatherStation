from PyQt5.QtCore import pyqtSignal, QRect
from PyQt5.QtWidgets import QMainWindow, QWidget

from views.MyItem import MyItem
from views.CityList import CityList
from views.TempItem import TempItem

from classes.element import position

class MainFrame(QMainWindow):

    """
        Classe de la fenetre principale

        :author: Delmas Pierre <panda@delmasweb.net>
        :date: 30 Août 2021
        :version: 0.3
    """

    """
        Signal de clic sur le widget des villes
    """
    clickedSig = pyqtSignal(position.Position)

    """
        Liste des villes (Widget CityList)    
    """
    __cities = None

    """
        La ville courante
    """
    __currentPosition = None

    """
        Partie temperature
    """
    __temp = None

    """
        Nombre de lignes
    """
    __numberOfRows = 10

    """
        Nombre de colonnes
    """
    __numberOfColumns = 10

    """
        Position initiale en x de la fenetre
    """
    __x = 50

    """
        Position initiale en y de la fenetre
    """
    __y = 50

    """
        Largeur initiale de la fenetre
    """
    __width = 1000

    """
        Hauteur initiale de la fenetre
    """
    __height = 1000

    def __init__(self, parent : QWidget = None, appName : str = "My Weather App", borderLess : bool = False, 
        x : int = 50, y : int = 50, width: int = 1000, height: int = 1000) -> None:
        """
        Constructeur

        :param appName: Le nom de l'application
        :type appName: str
        :param borderLess: Si on veut ou non afficher les bordures
        :type borderLess: bool
        :param width: La largeur de la fenetre
        :type width: int
        :param height: La hauteur de la fenetre
        :type height: int
        """
        super().__init__(parent)
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__borderLess = borderLess
        self.__currentPosition = None
        self.initUI()

    def initUI(self):
        """
        Initialise la fenetre et l'affiche
        """
        # On cree une liste vide pour la remplir
        citiesList = CityList()
        self.setCitiesList(citiesList)

        # On cree le widget de la temperature
        temp = TempItem()
        self.setTemp(temp)

        # On set la geometrie de la fenetre et l'affiche
        self.setGeometry(self.__x, self.__y, self.__width, self.__height)
        self.show()

    def setCitiesList(self, citiesList : CityList) -> None:
        """
            Setter de la liste des villes

            :param citiesList: Le widget de liste de villes
            :type citiesList: cities
        """
        self.__cities = citiesList
        self.__cities.setGeometry(200,200,400,400)
        self.layout().addChildWidget(self.__cities)
        self.__cities.itemClicked.connect(self.clicked)

    def getCitiesList(self) -> CityList:
        """
            Getter de la liste des villes

            :rtype: cities
        """
        return self.__cities

    def setTemp(self, temp : TempItem) -> None:
        """
            Setter de l'item de temperature
        """
        self.__temp = temp
        self.layout().addChildWidget(self.__temp)

    def clicked(self, item : MyItem) -> None:
        """
        Fonction qui est execute quand on clique sur un item

        :param item: L'item clique
        :type item: MyItem
        """
        if(self.__currentPosition != None):
            self.__currentPosition.setIsChoosen(False)
        
        self.__currentPosition = item
        self.__currentPosition.setIsChoosen(True)
        self.clickedSig.emit(self.__currentPosition.getPosition())