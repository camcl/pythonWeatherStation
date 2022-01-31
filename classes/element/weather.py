from classes.element.Wind import Wind
from classes.element.Position import Position
from classes.element.Temperature import Temperature

class Weather:
    """
        This class represents a weather (wind, position, temperature, pressure, ...)

        :author: Panda <panda@delmasweb.net>
        :date: 23 Janvier 2022
        :version: 1.0
    """
    def __init__(self, wind : Wind = None, position : Position = None, temperature : Temperature = None) -> None:

        """
            Constructor

            :param wind: Optional; Default : None; Place's Wind
            :type wind: Wind
            :param position: Optional; Default : None; Position 
            :type position: Position
            :param temperature: Optional; Default : None; Place's temperature
            :type temperature: Temperature
        """
        self.setWind(wind)
        self.setPosition(position)
        self.setTemperature(temperature)
    
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
