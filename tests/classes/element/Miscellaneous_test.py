import unittest
from ddt import ddt, data
from classes.element.miscellaneous import Miscellaneaous

@ddt
class TestMiscellaneous(unittest.TestCase):

    """
        This class is a test for the Miscellaneous element

        :author: Panda <panda@delmasweb.net>
        :date: January 31, 2022
        :version: 1.0
    """
    def setUp(self):
        """
            Setup
        """
        super().setUp()
        self.misc = Miscellaneaous()

    def testPressure(self):
        """
            Test for set and get pressure
        """
        self.misc.setPressure(10)
        self.assertEquals(self.misc.getPressure(), 10, "Should be 10")

    def testHumidity(self):
        """
            Test for set and get humidity
        """
        self.misc.setHumidity(10)
        self.assertEquals(self.misc.getHumidity(), 10, "Should be 10")

    def testSunset(self):
        """
            Test for set and get sunset
        """
        self.misc.setSunset(10)
        self.assertEquals(self.misc.getSunset(), 10, "Should be 10")

    def testSunrise(self):
        """
            Test for set and get sunrise
        """
        self.misc.setSunrise(10)
        self.assertEquals(self.misc.getSunrise(), 10, "Should be 10")
    
    def testToString(self):
        """
            Test for string reduction of the Misc class
        """
        self.assertEquals(self.misc.__str__(), "Pressure : [-1], Humidity : [-1], Sunrise : [-1], Sunset : [-1]")

    @data(0, 45, 90, 135, 180, 225, 270, 315)
    def testConvertDirectionDegreesToString(self, value):
        """
            Test for conversion from degrees in direction to position on compass rose
        """
        result = Miscellaneaous.convertDirectionDegreesInDirectionString(value)
        if(value == 0):
            self.assertEquals(result, "n", "Should return n")
        elif(value == 45):
            self.assertEquals(result, "ne", "Should return ne")
        elif(value == 90):
            self.assertEquals(result, "e", "Should return e")
        elif(value == 135):
            self.assertEquals(result, "se", "Should return se")
        elif(value == 180):
            self.assertEquals(result, "s", "Should return s")
        elif(value == 225):
            self.assertEquals(result, "sw", "Should return sw")
        elif(value == 270):
            self.assertEquals(result, "w", "Should return w")
        elif(value == 315):
            self.assertEquals(result, "nw", "Should return nw")
        else:
            self.assertTrue(False)

    def testConvertSpeedFromMeterSecondsToKilometersHours(self):
        """
            This function test to convert in m/s to km/h
        """
        self.assertEquals(Miscellaneaous.convertSpeedFromMeterSecondsToKilometersHours(5), 18, "Should return 18")