import sys
from PyQt5.QtWidgets import QApplication, QWidget

'''
每一个 pyqt 程序都需要从
创建 qapplication 、 qwidget 对象开始
亦即 应用程序和窗口
基本窗口操作包括： reszie, move, setwindowtitle, show
他们都是 qwidget 的方法

每一个 pyqt 程序都是从 exec_ 方法结束
生成界面的右上角 'X' 按钮会自动调用 sys.exit()
其中可以置入 qapplication 的 exec_() 方法作为 handler
'''

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