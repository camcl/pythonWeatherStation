import io
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QWidget
from views.items.BasicItem import BasicItem

import folium

class MapItem(BasicItem):
    """
        This class is used to print a map and all datas

        :author: Panda <panda@delmasweb.net>
        :date: February 01, 2022
        :version: 1.0
    """
    
    def __init__(self, parent: QWidget = None, x: int = 350, y: int = 350, width: int = 200, height: int = 200) -> None:
        """
            Constructor

            :param parent: Optional; Default : None; Parent
            :type parent: QWidget
            :param x: Optional; Default : 300; X Position
            :type x: int
            :param y: Optional; Default : 300; Y Position
            :type y: int
            :param width: Optional; Default : 350; Widget's width
            :type width: int
            :param height: Optional; Default : 350; Widget's height
            :type height: int
        """
        super().__init__(parent, x, y, width, height)
        self.__initWidget()

    def __initWidget(self) -> None:
        """
            This initialize the widget
        """
        self.__view = QWebEngineView()
        self.__map = folium.Map(tiles="OpenStreetMap", zoom_start=2)
        self.__data = io.BytesIO()
        super().getGridLayout().addWidget(self.__view, 0, 0, 1, 1)

    def printTheMap(self) -> None:
        """
            Prints the map
        """
        self.__map.save(self.__data, close_file=False)
        self.__view.setHtml(self.__data.getvalue().decode())

    def addACityOnMap(self, lat : float, lon : float, name : str) -> None:
        """
            Add a marker to the map

            :param lat: The latitude of the place
            :type lat: float
            :param lon: The longitude of the place
            :type lon: float
            :param name: The name of the place
            :type name: str
        """
        folium.Marker(location=[lat, lon], popup=name).add_to(self.__map)