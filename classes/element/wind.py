class Wind:
    """
        Classe permettant de symboliser le vent

        :author: Delmas Pierre <panda@delmasweb.net>
        :date: 23 Janvier 2022
        :version: 0.1
    """

    def __init__(self, speed : int = 0, direction : int = 0) -> None:
        """
        :param speed: La vitesse du vent
        :type speed: int
        :param direction: La direction du vent par rapport au nord
        :type direction: int
        """
        self.setSpeed(speed)
        self.setDirection(direction)
    
    def __str__(self) -> str:
        """
        Retourne la classe sous la forme d'une chaine de caractere

        :rtype: str
        """
        return "Speed : ["+str(self.getSpeed())+"], Direction : ["+str(self.getDirection())+"]"

    def setSpeed(self, speed : int) -> None:
        """
        Setter de la vitesse du vent

        :param speed: La vitesse du vent
        :type speed: int
        """
        self.__speed = speed

    def setDirection(self, direction : int) -> None:
        """
        Setter de la direction du vent

        :param direction: La direction du vent par rapport au nord
        :type direction: int
        """
        self.__direction = direction

    def getSpeed(self) -> int:
        """
        Retourne la vitesse du vent

        :return: La vitesse du vent
        :rtype: int
        """
        return self.__speed

    def getDirection(self) -> int:
        """
        Retourne la direction du vent

        :return: La direction du vent
        :rtype: int
        """
        return self.__direction