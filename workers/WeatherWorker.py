from typing import Any
from time import sleep
from PyQt5.QtCore import QObject, pyqtSignal

from classes.httpRequest.dataRequest import dataRequest as request
from classes.element.position import Position as position
from classes.element.temperature import Temperature as temp
from classes.element.wind import Wind as wind
from classes.element.weather import Weather as weather

class WeatherWorker(QObject):

    """
        Signal de fin du worker
    """
    finished = pyqtSignal()

    """
        Signal de worker en cours
    """
    progress = pyqtSignal(weather)

    """
        Cle d'API
    """
    __apiKey = ""

    """
        Position courante
    """
    __currentPosition = None

    """
        Doit-on ou non lire la meteo tel est la question ?
    """
    __hasToReadWeather = True

    """
        Delai (en s) de la pause de lecture du worker
    """
    __delayTime = 60

    def __requestWeather(self, pos : position) -> Any:
        """
            Cette fonction fait la requete API REST a OpenWeatherMap

            :param pos: La position pour laquelle on fait la requete
            :type pos: position
        """
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
        """
            Setter de la cle d'API

            :param apiKey: La cle d'API
            :type apiKey: str
        """
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
        """
            Setter du delai de pause

            :param delayTime: Le delai (en secondes) de la pause
            :type delayTime: int
        """
        self.__delayTime = delayTime

    def run(self):
        """
            La fonction principale du worker
        """
        # On execute cette boucle en permanence. 
        # Si jamais on demande l'arret alors hasToReadWeather devra passer a false ce qui provoquera une sortie de la boucle
        while self.__hasToReadWeather:
            if(self.__currentPosition != None):
                weatherData = self.__requestWeather(self.__currentPosition)
                if(weatherData != None):
                    self.progress.emit(weatherData)
            sleep(int(self.__delayTime))
        self.finished.emit()