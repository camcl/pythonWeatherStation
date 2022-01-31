from PyQt5.QtCore import Qt
from PyQt5.QtGui  import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QSizePolicy

import i18n

class TempItem(QWidget):
    """
        Temperature part manager

        :author: Panda <panda@delmasweb.net>
        :date: January 15, 2022
        :version: 1.0
    """

    """
        QLabel to print the current temperature
    """
    __labelCurrent = None

    """
        QLabel to print the feels like temperature
    """
    __labelFeels = None

    """
        QLabel to print the maximal temperature
    """
    __labelMax = None

    """
        QLabel to print the minimal temperature
    """
    __labelMin = None

    """
        X Position of the widget
    """
    __realX = 300

    """
        Y Position of the widget
    """
    __realY = 300

    """
        Width of the widget
    """
    __realWidth = 350

    """
        Height of the widget
    """
    __realHeight = 350

    """
        Number of columns in the grid of the widget
    """
    __numberOfColumns = 5

    """
        The internal grid
    """
    __gridLayout = None

    def __init__(self, parent: QWidget = None, x : int = 300, y : int = 300, width : int = 350, height : int = 350) -> None:
        """
            Constructeur

            :param parent: Optional; Default : None; Parent
            :type parent: QWidget
            :param x: Optional; Default : 300; X Position
            :type x: int
            :param y: Optional; Default : 300; Y Position
            :type y: int
            :param width: Optional; Default : 350; Widget's width
            :type width: int
            :param height: Optional; Default : 350; Height's height
            :type height: int
        """
        super().__init__(parent)
        self.__realX = x
        self.__realY = y
        self.__realWidth = width
        self.__realHeight = height
        self.initWidget()

    def initWidget(self):
        """
            Create the labels
        """
        self.__gridLayout = QGridLayout(self)

        # Le label de la meteo courante
        self.__labelCurrent = QLabel()
        self.__labelCurrent.setStyleSheet("QLabel { background-color : red; }")
        self.__labelCurrent.setText("TEST")
        self.__labelCurrent.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.__labelCurrent.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__labelCurrent.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        fontType = QFont()
        fontType.setBold(True)
        fontType.setPointSize(20)
        self.__labelCurrent.setFont(fontType)
        self.__gridLayout.addWidget(self.__labelCurrent, 0, 0, 2, self.__numberOfColumns)
        
        #Le label de la meteo ressentie
        self.__labelFeels = QLabel()
        self.__labelFeels.setStyleSheet("QLabel { background-color : yellow; }")
        self.__labelFeels.setText("TEST II")
        self.__labelFeels.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.__labelFeels.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__gridLayout.addWidget(self.__labelFeels, 2, 1, 1, 1)

        #Le label de la meteo minimale
        self.__labelMin = QLabel()
        self.__labelMin.setStyleSheet("QLabel { background-color : purple; }")
        self.__labelMin.setText("TEST III")
        self.__labelMin.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.__labelMin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__gridLayout.addWidget(self.__labelMin, 2, 2, 1, 1)

        #Le label de la meteo ressentie
        self.__labelMax = QLabel()
        self.__labelMax.setStyleSheet("QLabel { background-color : orange; }")
        self.__labelMax.setText("TEST IV")
        self.__labelMax.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.__labelMax.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__gridLayout.addWidget(self.__labelMax, 2, 3, 1, 1)

        self.setGeometry(self.__realX, self.__realY, self.__realWidth, self.__realHeight)

    def setCurrentTempText(self, temp : float, unit : str) -> None:
        """
            This function set the text for the current label

            :param temp: The temperature to print
            :type temp: float
            :param unit: The unit of the value
            :type unit: str
        """
        self.__labelCurrent.setText(i18n.t('translate.temperature.current', value=temp, unit=unit))
    
    def setFeelsLikeTempText(self, temp : float, unit : str) -> None:
        """
            This function set the text for the current label

            :param temp: The temperature to print
            :type temp: float
            :param unit: The unit of the value
            :type unit: str
        """
        self.__labelFeels.setText(i18n.t('translate.temperature.feelslike', value=temp, unit=unit))

    def setMaxTempText(self, temp : float, unit : str) -> None:
        """
            This function set the text for the current label

            :param temp: The temperature to print
            :type temp: float
            :param unit: The unit of the value
            :type unit: str
        """
        self.__labelMax.setText(i18n.t('translate.temperature.max', value=temp, unit=unit))

    def setMinTempText(self, temp : float, unit : str) -> None:
        """
            This function set the text for the current label

            :param temp: The temperature to print
            :type temp: float
            :param unit: The unit of the value
            :type unit: str
        """
        self.__labelMin.setText(i18n.t('translate.temperature.min', value=temp, unit=unit).format("%.06f"))
        