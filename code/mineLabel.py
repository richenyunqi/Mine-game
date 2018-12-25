from PyQt5 import QtWidgets, QtCore


class mineLabel (QtWidgets.QLabel):
    leftRelease = QtCore.pyqtSignal (int, int)  # 定义信号
    rightRelease = QtCore.pyqtSignal (int, int)
    leftPressed = QtCore.pyqtSignal (int, int)
    leftAndRightPressed = QtCore.pyqtSignal (int, int)
    leftAndRightRelease = QtCore.pyqtSignal (int, int)

    def __init__(self, i, j, num, parent=None):
        super (mineLabel, self).__init__ (parent)
        self.num = num
        self.i = i
        self.j = j
        self.leftAndRightClicked = False
        self.status = 0  # 0、1、2、3代表没挖开、挖开、旗子、疑问

    def mousePressEvent(self, e):  ##重载一下鼠标点击事件
        if e.buttons () == QtCore.Qt.LeftButton | QtCore.Qt.RightButton:
            self.leftAndRightPressed.emit (self.i, self.j)
            self.leftAndRightClicked = True
        elif e.buttons () == QtCore.Qt.LeftButton:
            self.leftPressed.emit (self.i, self.j)

    def mouseReleaseEvent(self, e):
        if self.leftAndRightClicked:
            self.leftAndRightRelease.emit (self.i, self.j)
            self.leftAndRightClicked=False
        else:
            if e.button () == QtCore.Qt.LeftButton:
                self.leftRelease.emit (self.i, self.j)
            elif e.button () == QtCore.Qt.RightButton:
                self.rightRelease.emit (self.i, self.j)
