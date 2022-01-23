from typing import Any
from classes.httpRequest.dataRequest import dataRequest as request
from classes.element.position import Position as position
from classes.element.temperature import Temperature as temp
from classes.element.wind import Wind as wind
from classes.element.weather import Weather as weather

weatherData = weather(
    wind=wind(), 
    position=position(name="Nantes", country="FR", id=2990969, longitude=-1.5534, latitude=47.2173), 
    temperature=temp(), 
    pressure=0, 
    humidity=0)

def requestWeather() -> Any:
    rObject = request("605acfbb33d9e69764c03738c0b3fb49")
    try:
        result = rObject.makeRequest(uri="https://api.openweathermap.org", url="data/2.5/weather", getParams="id="+str(weatherData.getPosition().getId()))
        
        # On set le vent
        weatherData.getWind().setSpeed(result['wind']['speed'])
        weatherData.getWind().setDirection(result['wind']['deg']) 

        # On set la temperature
        weatherData.getTemperature().setCurrent(result['main']['temp'])
        weatherData.getTemperature().setMin(result['main']['temp_min'])
        weatherData.getTemperature().setMax(result['main']['temp_max'])
        weatherData.getTemperature().setFeelsLike(result['main']['feels_like'])

        # On set la pression
        weatherData.setPressure(result['main']['pressure'])

        # On set l'humidite
        weatherData.setHumidity(result['main']['humidity'])


        print(weatherData)
    except:
        print("Probleme sur la requete de meteo")

def main() -> None:
    if __name__=='__main__':
        print(requestWeather())

main()