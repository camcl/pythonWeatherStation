from PyQt5.QtWidgets import QListWidget,QWidget


class CityList(QListWidget):
    """
        Cities list manager

        :author: Delmas Pierre <panda@delmasweb.net>
        :date: January 15, 2022
        :version: 1.0
    """

    def __init__(self, parent : QWidget = None, x : int = 100, y : int = 100, width : int = 400, height : int = 400) -> None:
        """
            Constructeur


            :param parent: Optional; Default : None; The parent of the widget
            :return parent: str
            :param x: Optional; Default : 100; The top left corner x position 
            :type x: int
            :param y: Optional; Default : 100; The top left corner y position
            :type y: int
            :param width: Optional; Default : 400; The widget's width
            :type width: int
            :param height: Optional; Default : 100; The widget's height
            :type height: int
        """
        super().__init__(parent)
        self.__xPos = x
        self.__yPos = y
        self.__width = width
        self.__height = height
        self.resize(self.__width, self.__height)
        self.move(self.__xPos, self.__yPos)