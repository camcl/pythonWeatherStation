import logging

from typing import Any
from time import sleep
from PyQt5.QtCore import QObject, pyqtSignal
from views.mainFrame import MainFrame as App

from classes.httpRequest.dataRequest import dataRequest as request
from classes.element.position import Position as position
from classes.element.temperature import Temperature as temp
from classes.element.wind import Wind as wind
from classes.element.weather import Weather as weather


class WeatherWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(weather)
    __apiKey = ""
    __currentPosition = None
    __hasToReadWeather = True
    __delayTime = 60

    def __requestWeather(self, pos : position) -> Any:
        rObject = request(self.__apiKey)
        try:
            result = rObject.makeRequest(uri="https://api.openweathermap.org", url="data/2.5/weather", getParams="id="+str(pos.getId()))
            
            weatherData = weather(
                wind=wind(speed=result['wind']['speed'], direction=result['wind']['deg']), 
                position=pos, 
                temperature=temp(current=result['main']['temp'], min=result['main']['temp_min'], max=result['main']['temp_max'], feelsLike=result['main']['feels_like']), 
                pressure=result['main']['pressure'], 
                humidity=result['main']['humidity'])

            return weatherData
        except:
            print("Weather request problem")

    def setApiKey(self, apiKey : str) -> None:
        self.__apiKey = apiKey

    def setHasToReadWeather(self, hasToReadWeather : bool) -> None:
        """
        Setter de hasToReadWeather

        :param hasToReadWeather: La valeur
        :type hasToReadWeather: bool
        """
        self.__hasToReadWeather = hasToReadWeather
    
    def setCurrentPosition(self, position : position) -> None:
        """
        Setter de la position courante

        :param position: La position courante
        :type position: position
        """
        self.__currentPosition = position

    def setDelayTime(self, delayTime : int) -> None:
        self.__delayTime = delayTime

    def run(self):
        # On execute cette boucle en permanence. 
        # Si jamais on demande l'arret alors hasToReadWeather devra passer a false ce qui provoquera un break de la boucle et son arret
        while self.__hasToReadWeather:
            if(self.__currentPosition != None):
                weatherData = self.__requestWeather(self.__currentPosition)
                self.progress.emit(weatherData)
            sleep(int(self.__delayTime))

        self.finished.emit()