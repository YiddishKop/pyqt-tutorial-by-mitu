import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    # 定制大小
    w = QWidget()
    w.resize(400, 300)
    
    # 移动到对应的位置
    w.move(500, 250)
    
    # 设置窗口名称
    w.setWindowTitle('hello pyqt5')
    
    # 显示
    w.show()
    
    # 进入到事件循环
    sys.exit(app.exec_())