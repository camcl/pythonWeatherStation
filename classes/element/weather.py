from classes.element import wind, position, temperature

class Weather:

    """
    Cette classe represente la meteo du lieu que l'on monitore

    :author: Delmas Pierre <panda@delmasweb.net>
    :date: 23 Janvier 2022
    :version: 0.1
    """
    def __init__(self, wind : wind.Wind = None, position : position.Position = None, temperature : temperature.Temperature = None, pressure : int = -1, humidity : int = -1) -> None:

        """
        Constructeur

        :param wind: Le vent du lieu
        :type wind: wind.Wind
        :param position: La position du lieu
        :type position: position.Position
        :param temperature: La temperature du lieu
        :type temperature: temperature.Temperature
        :param pressure: La pression
        :type pressure: int
        :param humidity: L'humidite du lieu
        :type humidity: int
        """
        self.setWind(wind)
        self.setPosition(position)
        self.setTemperature(temperature)
        self.setPressure(pressure)
        self.setHumidity(humidity)
    
    def __str__(self) -> str:
        """
        Retourne la classe sous la forme d'une chaine de caractere

        :rtype: str
        """
        return "Wind : ["+str(self.getWind())+"], Position : ["+str(self.getPosition())+"], Temperature : ["+str(self.getTemperature())+"], Pressure : ["+str(self.getPressure())+"], Humidity : ["+str(self.getHumidity())+"]"

    def setWind(self, wind : wind.Wind) -> None:
        """
        Setter du vent

        :param wind: Le vent du lieu
        :type wind: wind.Wind
        """
        self.__wind = wind

    def getWind(self) -> wind.Wind:
        """
        Getter du vent

        :return: Le vent du lieu
        :rtype: wind.Wind
        """
        return self.__wind

    def setPosition(self, position : position.Position) -> None:
        """
        Setter du vent

        :param position: Le vent du lieu
        :type position: position.Position
        """
        self.__position = position

    def getPosition(self) -> position.Position:
        """
        Getter de la position

        :return: Le position du lieu
        :rtype: position.Position
        """
        return self.__position

    def setTemperature(self, temperature : temperature.Temperature) -> None:
        """
        Setter de la temperature

        :param temperature: La temperature du lieu
        :type temperature: temperature.Temperature
        """
        self.__temperature = temperature

    def getTemperature(self) -> temperature.Temperature:
        """
        Getter de la temperature

        :return: La temperature du lieu
        :rtype: temperature.Temperature
        """
        return self.__temperature
    
    def setPressure(self, pressure : int) -> None:
        """
        Setter de la pression

        :param pressure: La pression du lieu
        :type pressure: int
        """
        self.__pressure = pressure

    def getPressure(self) -> int:
        """
        Getter de la pression

        :return: La pression du lieu
        :rtype: int
        """
        return self.__pressure

    def setHumidity(self, humidity : int) -> None:
        """
        Setter de l'humidite

        :param pressure: L'humidite
        :type pressure: int
        """
        self.__humidity = humidity

    def getHumidity(self) -> int:
        """
        Getter de l'humidite

        :return: L'humidite
        :rtype: int
        """
        return self.__humidity

    
