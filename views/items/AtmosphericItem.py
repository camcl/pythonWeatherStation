from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QSizePolicy
from views.items.BasicItem import BasicItem
import i18n

class AtmosphericItem(BasicItem):
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
        super().__init__(parent, x, y, width, height)
        self.__initWidget()

    def __initWidget(self) -> None:
        """
            Init the widget
        """
        self.__windSpeed = QLabel()
        self.__windSpeed.setStyleSheet("QLabel { background-color : yellow; }")
        self.__windSpeed.setText(i18n.t("translate.init"))
        self.__windSpeed.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.__windSpeed.setAlignment(Qt.AlignmentFlag.AlignCenter)
        super().getGridLayout().addWidget(self.__windSpeed, 0, 0, 1, 1)

        self.__windDirection = QLabel()
        self.__windDirection.setStyleSheet("QLabel { background-color : blue; }")
        self.__windDirection.setText(i18n.t("translate.init"))
        self.__windDirection.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.__windDirection.setAlignment(Qt.AlignmentFlag.AlignCenter)
        super().getGridLayout().addWidget(self.__windDirection, 0, 1, 1, 1)

        self.__pressure = QLabel()
        self.__pressure.setStyleSheet("QLabel { background-color : red; }")
        self.__pressure.setText(i18n.t("translate.init"))
        self.__pressure.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.__pressure.setAlignment(Qt.AlignmentFlag.AlignCenter)
        super().getGridLayout().addWidget(self.__pressure, 0, 2, 1, 1)

        self.__humidity = QLabel()
        self.__humidity.setStyleSheet("QLabel { background-color : purple; }")
        self.__humidity.setText(i18n.t("translate.init"))
        self.__humidity.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.__humidity.setAlignment(Qt.AlignmentFlag.AlignCenter)
        super().getGridLayout().addWidget(self.__humidity, 0, 3, 1, 1)

    def setWindSpeedValue(self, windSpeed : float) -> None:
        """
            Set the text inside the wind speed label

            :param windSpeed: The value to print
            :type windSpeed: float
        """
        self.__windSpeed.setText(i18n.t("translate.wind.speed", value=windSpeed))
    
    def setWindDirectionValue(self, windDirection : int) -> None:
        """
            Set the text inside the wind direction label

            :param windDirection: The value to print
            :type windDirection: int
        """
        self.__windDirection.setText(i18n.t("translate.wind.direction", value=windDirection))

    def setPressureValue(self, pressure : int) -> None:
        """
            Set the text inside the pressure label

            :param pressure: The value to print
            :type pressure: int
        """
        self.__pressure.setText(i18n.t("translate.atmo.pressure", value=pressure))

    def setHumidityValue(self, humidity : int) -> None:
        """
            Set the text inside the humidity label

            :param humidity: The value to print
            :type humidity: int
        """
        self.__humidity.setText(i18n.t("translate.atmo.humidity", value=humidity))