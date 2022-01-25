from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGridLayout, QWidget

from views.myItem import MyItem
from views.cityList import CityList as cities
from views.TempItem import TempItem

from classes.element import position

class MainGrid(QGridLayout):

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

    def __init__(self, parent : QWidget = None):
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
        self.__currentPosition = None
        
        self.initUI()

    def initUI(self):
        """
        Initialise la fenetre et l'affiche
        """
        #self.setWindowTitle(self.title)
        #self.setGeometry(self.left,self.top,self.width,self.height)

        #self.show()
        
        # On cree une liste vide pour la remplir
        citiesList = cities()
        self.setCitiesList(citiesList)

        # On cree le widget de la temperature
        temp = TempItem()
        self.setTemp(temp)

        self.update()

    def setCitiesList(self, citiesList : cities) -> None:
        """
            Setter de la liste des villes

            :param citiesList: Le widget de liste de villes
            :type citiesList: cities
        """
        self.__cities = citiesList
        self.addWidget(self.__cities, 5, 5, 4, 4)
        self.__cities.itemClicked.connect(self.clicked)

    def getCitiesList(self) -> cities:
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
        self.addLayout(self.__temp, 5, 5, 3, 3)

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