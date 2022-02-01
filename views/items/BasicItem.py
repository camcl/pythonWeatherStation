from PyQt6.QtWidgets import QWidget, QGridLayout

class BasicItem(QWidget):
    """
        This class is used to print all data

        :author: Panda <panda@delmasweb.net>
        :date: February 01, 2022
        :version: 1.0
    """
    
    def __init__(self, parent : QWidget = None, x : int = 350, y : int = 350, width : int = 200, height : int = 200) -> None:
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
        super().__init__(parent)
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        
        self.__gridLayout = QGridLayout(self)
        
        self.setGeometry(self.__x, self.__y, self.__width, self.__height)

    def getGridLayout(self) -> QGridLayout:
        """
            The grid layout getter

            :return: The grid layout
            :rtype: QGridLayout
        """
        return self.__gridLayout