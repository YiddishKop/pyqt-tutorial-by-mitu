# pyqt 分离逻辑和界面代码

## 逻辑代码封装成类

之前的逻辑代码如下所示为 `脚本方式`， 如果用 `面向对象的方式`. 应该
将其封装成类，方便代码复用和管理。

``` python
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
```

可以改写为如下方式，两者是等价的，面向对象的方式更清晰：

```python
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
        4. Ui_MainWindow 为 ui 生成的 py 文件主类
    '''
    # parent=None 保证了该窗体是最顶层窗体
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # ... TODO
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()   # 构建对象初始化时，会自动执行 setupUi
    mainWindow.show()
    sys.exit(app.exec_())
```


## 逻辑代码中为何指定 parent=None
Pyqt 中 `__init__(self, parent=None)` 中的参数 `parent` 的理解


在PyQt中，所有 class 都是从 `QObject` 派生而来，`QWidget` 对象就可以有一个parent。
这种 parent-child 关系主要用于两个方面：

> *没有 parent 的 QWidget 类被认为是最上层的窗体（通常是MainWindow）* 

1. 由于 MainWindow 的一些操作生成的新窗体对象，parent 都应该指向 MainWindow;
2. 由于 parent-child 关系的存在，它保证了child 窗体在主窗体被回收之时也被回收.

parent 作为构造函数的最后一个参数被传入，但通常情况下不必显示去指定 parent 对象。因为当调用局管理器时，部局管理器会自动处理这种 parent-child 关系。但是在一些特殊的情况下，我们必须显示的指定 parent-child 关系。 如当生成的子类不是 `QWidget` 对象但继承了 `QObject` 对象，用作 dock widgets 的 `QWidget` 对象。

我们可以看到，对象之间有了依赖和生命周期，把IOC容器运用到GUI编程中是自然而然的事情了。
