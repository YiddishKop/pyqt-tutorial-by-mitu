# tutorial - 3: QtDesigner 设计UI界面

`ctrl + r` 用来实现UI界面快速预览


### signal and slot
当你需要实现类似鼠标点击事件，就需要用到 signal and slot (信号和槽) 的概念：
1. 这个功能通过菜单栏  edit -> signal slot 打开
2. 鼠标移到某个控件，`拖拽`到空白处
3. 在弹出的框中【左侧】选择要实现的事件，【右侧】是该事件执行的方法，如果没有自己新建一个即可（UI界面下无要求实现）

### pyuic : UI --> python 
1. pyuic 能把 UI 文件转换成 python 代码文件，方便逻辑代码进行调用

2. 默认情况会把 ui 文件转为同名的 py 文件，其中定义了类名为 `Ui_MainWindow` 的类

3. 在逻辑 python 文件中创建 2 个对象：
   1.  `Ui_MainWindow` 对象
   2.  `QMainWindow` 对象
   3.  通过 `setupUi` 方法连接两者

4. 实现事件响应函数
   1. 本节课程序是将 `self.pushButton.clicked.connect(MainWindow.button_click)` 改成了 `self.pushButton.clicked.connect(self.button_click)`
   2. `MainWindow` 换成 `self` 是把事件响应函数直接放在界面 python 文件中了