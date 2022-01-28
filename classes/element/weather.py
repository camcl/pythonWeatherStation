from classes.element.Wind import Wind
from classes.element.Position import Position
from classes.element.Temperature import Temperature

class Weather:
    """
        This class represents a weather (wind, position, temperature, pressure, ...)

        :author: Delmas Pierre <panda@delmasweb.net>
        :date: 23 Janvier 2022
        :version: 1.0
    """
    def __init__(self, wind : Wind = None, position : Position = None, temperature : Temperature = None, pressure : int = -1, humidity : int = -1) -> None:

        """
            Constructor

            :param wind: Optional; Default : None; Place's Wind
            :type wind: Wind
            :param position: Optional; Default : None; Position 
            :type position: Position
            :param temperature: Optional; Default : None; Place's temperature
            :type temperature: Temperature
            :param pressure: Optional; Default : -1; Place's pressure
            :type pressure: int
            :param humidity: Optional; Default : -1; Place's Humidity
            :type humidity: int
        """
        self.setWind(wind)
        self.setPosition(position)
        self.setTemperature(temperature)
        self.setPressure(pressure)
        self.setHumidity(humidity)
    
    def __str__(self) -> str:
        """
            Return the class as a string

            :rtype: str
        """
        return "Wind : ["+str(self.getWind())+"], Position : ["+str(self.getPosition())+"], Temperature : ["+str(self.getTemperature())+"], Pressure : ["+str(self.getPressure())+"], Humidity : ["+str(self.getHumidity())+"]"

    def setWind(self, wind : Wind) -> None:
        """
            Wind's setter

            :param wind: Place's wind
            :type wind: Wind
        """
        self.__wind = wind

    def getWind(self) -> Wind:
        """
            Wind's getter

            :return: Place's wind
            :rtype: Wind
        """
        return self.__wind

    def setPosition(self, position : Position) -> None:
        """
            Place's position

            :param position: Place's position
            :type position: Position
        """
        self.__position = position

    def getPosition(self) -> Position:
        """
            Position's getter

            :return: Place's position
            :rtype: Position
        """
        return self.__position

    def setTemperature(self, temperature : Temperature) -> None:
        """
            Temperature's getter

            :param temperature: Place's temperature
            :type temperature: Temperature
        """
        self.__temperature = temperature

    def getTemperature(self) -> Temperature:
        """
            Temperature's getter

            :return: Place's temperature
            :rtype: Temperature
        """
        return self.__temperature
    
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

    
