class Miscellaneaous:
    """
        This class represents all misc data for weather like pressure, humidity, ...

        :author: Panda <panda@delmasweb.net>
        :date: January 31, 2022
        :version: 1.0
    """

    def __init__(self, pressure : int = -1, humidity : int = -1, sunset : int = -1, sunrise : int = -1):
        """
            Constructor

            :param pressure: Optional; Default : -1; Place's pressure
            :type pressure: int
            :param humidity: Optional; Default : -1; Place's humidity
            :type humidity: int
            :param sunset: Optional; Default : -1; Place's sunset hour in UNIX Epoch format
            :type sunset: int
            :param sunrise: Optional; Default : -1; Place's sunrise hour in UNIX Epoch format
            :type sunrise: int
        """
        self.setPressure(pressure)
        self.setHumidity(humidity)
        self.setSunset(sunset)
        self.setSunrise(sunrise)

    def __str__(self) -> str:
        """
            Return the class as a string

            :rtype: str
        """
        return "Pressure : ["+str(self.getPressure())+"], Humidity : ["+str(self.getHumidity())+"], Sunrise : ["+str(self.getSunrise())+"], Sunset : ["+str(self.getSunset())+"]"

    def setPressure(self, pressure : int) -> None:
        """
            Pression setter

            :param pressure: Place's pressure
            :type pressure: int
        """
        self.__pressure = pressure

    def getPressure(self) -> int:
        """
            Pression getter

            :return: Place's pression
            :rtype: int
        """
        return self.__pressure

    def setHumidity(self, humidity : int) -> None:
        """
            Humidity's getter

            :param pressure: Place's humidity
            :type pressure: int
        """
        self.__humidity = humidity

    def getHumidity(self) -> int:
        """
            Humidity's getter

            :return: Place's humidity
            :rtype: int
        """
        return self.__humidity

    def setSunset(self, sunset : int = -1) -> None:
        """
            Sunset's setter
            
            :param sunset: Place's sunset hour in UNIX Epoch format
            :type sunset: int
        """
        self.__sunset = sunset

    def getSunset(self) -> int:
        """
            Sunset's getter
            
            :return: Place's sunset hour in UNIX Epoch format
            :rtype: int
        """
        return self.__sunset

    def setSunrise(self, sunrise : int = -1) -> None:
        """
            Sunset's setter
            
            :param sunrise: Place's sunrise hour in UNIX Epoch format
            :type sunrise: int
        """
        self.__sunrise = sunrise

    def getSunrise(self) -> int:
        """
            Sunset's getter
            
            :return: Place's sunrise hour in UNIX Epoch format
            :rtype: int
        """
        return self.__sunrise