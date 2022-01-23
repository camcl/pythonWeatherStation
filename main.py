import os
import sys
import threading
import signal
from time import sleep

from typing import Any
from dotenv import load_dotenv

from classes.httpRequest.dataRequest import dataRequest as request
from classes.element.position import Position as position
from classes.element.temperature import Temperature as temp
from classes.element.wind import Wind as wind
from classes.element.weather import Weather as weather

from views.mainFrame import MainFrame as App

from PyQt5.QtWidgets import QApplication

load_dotenv()

hasToReadWeather = True

def requestWeather(pos : position) -> Any:
    print(os.getenv('API_KEY'))
    rObject = request(os.getenv('API_KEY'))
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
        print("Probleme sur la requete de meteo")

def weatherThread():
    while True:
        global hasToReadWeather
        if hasToReadWeather:
            pos = ex.getCurrentPosition()
            if(pos != None):
                weatherData = requestWeather(pos)
                print(weatherData)
            else:
                print("No position provided")
            sleep(1)
        else:
            break
    print("Weather thread stopped")

def main() -> None:
    if __name__=='__main__':
        ex.printListOfCities(os.getenv("CITY_FILE"))
        ex.show()
        sys.exit(app.exec_())

# Cette fonction gère l'appel à un signal d'arrêt
def cleanUp():
    global hasToReadWeather
    hasToReadWeather = False
    t1.join()
    print("")
    print("")
    print("Arrêt du programme comme demandé par le signal")
    
app=QApplication(sys.argv)
app.aboutToQuit.connect(cleanUp)

ex=App()

t1 = threading.Thread(target=weatherThread)
t1.start()

main()