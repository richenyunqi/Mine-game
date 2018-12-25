from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
import symbol


class SymbolDialog (symbol.Ui_Dialog):
    def __init__(self, Dialog):
        self.setupUi (Dialog)
        Dialog.setWindowIcon(QIcon("media/mine.jpg"))
        Dialog.setFixedSize (305, 286)
        labelNum = [self.label, self.label_3, self.label_5, self.label_7, self.label_9,
                    self.label_11, self.label_13, self.label_15]
        picNum = ["underway.png", "win.png", "fail.png", "mine.jpg", "flag.jpg", "question.jpg",
                  "correct.jpg", "mistake.jpg"]
        for i in range (0, len (labelNum)):
            labelNum[i].setFixedSize (27, 27)
            picNum[i] = "media/" + picNum[i]
            pixmap = QPixmap (picNum[i])
            labelNum[i].setPixmap (pixmap)
            labelNum[i].setScaledContents (True)
