from PyQt5.QtWidgets import QListWidgetItem

from classes.element.Position import Position

class MyItem(QListWidgetItem):
    """
        Item of cities list

        :author: Panda <panda@delmasweb.net>
        :date: January 15, 2022
        :version: 1.0
    """

    def __init__(self, position : Position, isChoosen : bool) -> None:
        """
            Constructor

            :param position: Position de la ville
            :type position: Position
            :param isChoosen: If the position is the one currently clicked in the list
            :type isChoosen: bool
        """
        super().__init__()
        self.__position = position
        self.__isChoosen = isChoosen
        self.setText(self.__str__())

    def __str__(self) -> str:
        """
            Return the item in a string

            :return: The item as a string
            :rtype: str            
        """
        return self.__position.getName()+", "+self.__position.getCountry()

    def getPosition(self) -> Position:
        """
            Return the position

            :return: position
            :rtype: Position
        """
        return self.__position
    
    def isChoosen(self) -> bool:
        """
            Return if the item is the choosen one 

            :return: isChoosen
            :rtype: bool
        """
        return self.__isChoosen
    
    def setIsChoosen(self, isChoosen : bool) -> None:
        """
            isChoosen setter
            
            :param isChoosen: isChoosen
            :type isChoosen: bool
        """
        self.__isChoosen = isChoosen