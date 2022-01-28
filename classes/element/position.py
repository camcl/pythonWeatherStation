class Position:
    """
        This class represents a geographical position

        :author: Delmas Pierre <panda@delmasweb.net>
        :date: January 15, 2022
        :version: 1.0
    """

    def __init__(self, name : str, country : str, id : int, longitude : float, latitude : float):
        """
            Constructor

            :param name: City's name
            :type name: str
            :param country: Country code on two letters as specified by ISO 3166
            :type country: str
            :param id: City's id in OpenWeatherAPI
            :type id: int
            :param longitude: City's Longitude
            :type longitude: float
            :param latitude: City's Latitude
            :param latitude: float
        """
        self.__setName(name)
        self.__setCountry(country)
        self.__setId(id)
        self.__setLongitude(longitude)
        self.__setLatitude(latitude)

    def __str__(self) -> str:
        """
            Returns values as a string

            :rtype: str
        """
        return "Name : ["+self.getName()+"], Country : ["+self.getCountry()+"], Id : ["+str(self.getId())+"], Longitude : ["+str(self.getLongitude())+"], Latitude : ["+str(self.getLatitude())+"]"

    def __setName(self, name : str):
        """
            City's name setter

            :param name: City's name
            :type name: str
        """
        self.__name = name

    def __setCountry(self, country : str):
        """
            Country's code setter

            :param country: Country's code on two letter as specified by ISO3166
            :type country: str
        """
        self.__country = country

    def __setId(self, id : int):
        """
            City's id setter

            :param country: City's id in OpenWeatherAPI
            :type country: int
        """
        self.__id = id

    def __setLongitude(self, longitude : float):
        """
            Longitude's setter

            :param longitude: City's longitude setter
            :type longitude: float
        """
        self.__longitude = longitude

    def __setLatitude(self, latitude : float):
        """
            Latitude's setter

            :param latitude: City's latitude
            :type latitude: float
        """
        self.__latitude = latitude

    def getName(self) -> str:
        """
            City's name getter

            :return: City's name
            :rtype: str
        """
        return self.__name

    def getCountry(self) -> str:
        """
        Country's code setter

        :return: Country's code on two letters as specified in ISO3166
        :rtype: str
        """
        return self.__country

    def getId(self) -> int:
        """
            City's id getter

            :return: The id of the city in OpenWeatherAPI
            :rtype: int
        """
        return self.__id

    def getLongitude(self) -> float:
        """
            Longitude's getter

            :return: City's longtiude
            :rtype: float
        """
        return self.__longitude

    def getLatitude(self) -> float:
        """
            Latitude's getter

            :return: City's latitude
            :rtype: float
        """
        return self.__latitude
