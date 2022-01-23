import os
import sys
from time import sleep

from typing import Any
from dotenv import load_dotenv

from classes.httpRequest.dataRequest import dataRequest as request
from classes.element.position import Position as position
from classes.element.temperature import Temperature as temp
from classes.element.wind import Wind as wind
from classes.element.weather import Weather as weather

from views.mainFrame import MainFrame as App

from PyQt5.QtWidgets import QApplication, QListWidget, QMessageBox

load_dotenv()

pos=position(name="Nantes", country="FR", id=2990969, longitude=-1.5534, latitude=47.2173)


class myListWidget(QListWidget):

   def Clicked(self,item):
      QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())

def requestWeather() -> Any:
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

def main() -> None:
    if __name__=='__main__':
        app=QApplication(sys.argv)

        ex=App()
        ex.printListOfCities(os.getenv("CITY_FILE"))
        ex.show()

        sys.exit(app.exec_())

main()