# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'limit.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog (object):
    def setupUi(self, Dialog):
        Dialog.setObjectName ("Dialog")
        Dialog.setFixedSize (370, 80)
        Dialog.setWindowIcon (QtGui.QIcon ("media/mine.jpg"))
        self.gridLayout = QtWidgets.QGridLayout (Dialog)
        self.gridLayout.setObjectName ("gridLayout")
        self.label = QtWidgets.QLabel (Dialog)
        self.label.setObjectName ("label")
        self.gridLayout.addWidget (self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel (Dialog)
        self.label_4.setObjectName ("label_4")
        self.gridLayout.addWidget (self.label_4, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel (Dialog)
        self.label_2.setObjectName ("label_2")
        self.gridLayout.addWidget (self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel (Dialog)
        self.label_5.setObjectName ("label_5")
        self.gridLayout.addWidget (self.label_5, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel (Dialog)
        self.label_3.setObjectName ("label_3")
        self.gridLayout.addWidget (self.label_3, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel (Dialog)
        self.label_6.setObjectName ("label_6")
        self.gridLayout.addWidget (self.label_6, 2, 1, 1, 1)

        self.retranslateUi (Dialog)
        QtCore.QMetaObject.connectSlotsByName (Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle (_translate ("Dialog", "自定义参数上下限"))
        self.label.setText (_translate ("Dialog", "行数(row)："))
        self.label_4.setText (_translate ("Dialog", "[9,30]"))
        self.label_2.setText (_translate ("Dialog", "列数(column)："))
        self.label_5.setText (_translate ("Dialog", "[9,70]"))
        self.label_3.setText (_translate ("Dialog", "雷数(number)："))
        self.label_6.setText (_translate ("Dialog", "[max(10,row*column/7),(row-1)*(column-1)]"))
