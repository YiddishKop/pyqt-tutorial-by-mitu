# pyqt 定时器 QTimer


### 逻辑代码中为何指定 parent=None
Pyqt 中 `__init__(self, parent=None)` 中的参数 `parent` 的理解


在PyQt中，所有 class 都是从 `QObject` 派生而来，`QWidget` 对象就可以有一个parent。
这种 parent-child 关系主要用于两个方面：

> *没有 parent 的 QWidget 类被认为是最上层的窗体（通常是MainWindow）* 

1. 由于 MainWindow 的一些操作生成的新窗体对象，parent 都应该指向 MainWindow;
2. 由于 parent-child 关系的存在，它保证了child 窗体在主窗体被回收之时也被回收.

parent 作为构造函数的最后一个参数被传入，但通常情况下不必显示去指定 parent 对象。因为当调用局管理器时，部局管理器会自动处理这种 parent-child 关系。但是在一些特殊的情况下，我们必须显示的指定 parent-child 关系。 如当生成的子类不是 `QWidget` 对象但继承了 `QObject` 对象，用作 dock widgets 的 `QWidget` 对象。

我们可以看到，对象之间有了依赖和生命周期，把IOC容器运用到GUI编程中是自然而然的事情了。
