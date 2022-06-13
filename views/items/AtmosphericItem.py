from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QSizePolicy
from views.items.basicItem import BasicItem
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
        self.__windSpeedLabel = QLabel()
        self.__windSpeedLabel.setText(i18n.t("translate.init"))
        self.__windSpeedLabel.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.__windSpeedLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        super().getGridLayout().addWidget(self.__windSpeedLabel, 0, 0, 1, 1)

        self.__windDirectionLabel = QLabel()
        self.__windDirectionLabel.setText(i18n.t("translate.init"))
        self.__windDirectionLabel.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.__windDirectionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        super().getGridLayout().addWidget(self.__windDirectionLabel, 0, 1, 1, 1)

        self.__pressureLabel = QLabel()
        self.__pressureLabel.setText(i18n.t("translate.init"))
        self.__pressureLabel.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.__pressureLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        super().getGridLayout().addWidget(self.__pressureLabel, 0, 2, 1, 1)

        self.__humidityLabel = QLabel()
        self.__humidityLabel.setText(i18n.t("translate.init"))
        self.__humidityLabel.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.__humidityLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        super().getGridLayout().addWidget(self.__humidityLabel, 0, 3, 1, 1)

    def setWindSpeedValue(self, windSpeed : float) -> None:
        """
            Set the text inside the wind speed label

            :param windSpeed: The value to print
            :type windSpeed: float
        """
        self.__windSpeedLabel.setText(i18n.t("translate.wind.speed", value=windSpeed))
    
    def setWindDirectionValue(self, windDirection : int) -> None:
        """
            Set the text inside the wind direction label

            :param windDirection: The value to print
            :type windDirection: int
        """
        self.__windDirectionLabel.setText(i18n.t("translate.wind.direction", value=windDirection))

    def setPressureValue(self, pressure : int) -> None:
        """
            Set the text inside the pressure label

            :param pressure: The value to print
            :type pressure: int
        """
        self.__pressureLabel.setText(i18n.t("translate.atmo.pressure", value=pressure))

    def setHumidityValue(self, humidity : int) -> None:
        """
            Set the text inside the humidity label

            :param humidity: The value to print
            :type humidity: int
        """
        self.__humidityLabel.setText(i18n.t("translate.atmo.humidity", value=humidity))