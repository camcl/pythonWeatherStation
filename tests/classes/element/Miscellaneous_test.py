import unittest
from classes.element.Miscellaneous import Miscellaneaous

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
        self.assertEquals(self.misc.getPressure(), 10)

    def testHumidity(self):
        """
            Test for set and get humidity
        """
        self.misc.setHumidity(10)
        self.assertEquals(self.misc.getHumidity(), 10)

    def testSunset(self):
        """
            Test for set and get sunset
        """
        self.misc.setSunset(10)
        self.assertEquals(self.misc.getSunset(), 10)

    def testSunrise(self):
        """
            Test for set and get sunrise
        """
        self.misc.setSunrise(10)
        self.assertEquals(self.misc.getSunrise(), 10)
    
    def testToString(self):
        """
            Test for string reduction of the Misc class
        """
        self.assertEquals(self.misc.__str__(), "Pressure : [-1], Humidity : [-1], Sunrise : [-1], Sunset : [-1]")