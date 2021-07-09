from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui.Ui_windows import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    '''
    @summary:
        1. 该文件结构以类的形式出现（区别于 tutorial-4 中函数脚本的形式），
        可以更好的将 pyqt 的逻辑代码封装在一起。
        2. 初始化函数( __init__ )保证了在创建该类的对象的时候就会自动调用
        setupUi 函数
        3. parent=None 保证了该窗体是最顶层窗体（已经成为墨守成规的方式）
    '''
    # parent=None 保证了该窗体是最顶层窗体
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # ... TODO
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())