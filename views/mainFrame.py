from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QWidget
from views.items.MapItem import MapItem

from views.lists.MyItem import MyItem
from views.lists.CityList import CityList
from views.items.HoursItem import HoursItem
from views.items.TempItem import TempItem
from views.items.AtmosphericItem import AtmosphericItem

from classes.element.Position import Position

class MainFrame(QMainWindow):
    """
        Main Window

        :author: Panda <panda@delmasweb.net>
        :date: January 15, 2022
        :version: 1.0
    """

    """
        Clicking pyqtSignal on the cities list
    """
    clickedSig = pyqtSignal(Position)

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
        # Creating an empty list for cities
        #citiesList = CityList(x=self.__width * 0.1, y=self.__height * 0.1, width= self.__width * 0.3, height=self.__height * 0.6)
        #self.__setCitiesList(citiesList)

        # Creating the temperature widget 
        temp = TempItem(x=self.__width * 0.7, y=self.__height * 0.1, width=self.__width * 0.25, height= self.__height * 0.3)
        self.__setTemp(temp)

        # Creating the sunset/sunrise widget
        sunHours = HoursItem(x=self.__width * 0.7, y=self.__height * 0.4, width=self.__width * 0.25, height=self.__height * 0.3)
        self.__setSunHours(sunHours)

        # Creating the atmo item
        atm = AtmosphericItem(x=self.__width * 0.1, y=self.__height * 0.7, width=self.__width * 0.8, height=self.__height * 0.15)
        self.__setAtm(atm)

        # The map
        mMap = MapItem(x=self.__width * 0.1, y=self.__height * 0.1, width=self.__width * 0.6, height=self.__height * 0.6)
        self.__setMap(mMap)

        # Setting the size of the window
        self.setFixedSize(self.__width, self.__height)
        self.move(self.__x, self.__y)
        self.show()

    def __setCitiesList(self, citiesList : CityList) -> None:
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

    def __setTemp(self, temp : TempItem) -> None:
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

    def __setSunHours(self, sunHours : HoursItem) -> None:
        """
            Sunhours widget setter

            :param sunHours: The widget of sun hours
            :type sunHours: HoursItem
        """
        self.__sunHours = sunHours
        self.layout().addChildWidget(self.__sunHours)

    def getSunHours(self) -> HoursItem:
        """
            Sunhours widget getter

            :return: The widget of sun hours
            :rtype: HoursItem
        """
        return self.__sunHours
    
    def __setAtm(self, atm : AtmosphericItem) -> None:
        """
            Atm widget setter

            :param atm: The widget of sun hours
            :type atm: AtmosphericItem
        """
        self.__atm = atm
        self.layout().addChildWidget(self.__atm)

    def getAtm(self) -> AtmosphericItem:
        """
            Atm widget getter

            :return: The widget of atm
            :rtype: AtmosphericItem
        """
        return self.__atm

    def __setMap(self, mMap : MapItem) -> None:
        """
            Map widget setter

            :param map: The widget of sun hours
            :type map: MapItem
        """
        self.__map = mMap
        self.layout().addChildWidget(self.__map)

    def getMap(self) -> MapItem:
        """
            Atm widget getter

            :return: The widget of atm
            :rtype: MapItem
        """
        return self.__map

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