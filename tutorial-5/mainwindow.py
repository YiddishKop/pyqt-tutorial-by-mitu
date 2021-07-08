from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow
from ui.Ui_windows import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    # parent=None 保证了该窗体是最顶层窗体
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # ... TODO