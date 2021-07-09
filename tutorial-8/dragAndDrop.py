import sys
from PyQt5.QtWidgets import QApplication, QTextBrowser


class Demo(QTextBrowser):                                           # 1
    '''
    之前一直想知道如何实现 '多个文件拖拽到窗口，获取文件地址' 怎么做。通过这个例子
    就基本了解清楚了。往窗口拖拽的文件，属于 pyqt 的 mimeData 类型，该类型有一些
    内嵌的函数，可以用来获取路径（QDropEvent.mimeData().urls() 或者 
    QDropEvent.mimeData().text()）。 
    
    drag and drop 动作包含4个事件：
    1. dragEnterEvent   拖拽文件进入 qt 窗口
    2. dragMoveEvent    拖拽文件在 qt 窗口内移动
    3. dragLeaveEvent   拖拽文件移出 qt 窗口
    4. dropEvent        拖拽文件释放进 qt 窗口
    
    要获取文件地址，只需要在 dropEvent 进行
    
    QDropEvent.mimeData().urls() 返回的是数组，每一个元素都是 QUrl 对象，形如：
    [PyQt5.QtCore.QUrl('file:///C:/Users/Administrator/Desktop/xxx - 副本.txt'), 
     PyQt5.QtCore.QUrl('file:///C:/Users/Administrator/Desktop/xxx - 副本 (2).txt'), 
     PyQt5.QtCore.QUrl('file:///C:/Users/Administrator/Desktop/xxx - 副本 (3).txt')]
    想要拿到里面的地址，需要进行字符串化和正则匹配
    
    
    QDropEvent.mimeData().text() 返回的是字符串，形如：
    "file:///C:/Users/Administrator/Desktop/xxx - 副本.txt"
    
    '''
    def __init__(self):
        super(Demo, self).__init__()
        self.setAcceptDrops(True)                                   # 2

    def dragEnterEvent(self, QDragEnterEvent):                      # 3
        print('Drag Enter')
        if QDragEnterEvent.mimeData().hasText():
            QDragEnterEvent.acceptProposedAction()

    def dragMoveEvent(self, QDragMoveEvent):                        # 4
        print('Drag Move')

    def dragLeaveEvent(self, QDragLeaveEvent):                      # 5
        print('Drag Leave')

    def dropEvent(self, QDropEvent):                                # 6
        print('Drag Drop')
        
        # 获取单个拖拽文件的路径，其格式为 'file:///c://test.txt' 的字符串
        # 这里可以根据不同平台，对路径进行处理以获得该文件的绝对路径。
        # MacOS
        # txt_path = QDropEvent.mimeData().text().replace('file:///', '/')

        # Linux
        # txt_path = QDropEvent.mimeData().text().replace('file:///', '/').strip()

        # Windows
        # txt_path = QDropEvent.mimeData().text().replace('file:///', '')
        
        
        txt_path = QDropEvent.mimeData().text()
        print(txt_path)
        
        # 检测是否能够获取被拖拽的文件的地址。
        hasUrls = QDropEvent.mimeData().hasUrls()
        urls = []
        if hasUrls:
            urls = QDropEvent.mimeData().urls()
            print(urls)
            
        for url in urls:
            print(url)
            str_url = str(url)
            print(type(str_url))
            print('====================================')
            import re
            p1 = re.compile(r'[(](.*?)[)]', re.S)  #最小匹配
            p2 = re.compile(r'[(](.*)[)]', re.S)   #贪婪匹配
            url_file = re.findall(p2, str_url)[0]
            print(url_file)
            url_path = url_file.replace('file:///', '')
            print(url_path)

            
        print(hasUrls)

        # with open(txt_path, 'r') as f:
        #    self.setText(f.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())