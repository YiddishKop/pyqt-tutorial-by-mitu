# 进行拖拽文件实验

之前一直想知道如何实现 '多个文件拖拽到窗口，获取文件地址' 怎么做。

通过这个例子就基本了解清楚了。往窗口拖拽的文件，都属于 pyqt 的 `mimeData` 类型，

该类型有一些内嵌的函数，可以用来获取路径:
1. `QDropEvent.mimeData().urls()`   --> 获取多个拖拽文件地址
2. `QDropEvent.mimeData().text()`   --> 获取单个拖拽文件地址

可以参考官方文档，更详细了解两个函数：

https://doc.qt.io/qt-5/qmimedata.html#urls


## drag and drop 动作包含4个事件
1. dragEnterEvent   拖拽文件进入 qt 窗口
2. dragMoveEvent    拖拽文件在 qt 窗口内移动
3. dragLeaveEvent   拖拽文件移出 qt 窗口
4. dropEvent        拖拽文件释放进 qt 窗口

要获取文件地址，只需要在 dropEvent 进行

## urls() vs. text()

`QDropEvent.mimeData().urls()` 返回的是数组，每一个元素都是 QUrl 对象，
里面存放了所有被拖拽的文件的地址，形如：

```python
[PyQt5.QtCore.QUrl('file:///C:/Users/Administrator/Desktop/xxx - 副本.txt'), 
 PyQt5.QtCore.QUrl('file:///C:/Users/Administrator/Desktop/xxx - 副本 (2).txt'), 
 PyQt5.QtCore.QUrl('file:///C:/Users/Administrator/Desktop/xxx - 副本 (3).txt')]
```

想要拿到里面的地址，需要进行字符串化和正则匹配


`QDropEvent.mimeData().text()` 返回的是字符串，该方法仅支持单个文件的拖放，形如：
`"file:///C:/Users/Administrator/Desktop/xxx - 副本.txt"`

只需要进行简单的字符串