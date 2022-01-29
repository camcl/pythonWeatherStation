class Temperature:
    """
        This class represents all data on temperature. All values are in Kelvin

        :author: Delmas Pierre <panda@delmasweb.net>
        :date: 23 Janvier 2022
        :version: 1.0
    """

    def __init__(self, current : float = -1, min : float = -1, max : float = -1, feelsLike : float = -1) -> None:
        """
            Constructor

            :param current: Optional; Default : -1; Current temperature
            :type current: float
            :param min: Optional; Default : -1; Minimal temperature
            :type min: float
            :param max: Optional; Default : -1; Maximal temperature
            :type max: float
            :param max: Optional; Default : -1; Feels like temperature
            :type max: float
        """
        self.setCurrent(current)
        self.setMin(min)
        self.setMax(max)
        self.setFeelsLike(feelsLike)

    def __str__(self) -> str:
        """
            Return the class as a string

            :rtype: str
        """
        return "Current : ["+str(self.getCurrent())+"], Min : ["+str(self.getMin())+"], Max : ["+str(self.getMax())+"], Feels like : ["+str(self.getFeelsLike())+"]"

    def setCurrent(self, current : float) -> None:
        """
            Current temperature setter

            :param current: Current temperature
            :type current: float
        """
        self.__current = current
    
    def getCurrent(self) -> float:
        """
            Current temperature getter

            :return: Current temperature
            :rtype: float
        """
        return self.__current

    def setMin(self, min : float) -> None:
        """
            Minimal temperature setter

            :param min: Minimal temperature
            :type min: float
        """
        self.__min = min
    
    def getMin(self) -> float:
        """
            Minimal temperature getter

            :return: Minimal temperature
            :rtype: float
        """
        return self.__min

    def setMax(self, max : float) -> None:
        """
            Maximal temperature setter

            :param max: Maximal temperature
            :type max: float
        """
        self.__max = max
    
    def getMax(self) -> float:
        """
            Maximal temperature getter

            :return: Maximal temperature
            :rtype: float
        """
        return self.__max

    def setFeelsLike(self, feelsLike : float) -> None:
        """
            Feels like temperature setter

            :param max: Feels like temperature
            :type max: float
        """
        self.__feelsLike = feelsLike
    
    def getFeelsLike(self) -> float:
        """
            Feels like temperature getter

            :return: Feels like temperature
            :rtype: float
        """
        return self.__feelsLike

    def fromKelvinToCelsius(value : float) -> float:
        """
            This function convert a temperature from Kelvin to celsius

            :param value: The value to convert
            :type value: float
            :return: The converted value
            :rtype: float
            :meta static:
        """
        return value-273.15

    def fromCelsiusToKelvin(value : float) -> float:
        """
            This function convert a temperature from Celsius to Kelvin

            :param value: The value to convert
            :type value: float
            :return: The converted value
            :rtype: float
            :meta static:
        """
        return value + 273.15

    def fromCelsiusToFahrenheit(value : float) -> float:
        """
            This function convert a temperature from Celsius to Fahrenheit

            :param value: The value to convert
            :type value: float
            :return: The converted value
            :rtype: float
            :meta static:
        """
        return value * 1.8 + 32

    def fromFahrenheitToCelsius(value : float) -> float:
        """
            This function convert a temperature from Fahrenheit to Celsius

            :param value: The value to convert
            :type value: float
            :return: The converted value
            :rtype: float
            :meta static:
        """
        return (value - 32)/1.8

    def fromFahrenheitToKelvin(value : float) -> float:
        """
            This function convert a temperature from Fahrenheit to Kelvin

            :param value: The value to convert
            :type value: float
            :return: The converted value
            :rtype: float
            :meta static:
        """
        return Temperature.fromCelsiusToKelvin(Temperature.fromFahrenheitToCelsius(value))

    def fromKelvinToFahrenheit(value : float) -> float:
        """
            This function convert a temperature from Kelvin to Fahrenheit

            :param value: The value to convert
            :type value: float
            :return: The converted value
            :rtype: float
            :meta static:
        """
        return Temperature.fromCelsiusToFahrenheit(Temperature.fromKelvinToCelsius(value))