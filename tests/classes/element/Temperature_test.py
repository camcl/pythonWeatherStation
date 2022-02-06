import unittest
from classes.element.Temperature import Temperature

class TestTemperature(unittest.TestCase):
    """
        This class is a test for the Temperature element

        :author: Panda <panda@delmasweb.net>
        :date: January 31, 2022
        :version: 1.0
    """

    def setUp(self):
        """
            Setup
        """
        super().setUp()
        self.temp = Temperature()

    def testCurrent(self):
        """
            Test getter and setter for current
        """
        self.temp.setCurrent(10)
        self.assertEquals(self.temp.getCurrent(), 10)

    def testFeelsLike(self):
        """
            Test getter and setter for feels like
        """
        self.temp.setFeelsLike(10)
        self.assertEquals(self.temp.getFeelsLike(), 10)

    def testMax(self):
        """
            Test getter and setter for max
        """
        self.temp.setMax(10)
        self.assertEquals(self.temp.getMax(), 10)

    def testMin(self):
        """
            Test getter and setter for current
        """
        self.temp.setMin(10)
        self.assertEquals(self.temp.getMin(), 10)

    def testToString(self):
        """
            Test to string for temperature
        """
        self.assertEquals(self.temp.__str__(), "Current : [-1], Min : [-1], Max : [-1], Feels like : [-1]")

    def testKelvinToCelsius(self):
        """
            Test the conversion from Celsius to Kelvin
        """
        self.assertEquals(Temperature.fromKelvinToCelsius(10), -263.15)

    def testCelsiusToKelvin(self):
        """
            Test the conversion from Celsius to Kelvin
        """
        self.assertEquals(Temperature.fromCelsiusToKelvin(100), 373.15)

    def testCelsiusToFahrenheit(self):
        """
            Test the conversion from Celsius To Fahrenheit
        """
        self.assertEquals(Temperature.fromCelsiusToFahrenheit(10), 50.0)

    def testFahrenheitToCelsius(self):
        """
            Test the conversion from Fahrenheit To Celsius
        """
        self.assertEquals(Temperature.fromFahrenheitToCelsius(10), -12.22)

    def testKelvinToFahrenheit(self):
        """
            Test the conversion from Kelvin To Fahrenheit
        """
        self.assertEquals(Temperature.fromKelvinToFahrenheit(10), -441.67)

    def testFahrenheitToKelvin(self):
        """
            Test the conversion from Fahrenheit To Kelvin
        """
        self.assertEquals(Temperature.fromFahrenheitToKelvin(10), 260.93)