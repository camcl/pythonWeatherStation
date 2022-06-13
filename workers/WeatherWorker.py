from typing import Any
from time import sleep
from PyQt6.QtCore import QObject, pyqtSignal

from classes.httpRequest.DataRequest import DataRequest
from classes.element.position import Position
from classes.element.temperature import Temperature
from classes.element.wind import Wind
from classes.element.weather import Weather
from classes.element.miscellaneous import Miscellaneaous

class WeatherWorker(QObject):
    """
        Weather worker

        :author: Panda <panda@delmasweb.net>
        :date: January 15, 2022
        :version: 1.0
    """

    """
        pyqtSignal to be send when the worker is over
    """
    finished = pyqtSignal()

    """
        pyqtSignal to be send while the worker has a new value to send
    """
    progress = pyqtSignal(Weather)

    """
        API Key
    """
    __apiKey = ""

    """
        Current position
    """
    __currentPosition = None

    """
        To read or not to read weather that is the question ?
    """
    __hasToReadWeather = True

    """
        Sleep time for the weather loop in seconds
    """
    __delayTime = 60

    def __requestWeather(self, pos : Position) -> Any:
        """
            This function make the OpenWeatherAPI request

            :param pos: The position for which the request is made
            :type pos: position
        """
        rObject = DataRequest(self.__apiKey)
        try:
            result = rObject.makeRequest(uri="https://api.openweathermap.org", url="data/2.5/weather", getParams="id="+str(pos.getId()))

            weatherData = Weather(
                wind=Wind(speed=result['wind']['speed'], direction=result['wind']['deg']), 
                position=pos, 
                temperature=Temperature(current=result['main']['temp'], min=result['main']['temp_min'], max=result['main']['temp_max'], feelsLike=result['main']['feels_like']),
                misc=Miscellaneaous(pressure=result['main']['pressure'], humidity=result['main']['humidity'], sunset=result['sys']['sunset'], sunrise=result['sys']['sunrise']))

            return weatherData
        except:
            return None

    def setApiKey(self, apiKey : str) -> None:
        """
            API Key setter

            :param apiKey: API Key
            :type apiKey: str
        """
        self.__apiKey = apiKey

    def setHasToReadWeather(self, hasToReadWeather : bool) -> None:
        """
        hasToReadWeather setter

        :param hasToReadWeather: The new value
        :type hasToReadWeather: bool
        """
        self.__hasToReadWeather = hasToReadWeather
    
    def setCurrentPosition(self, position : Position) -> None:
        """
        Current position setter

        :param position: The new value for the current position
        :type position: Position
        """
        self.__currentPosition = position

    def setDelayTime(self, delayTime : int) -> None:
        """
            Delay Time setter

            :param delayTime: The new value
            :type delayTime: int
        """
        self.__delayTime = delayTime

    def run(self):
        """
            Worker main loop
        """
        # If we ask to stop reading we have to change value of hasToReadWeather to false
        while self.__hasToReadWeather:
            if(self.__currentPosition != None):
                weatherData = self.__requestWeather(self.__currentPosition)
                if(weatherData != None):
                    self.progress.emit(weatherData)
            sleep(int(self.__delayTime))
        self.finished.emit()