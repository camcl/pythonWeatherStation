from PyQt5.QtWidgets import QWidget, QMainWindow

from views.MainGrid import MainGrid

class MainFrame(QMainWindow):

    """
        Grille principale
    """
    __mainGrid = None

    def __init__(self, parent: QWidget = None, appName : str = "My Weather App", borderLess : bool = False, width: int = 1000, height: int = 1000) -> None:
        super().__init__(parent)
        self.__title=appName
        self.__left=10
        self.__top=10
        self.__width=width
        self.__height=height
        self.__initUI()

    def __initUI(self) -> None:
        """
            Initialise l'UI
        """        
        self.__mainGrid = MainGrid()
        self.layout().addChildLayout(self.__mainGrid)
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setWindowTitle(self.__title)
        self.show()

    def getMainGrid(self) -> MainGrid:
        """
            Renvoi la grille principale
        """
        return self.__mainGrid