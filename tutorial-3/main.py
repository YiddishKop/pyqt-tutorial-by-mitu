from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from ui.windows import *
import sys


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    mainWindow = QMainWindow()
    
    ui = Ui_MainWindow()
    
    ui.setupUi(mainWindow)
    
    mainWindow.show()
    
    sys.exit(app.exec_())
    
    