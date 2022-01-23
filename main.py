import os

from typing import Any
from dotenv import load_dotenv

from classes.httpRequest.dataRequest import dataRequest as request
from classes.element.position import Position as position
from classes.element.temperature import Temperature as temp
from classes.element.wind import Wind as wind
from classes.element.weather import Weather as weather

load_dotenv()

pos=position(name="Nantes", country="FR", id=2990969, longitude=-1.5534, latitude=47.2173)

def requestWeather() -> Any:
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
        print(requestWeather())

main()