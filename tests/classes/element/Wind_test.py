import unittest
from classes.element.Wind import Wind

class WindTest(unittest.TestCase):
    """
        This class is a test for the Wind element

        :author: Panda <panda@delmasweb.net>
        :date: January 31, 2022
        :version: 1.0
    """
    def setUp(self) -> None:
        """
            Setup
        """
        super().setUp()
        self.wind = Wind()

    def testSpeed(self):
        """
            This function test speed
        """
        self.wind.setSpeed(10)
        self.assertEquals(self.wind.getSpeed(), 10, "Should be 10")

    def testDirectionValueOk(self):
        """
            This function test direction
        """
        self.wind.setDirection(10)
        self.assertEquals(self.wind.getDirection(), 10, "Should be 10")

    def testDirectionValueUp360(self):
        """
            This function test direction if the value is up 360°, should return the value - 360
        """
        self.wind.setDirection(460)
        self.assertEquals(self.wind.getDirection(), 100, "Should be 100")

    def testDirectionValueDown0(self):
        """
            This function test direction if the value is below 360°, should return the value + 360
        """
        self.wind.setDirection(-50)
        self.assertEquals(self.wind.getDirection(), 310, "Should be 310")