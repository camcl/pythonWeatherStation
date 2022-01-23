from PyQt5.QtWidgets import QMainWindow

class MainFrame(QMainWindow):

    """
        Classe de la fenetre principale

        :author: Delmas Pierre <panda@delmasweb.net>
        :date: 30 Août 2021
        :version: 0.3
    """

    def __init__(self, appName : str = "My Weather App", borderLess : bool = False, width: int = 1000, height: int = 1000):
        super().__init__()
        self.title=appName
        self.left=10
        self.top=10
        self.width=width
        self.height=height
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()