# 尺寸策略（sizePolicy）

尺寸策略：一个控件跟随环境（主窗口、容器、布局）的调整而调整自身尺寸的方式。

## 4个尺寸策略
尺寸策略是每个空间都具有的 _属性组_ ，其包含 4 个具体的 _属性_
1. 水平策略
2. 垂直策略
3. 水平伸展
4. 垂直伸展


## 水平、垂直策略属性值
水平、垂直策略属性，又包含 7 个可选的值：
1. fixed
2. minimum
3. maximum
4. prefered
5. minimumExpanding
6. expanding           <- 与水平、垂直伸展属性配合使用，调整控件在环境中的比例
7. ignored


## 水平、垂直伸展属性值
伸展属性主要是配合 Expanding 对环境内的控件，进行比例调整

他的数值，主要标明了多个控件的尺寸比例关系

## 举例

一个 垂直布局 中包含 3 个按钮，希望第一个占 50%，第二、三个各占 25%

三个按钮设置：

sizePolicy -> 水平策略 -> Expanding Expanding Expanding
           -> 水平伸展 -> 2         1         1


