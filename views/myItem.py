from PyQt5.QtWidgets import QListWidgetItem

import classes.element.position as position

class MyItem(QListWidgetItem):
    """
        Classe qui un element de liste

        :author: Delmas Pierre <panda@delmasweb.net>
        :date: 30 Août 2021
        :version: 0.3
    """

    def __init__(self, position : position.Position, isChoosen : bool) -> None:
        """
            Constructeur

            :param position: Position de la ville
            :type position: position.Position
            :param isChoosen: Si la position est celle choisie
            :type isChoosen: bool
        """
        super().__init__()
        self.__position = position
        self.__isChoosen = isChoosen
        self.setText(self.__str__())

    def __str__(self) -> str:
        return self.__position.getName()+", "+self.__position.getCountry()

    def getPosition(self) -> position.Position:
        """
            Retourne la position

            :return: Position
            :rtype: position.Position
        """
        return self.__position
    
    def isChoosen(self) -> bool:
        """
        Retourne si la ville est choisie ou non

        :return: isChoosen
        :rtype: bool
        """
        return self.__isChoosen
    
    def setIsChoosen(self, isChoosen : bool) -> None:
        """
        Setter de isChoosen
        
        :param isChoosen: isChoosen
        :type isChoosen: bool
        """
        self.__isChoosen = isChoosen