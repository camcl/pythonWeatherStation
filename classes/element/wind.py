class Wind:
    """
        This represent a wind (direction and speed)

        :author: Panda <panda@delmasweb.net>
        :date: 23 Janvier 2022
        :version: 1.0
    """

    def __init__(self, speed : float = 0, direction : int = 0) -> None:
        """
            Constructor
        
            :param speed: Optional; Default : 0; Wind's speed
            :type speed: float
            :param direction: Optional; Default : 0; Wind's direction in degrees relative to North (0 : North, 90 : East, 180 : South, 270 : West)
            :type direction: int
        """
        self.setSpeed(speed)
        self.setDirection(direction)
    
    def __str__(self) -> str:
        """
            Return the class as a string

            :rtype: str
        """
        return "Speed : ["+str(self.getSpeed())+"], Direction : ["+str(self.getDirection())+"]"

    def setSpeed(self, speed : float) -> None:
        """
            Wind's speed setter

            :param speed: Wind's speed
            :type speed: float
        """
        self.__speed = speed

    def setDirection(self, direction : int) -> None:
        """
            Wind's direction setter

            The direction is in the 0-360 scope so better be sure

            :param direction: Wind's direction
            :type direction: int
        """
        if(direction < 0):
            direction = direction + 360
        
        if(direction > 360):
            direction = direction - 360

        self.__direction = direction

    def getSpeed(self) -> float:
        """
            Wind's speed getter

            :return: Wind's speed
            :rtype: float
        """
        return self.__speed

    def getDirection(self) -> int:
        """
            Wind's direction getter

            :return: Wind's direction
            :rtype: int
        """
        return self.__direction