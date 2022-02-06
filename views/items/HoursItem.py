from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QSizePolicy

from views.items.BasicItem import BasicItem

from datetime import datetime
import i18n
from pytz import timezone

class HoursItem(BasicItem):
    """
        This class is used to print the sunset and sunrise hour

        :author: Panda <panda@delmasweb.net>
        :date: January 15, 2022
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
            Init the widget by creating the elements
        """

        # The hour of sunrise
        self.__sunriseLabel = QLabel()
        self.__sunriseLabel.setText(i18n.t("translate.init"))
        self.__sunriseLabel.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.__sunriseLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        super().getGridLayout().addWidget(self.__sunriseLabel, 0, 0, 1, 1)

        # The hour of sunset
        self.__sunsetLabel = QLabel()
        self.__sunsetLabel.setText(i18n.t("translate.init"))
        self.__sunsetLabel.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.__sunsetLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        super().getGridLayout().addWidget(self.__sunsetLabel, 1, 0, 1, 1)

    def setSunsetValue(self, sunset : int, zone : str = "Etc/Greenwich") -> None:
        """
            This function set the text for the sunset element

            :param sunset: The value in UNIX Epoch UTC time
            :type sunset: int
            :param zone: The local timezone
            :type zone: str
        """
        if(sunset == -1):
            self.__sunsetLabel.setText(i18n.t("translate.init"))
        else:
            format="%H:%M:%S"
            self.__sunsetLabel.setText(i18n.t("translate.time.sunset", hour=datetime.fromtimestamp(sunset, tz=timezone(zone)).strftime(format)))

    def setSunriseValue(self, sunrise : int, zone : str = "Etc/Greenwich") -> None:
        """
            This function set the text for the sunrise element

            :param sunrise: The value in UNIX Epoch UTC time
            :type sunrise: int
            :param zone: The local timezone
            :type zone: str
        """
        if(sunrise == -1):
            self.__sunriseLabel.setText(i18n.t("translate.init"))
        else:
            format="%H:%M:%S"
            self.__sunriseLabel.setText(i18n.t("translate.time.sunrise", hour=datetime.fromtimestamp(sunrise, tz=timezone(zone)).strftime(format)))