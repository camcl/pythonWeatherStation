from PyQt5.QtWidgets import QListWidget,QWidget


class CityList(QListWidget):
    """
        Classe qui gere l'affichage de la liste de la liste des villes

        :author: Delmas Pierre <panda@delmasweb.net>
        :date: 30 Août 2021
        :version: 0.3
    """

    def __init__(self, parent : QWidget = None, x : int = 100, y : int = 100, width : int = 400, height : int = 400) -> None:
        """
        Constructeur

        :param filePath: Le chemin de la liste des villes disponible
        :return filePath: str
        :param x: La position du coin en haut a gauche en x
        :type x: int
        :param y: La position du coin en haut a gauche en y
        :type y: int
        :param width: La largeur de la fenetre
        :type width: int
        :param height: La hauteur de la fenetre
        :type height: int
        """
        super().__init__(parent)
        self.__xPos = x
        self.__yPos = y
        self.__width = width
        self.__height = height
        self.resize(self.__width, self.__height)
        self.move(self.__xPos, self.__yPos)