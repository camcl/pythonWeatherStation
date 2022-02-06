from classes.element.Wind import Wind
from classes.element.Position import Position
from classes.element.Temperature import Temperature
from classes.element.Miscellaneous import Miscellaneaous

class Weather:
    """
        This class represents a weather (wind, position, temperature, pressure, ...)

        :author: Panda <panda@delmasweb.net>
        :date: 23 Janvier 2022
        :version: 1.0
    """
    def __init__(self, wind : Wind = None, position : Position = None, temperature : Temperature = None, misc : Miscellaneaous = None) -> None:

        """
            Constructor

            :param wind: Optional; Default : None; Place's Wind
            :type wind: Wind
            :param position: Optional; Default : None; Position 
            :type position: Position
            :param temperature: Optional; Default : None; Place's temperature
            :type temperature: Temperature
            :param misc: Optional; Default : None; Place's misc data
            :type misc: Miscellaneaous
        """
        self.setWind(wind)
        self.setPosition(position)
        self.setTemperature(temperature)
        self.setMisc(misc)
    
    def __str__(self) -> str:
        """
            Return the class as a string

            :rtype: str
        """
        return "Wind : ["+str(self.getWind())+"], Position : ["+str(self.getPosition())+"], Temperature : ["+str(self.getTemperature())+"], Misc : ["+str(self.getMisc())+"]"

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

    def setMisc(self, misc : Miscellaneaous) -> None:
        """
            Misc's setter

            :param misc: Place's misc data
            :type misc: Miscellaneaous
        """
        self.__misc = misc

    def getMisc(self) -> Miscellaneaous:
        """
            Misc's setter

            :return: Place's misc data
            :rtype: Miscellaneaous
        """
        return self.__misc
