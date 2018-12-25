# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'heroDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog (object):
    def __init__(self):
        try:
            with open ("hero.txt")as file:
                self.data = file.readlines ()
        except FileNotFoundError:
            with open ("hero.txt", "w") as file2:
                file2.write ("9999\n匿名\n9999\n匿名\n9999\n匿名")
            with open ("hero.txt") as file3:
                self.data = file3.readlines ()
        self.Dialog = QtWidgets.QDialog ()
        self.setupUi ()
        self.Dialog.setWindowIcon (QtGui.QIcon ("media/mine.jpg"))
        self.pushButton.clicked.connect (self.reset)
        self.pushButton_2.clicked.connect (self.Dialog.close)

    def reset(self):
        with open ("hero.txt", "w") as file2:
            file2.write ("9999\n匿名\n9999\n匿名\n9999\n匿名")
        with open ("hero.txt") as file3:
            self.data = file3.readlines ()
        self.label_4.setText (str (self.data[0]).rstrip () + "秒")
        self.label_5.setText (str (self.data[2]).rstrip () + "秒")
        self.label_6.setText (str (self.data[4]).rstrip () + "秒")
        self.label_7.setText (self.data[1].rstrip ())
        self.label_8.setText (self.data[3].rstrip ())
        self.label_9.setText (self.data[5].rstrip ())

    def setupUi(self):
        self.Dialog.setObjectName ("Dialog")
        self.Dialog.setFixedSize (self.Dialog.minimumSize ())
        self.verticalLayout = QtWidgets.QVBoxLayout (self.Dialog)
        self.verticalLayout.setObjectName ("verticalLayout")
        self.widget = QtWidgets.QWidget (self.Dialog)
        self.widget.setObjectName ("widget")
        self.gridLayout = QtWidgets.QGridLayout (self.widget)
        self.gridLayout.setObjectName ("gridLayout")
        self.label_5 = QtWidgets.QLabel (self.widget)
        self.label_5.setAlignment (QtCore.Qt.AlignCenter)
        self.label_5.setObjectName ("label_5")
        self.gridLayout.addWidget (self.label_5, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel (self.widget)
        self.label_6.setAlignment (QtCore.Qt.AlignCenter)
        self.label_6.setObjectName ("label_6")
        self.gridLayout.addWidget (self.label_6, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel (self.widget)
        self.label_4.setAlignment (QtCore.Qt.AlignCenter)
        self.label_4.setObjectName ("label_4")
        self.gridLayout.addWidget (self.label_4, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel (self.widget)
        self.label.setAlignment (QtCore.Qt.AlignCenter)
        self.label.setObjectName ("label")
        self.gridLayout.addWidget (self.label, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel (self.widget)
        self.label_7.setAlignment (QtCore.Qt.AlignCenter)
        self.label_7.setObjectName ("label_7")
        self.gridLayout.addWidget (self.label_7, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel (self.widget)
        self.label_2.setAlignment (QtCore.Qt.AlignCenter)
        self.label_2.setObjectName ("label_2")
        self.gridLayout.addWidget (self.label_2, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel (self.widget)
        self.label_8.setAlignment (QtCore.Qt.AlignCenter)
        self.label_8.setObjectName ("label_8")
        self.gridLayout.addWidget (self.label_8, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel (self.widget)
        self.label_3.setAlignment (QtCore.Qt.AlignCenter)
        self.label_3.setObjectName ("label_3")
        self.gridLayout.addWidget (self.label_3, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel (self.widget)
        self.label_9.setAlignment (QtCore.Qt.AlignCenter)
        self.label_9.setObjectName ("label_9")
        self.gridLayout.addWidget (self.label_9, 5, 2, 1, 1)
        self.verticalLayout.addWidget (self.widget)
        self.widget_2 = QtWidgets.QWidget (self.Dialog)
        self.widget_2.setObjectName ("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout (self.widget_2)
        self.horizontalLayout.setObjectName ("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton (self.widget_2)
        self.pushButton.setObjectName ("pushButton")
        self.horizontalLayout.addWidget (self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton (self.widget_2)
        self.pushButton_2.setObjectName ("pushButton_2")
        self.horizontalLayout.addWidget (self.pushButton_2)
        self.verticalLayout.addWidget (self.widget_2)

        self.retranslateUi ()
        QtCore.QMetaObject.connectSlotsByName (self.Dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Dialog.setWindowTitle (_translate ("Dialog", "扫雷英雄榜"))
        self.label_4.setText (_translate ("Dialog", str (self.data[0]).rstrip () + "秒"))
        self.label_5.setText (_translate ("Dialog", str (self.data[2]).rstrip () + "秒"))
        self.label_6.setText (_translate ("Dialog", str (self.data[4]).rstrip () + "秒"))
        self.label.setText (_translate ("Dialog", "初级："))
        self.label_7.setText (_translate ("Dialog", self.data[1]).rstrip ())
        self.label_2.setText (_translate ("Dialog", "中级："))
        self.label_8.setText (_translate ("Dialog", self.data[3].rstrip ()))
        self.label_3.setText (_translate ("Dialog", "高级："))
        self.label_9.setText (_translate ("Dialog", self.data[5].rstrip ()))
        self.pushButton.setText (_translate ("Dialog", "重置"))
        self.pushButton_2.setText (_translate ("Dialog", "确定"))
