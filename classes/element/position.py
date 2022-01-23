class Position:
    """
    Cette classe represente la position geographique du lieu que l'on monitore

    :author: Delmas Pierre <panda@delmasweb.net>
    :date: 23 Janvier 2022
    :version: 0.1
    """

    def __init__(self, name : str, country : str, id : int, longitude : float, latitude : float):
        """
        Constructeur

        :param name: Le nom de la ville
        :type name: str
        :param country: Le code du pays sur deux lettres au format ISO 3166
        :type country: str
        :param id: L'id de la ville dans OpenWeatherAPI
        :type id: int
        :param longitude: La longitude de la ville
        :type longitude: float
        :param latitude: La latitude de la ville
        :param latitude: float
        """
        self.__setName(name)
        self.__setCountry(country)
        self.__setId(id)
        self.__setLongitude(longitude)
        self.__setLatitude(latitude)

    def __str__(self) -> str:
        """
        Retourne la classe sous la forme d'une chaine de caractere

        :rtype: str
        """
        return "Name : ["+self.getName()+"], Country : ["+self.getCountry()+"], Id : ["+str(self.getId())+"], Longitude : ["+str(self.getLongitude())+"], Latitude : ["+str(self.getLatitude())+"]"

    def __setName(self, name : str):
        """
        Setter du nom

        :param name: Le nom de la ville
        :type name: str
        """
        self.__name = name

    def __setCountry(self, country : str):
        """
        Setter du country

        :param country: Le code du pays sur deux lettres au format ISO 3166
        :type country: str
        """
        self.__country = country

    def __setId(self, id : int):
        """
        Setter de l'identifiant du pays

        :param country: L'id de la ville dans OpenWeatherAPI
        :type country: int
        """
        self.__id = id

    def __setLongitude(self, longitude : float):
        """
        Setter de la longitude

        :param longitude: La longitude de la ville
        :type longitude: float
        """
        self.__longitude = longitude

    def __setLatitude(self, latitude : float):
        """
        Setter de la latitude

        :param latitude: La latitude de la ville
        :param latitude: float
        """
        self.__latitude = latitude

    def getName(self) -> str:
        """
        Getter du nom

        :return: Le nom de la ville
        :rtype: str
        """
        return self.__name

    def getCountry(self) -> str:
        """
        Getter du country

        :return: Le code du pays sur deux lettres au format ISO 3166
        :rtype: str
        """
        return self.__country

    def getId(self) -> int:
        """
        Getter de l'identifiant du pays

        :return: L'id de la ville dans OpenWeatherAPI
        :rtype: int
        """
        return self.__id

    def getLongitude(self) -> float:
        """
        Getter de la longitude

        :return: La longitude de la ville
        :rtype: float
        """
        return self.__longitude

    def getLatitude(self) -> float:
        """
        Getter de la latitude

        :return: La latitude de la ville
        :rtype: float
        """
        return self.__latitude
