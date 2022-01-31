from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QWidget

from views.MyItem import MyItem
from views.CityList import CityList
from views.TempItem import TempItem

from classes.element.Position import Position

import i18n

class MainFrame(QMainWindow):

    """
        Main Window

        :author: Panda <panda@delmasweb.net>
        :date: January 15, 2022
        :version: 1.0
    """

    """
        Clicking signal on the cities list
    """
    clickedSig = pyqtSignal(Position)

    """
        Cities List Widget   
    """
    __cities = None

    """
        Current position to be monitored
    """
    __currentPosition = None

    """
        Temperature widget
    """
    __temp = None

    """
        Inital position of the window in x
    """
    __x = 50

    """
        Initial position of the window in y
    """
    __y = 50

    """
        initial width of the window
    """
    __width = 1000

    """
        Initial height of the window
    """
    __height = 1000

    def __init__(self, parent : QWidget = None, appName : str = "My Weather App", borderLess : bool = False, 
        x : int = 50, y : int = 50, width: int = 1000, height: int = 1000) -> None:
        """
        Constructor

        :param parent: Optional; Default : None; The parent of this window
        :type parent: QWidget
        :param appName: Optional; Default : "My Weather App"; Application name
        :type appName: str
        :param borderLess: Optional; Default : False; If we want or no the border
        :type borderLess: bool
        :param x: Optional; Default : 50; X position of the window
        :type x: int
        :param y: Optional; Default : 50; Y position of the window
        :type y: int
        :param width: Optional; Default : 1000; Window's width
        :type width: int
        :param height: Optional; Default : 1000; Window's height
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
            Window initialisation (widgets creation) and positionning
        """
        # On cree une liste vide pour la remplir
        citiesList = CityList(x=self.__width * 0.1, y=self.__height * 0.1, width= self.__width * 0.3, height=self.__height * 0.6)
        self.setCitiesList(citiesList)

        # On cree le widget de la temperature
        temp = TempItem(x=self.__width * 0.4, y=self.__height * 0.1, width=self.__width * 0.25, height= self.__height * 0.3)
        self.setTemp(temp)

        # On set la geometrie de la fenetre et l'affiche
        self.setFixedSize(self.__width, self.__height)
        self.move(self.__x, self.__y)
        self.show()

    def setCitiesList(self, citiesList : CityList) -> None:
        """
            Cities List widget setter

            :param citiesList: The new widget of the cities
            :type citiesList: CityList
        """
        self.__cities = citiesList
        self.layout().addChildWidget(self.__cities)
        self.__cities.itemClicked.connect(self.clicked)

    def getCitiesList(self) -> CityList:
        """
            CitiesList getter

            :rtype: CityList
        """
        return self.__cities

    def setTemp(self, temp : TempItem) -> None:
        """
            Temperature widget setter

            :param temp: The temperature item
            :type temp: TempItem
        """
        self.__temp = temp
        self.layout().addChildWidget(self.__temp)

    def getTemp(self) -> TempItem:
        """
            Temperature widget getter

            :return: The temperature widget
            :rtype: TempItem
        """
        return self.__temp

    def clicked(self, item : MyItem) -> None:
        """
            Function to be executed when an item is clicked in the cities list
            Send a signal if the clicked item

            :param item: Clicked item
            :type item: MyItem
        """
        if(self.__currentPosition != None):
            self.__currentPosition.setIsChoosen(False)
        
        self.__currentPosition = item
        self.__currentPosition.setIsChoosen(True)
        self.clickedSig.emit(self.__currentPosition.getPosition())