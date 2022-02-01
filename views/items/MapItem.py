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
        self.__view.setContentsMargins(50, 50, 50, 50)
        map = folium.Map()

        data = io.BytesIO()
        map.save(data, close_file=False)