# 使用 pyinstaller 打包程序

`pyinstaller -F --distpath ./tutorial-4/release ./tutorial-3/main.py`

`-F` 生成当前平台可用的可执行文件

`-distpath` 生成的可执行文件，放在哪里，这里放在教程4的 release 文件夹下

> 生成的可执行文件，因为包含了所有 pyqt 组件，所以一般比较大，都是30M~70M, 后期
要学习如何精简可执行文件大小。