from PyQt5.QtWidgets import QMainWindow

from views.myItem import MyItem
from views.cityList import CityList as cities

from classes.element import position

class MainFrame(QMainWindow):

    """
        Classe de la fenetre principale

        :author: Delmas Pierre <panda@delmasweb.net>
        :date: 30 Août 2021
        :version: 0.3
    """

    def __init__(self, appName : str = "My Weather App", borderLess : bool = False, width: int = 1000, height: int = 1000):

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
        super().__init__()
        self.title=appName
        self.left=10
        self.top=10
        self.__currentPosition = None
        self.width=width
        self.height=height
        self.initUI()

    def initUI(self):
        """
        Initialise la fenetre et l'affiche
        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

    def printListOfCities(self, citiesFilePath : str = None):
        """
        Cette methode affiche la liste des villes disponible dans le fichier que l'on charge

        :param citiesFilePath: Le chemin du fichier a charger
        :type citiesFilePath: str
        """
        if(citiesFilePath != None):
            citiesList = cities(citiesFilePath) # On charge la liste des villes
            self.layout().addChildWidget(citiesList)
            citiesList.itemClicked.connect(self.clicked)

    def clicked(self, item : MyItem) -> None:
        """
        Fonction qui est execute quand on clique sur un item

        :param item: L'item clique
        :type item: QListWidgetItem
        """
        self.__currentPosition = item.getPosition()
        print(self.getCurrentPosition())
    
       
    def getCurrentPosition(self) -> position.Position:
        """
        Retourne la position courante choisi

        :rtype: position.Position
        """
        return self.__currentPosition