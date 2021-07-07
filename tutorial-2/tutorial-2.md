# tutorial - 2: 第一个 pyqt 程序

### 应用程序和窗口
程序：每一个 pyqt 程序都需要从创建 `qapplication` 开始

窗口：第二步就是创建图形窗口： 创建 `qwidget` 或者 `qmainwindow` 对象

### 窗口的基本操作
基本窗口操作包括： reszie, move, setwindowtitle, show
他们都是 qwidget 的方法

### 程序的退出
每一个 pyqt 程序都是从 exec_ 方法结束
生成界面的右上角 'X' 按钮会自动调用 sys.exit()
其中可以置入 qapplication 的 exec_() 方法作为 handler
