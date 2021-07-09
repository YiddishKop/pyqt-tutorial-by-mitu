# 课程来源

https://www.youtube.com/watch?v=ta73dduP4Uk&list=PLLPsLcbaFY21h8bnBBig8Y0YgOdGpzIjm&index=124

lecture 10 ~ 16

# QtDesigner 四种布局之： 水平布局

QtDesigner 中有4个种布局：水平布局、垂直布局、网格布局、表单布局

### 先由控件，后设布局

框选多个 -> 右键 -> 布局 -> 水平布局  ===  整体居中，横向等宽

### 先有布局，后设控件

添加水平布局 -> 拖动控件置于其中 ===  同上

# QtDesigner 四种布局之： 栅格布局

栅格布局 = 二维表格布局

### 界面 python 文件中 addWidget 参数解析
`self.gridLayout_2.addWidget(self.pushButton_15, 3, 2, 1, 1)`

`3, 2, 1, 1`

前面两个参数，表示：处在几行和几列，这里是处在 3 行 2 列，（注意是从0开始计数）

最后两个参数，表示：占用几行和几列，这里是占用 1 行 1 列

# QtDesigner 四种布局之： 同时使用水平和垂直布局

遇到比较复杂的布局，可以选取比较小的 *分组*，先将其设定为垂直 or 水平布局。

然后再对包含这些 *分组* 的整体，进行水平 or 垂直布局