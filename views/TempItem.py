from PyQt5.QtCore import QRect, QPoint
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout

class TempItem(QGridLayout):
    """
        QLabel temperature courante
    """
    __labelCurrent = None

    """
        QLabel temperature ressentie
    """
    __labelFeels = None

    """
        QLabel temperature max
    """
    __labelMax = None

    """
        QLabel temperature min
    """
    __labelMin = None

    """
        Position en X
    """
    __realX = 300

    """
        Position en Y
    """
    __realY = 300

    """
        Largeur reelle
    """
    __realWidth = 350

    """
        Hauteur reelle
    """
    __realHeight = 350

    """
        Nombre de colonnes
    """
    __numberOfColumns = 5

    """
        Nombre de lignes
    """
    __numberOfRows = 4

    def __init__(self, parent: QWidget = None, x : int = 300, y : int = 300, width : int = 350, height : int = 350) -> None:
        """
            Constructeur

            :param parent: Parent
            :type parent: QWidget
            :param x: La position du coin en haut a gauche en x
            :type x: int
            :param y: La position du coin en haut a gauche en y
            :type y: int
            :param width: La largeur de la fenetre
            :type width: int
            :param height: La hauteur de la fenetre
            :type height: int
        """
        super().__init__(parent)
        self.__realX = x
        self.__realY = y
        self.__realWidth = width
        self.__realHeight = height
        self.initUI()

    def initUI(self):
        """
            Cree les differents labels
        """
        # Le label de la meteo courante
        self.__labelCurrent = QLabel(None)
        self.__labelCurrent.setText("TEST")
        self.addWidget(self.__labelCurrent, 0, 0, self.__numberOfRows, 2)
        
        #Le label de la meteo ressentie
        