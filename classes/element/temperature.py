class Temperature:
    """
    Cette classe represente la temperature du lieu. Toutes les informations fournies sont en degres Kelvin

    :author: Delmas Pierre <panda@delmasweb.net>
    :date: 23 Janvier 2022
    :version: 0.1
    """

    def __init__(self, current : float = -1, min : float = -1, max : float = -1, feelsLike : float = -1) -> None:
        """
        Constructeur

        :param current: La temperature courante
        :type current: float
        :param min: La temperature minimale
        :type min: float
        :param max: La temperature maximale
        :type max: float
        :param max: La temperature ressenti
        :type max: float
        """
        self.setCurrent(current)
        self.setMin(min)
        self.setMax(max)
        self.setFeelsLike(feelsLike)

    def __str__(self) -> str:
        """
        Retourne la classe sous la forme d'une chaine de caractere

        :rtype: str
        """
        return "Current : ["+str(self.getCurrent())+"], Min : ["+str(self.getMin())+"], Max : ["+str(self.getMax())+"], Feels like : ["+str(self.getFeelsLike())+"]"

    def setCurrent(self, current : float) -> None:
        """
        Setter de la temperature courante

        :param current: La temperature courante
        :type current: float
        """
        self.__current = current
    
    def getCurrent(self) -> float:
        """
        Getter de la temperature courante

        :return: La temperature courante
        :rtype: float
        """
        return self.__current

    def setMin(self, min : float) -> None:
        """
        Setter de la temperature minimale

        :param min: La temperature minimale
        :type min: float
        """
        self.__min = min
    
    def getMin(self) -> float:
        """
        Getter de la temperature minimale

        :return: La temperature minimale
        :rtype: float
        """
        return self.__min

    def setMax(self, max : float) -> None:
        """
        Setter de la temperature maximale

        :param max: La temperature maximale
        :type max: float
        """
        self.__max = max
    
    def getMax(self) -> float:
        """
        Getter de la temperature maximale

        :return: La temperature maximale
        :rtype: float
        """
        return self.__max

    def setFeelsLike(self, feelsLike : float) -> None:
        """
        Setter de la temperature ressenti

        :param max: La temperature ressenti
        :type max: float
        """
        self.__feelsLike = feelsLike
    
    def getFeelsLike(self) -> float:
        """
        Getter de la temperature ressenti

        :return: La temperature ressenti
        :rtype: float
        """
        return self.__feelsLike