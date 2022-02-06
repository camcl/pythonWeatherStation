# Python Weather Station

This project contains a weather station in Python. This weather station uses the OpenWeatherAPI, so it needs an Internet connection and an active OpenWeather Account with an API key (see : https://openweathermap.org/api). 

**Note : A free account is enough for the usage of this application.**

## Installation
To install this application you will need to download the source code and have Python3 (>3.6) installed on the local machine you use it

Then you will need to install the required packages via Pip :

`pip install -r requirements.txt`

Then you will need to create an empty logs folder (for the logs of the application) and a conf directory containing two files :

### First file

The first one has to be called settings.ini and contains the following to start 

```
[weather]
tempunit = c
delay = 1

[time]
timezone = Etc/UTC

[cities]
filename = ./resources/filtered.list.json
choosen = 2981280

[language]
folder = ./resources/translation
locale = en
```

You can modify the logging level with :

- 10 : DEBUG
- 20 : INFO
- 30 : WARNING
- 40 : ERROR
- 50 : CRITICAL

The delay is in seconds for the fetch of the API

The timezone is a compatible version of pytz timezone (https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568)

### Second file

The second file has to be called .env and contains only the following

```
API_KEY=<your very secret API key>
```

## Launching

To run the application you only need to run the file called `main.py`

## Tests

Tests can be run from tests folder