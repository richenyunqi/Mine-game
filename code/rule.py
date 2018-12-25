# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'rule.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 326)
        Dialog.setWindowIcon (QtGui.QIcon ("mine.jpg"))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setMidLineWidth(3)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "游戏规则"))
        self.textBrowser.setDocumentTitle(_translate("Dialog", "游戏规则"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>游戏规则</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:10px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:29px; background-color:#ffffff;\"><span style=\" font-family:\'PingFang SC,Lantinghei SC,Microsoft YaHei,arial,宋体,sans-serif,tahoma\'; font-size:16px; color:#333333; background-color:#ffffff;\">      将所有非地雷的格子揭开则游戏胜利；踩到地雷格子</span><span style=\" font-family:\'PingFang SC,Lantinghei SC,Microsoft YaHei,arial,宋体,sans-serif,tahoma\'; font-size:16px; color:#333333;\">则游戏失败。<br />      游戏主区域由很多个方格组成。使用鼠标左键随机点击一个方格，方格即被打开并显示出方格中的数字，</span><span style=\" font-family:\'PingFang SC,Lantinghei SC,Microsoft YaHei,arial,宋体,sans-serif,tahoma\'; font-size:16px; font-weight:600; color:#333333;\">方格中数字则表示其周围的8个方格隐藏了几颗雷。</span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:29px; background-color:#ffffff;\"><span style=\" font-family:\'PingFang SC,Lantinghei SC,Microsoft YaHei,arial,宋体,sans-serif,tahoma\'; font-size:16px; color:#333333;\">      如果点开的格子为空白格，即其周围有0颗雷，则其周围格子自动打开，如果其周围还有空白格，则会继续打开并引发连锁反应。</span></p>\n"
"<p style=\" margin-top:10px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:29px; background-color:#ffffff;\"><span style=\" font-family:\'PingFang SC,Lantinghei SC,Microsoft YaHei,arial,宋体,sans-serif,tahoma\'; font-size:16px; color:#333333;\">      在你认为有雷的格子上，</span><span style=\" font-family:\'PingFang SC,Lantinghei SC,Microsoft YaHei,arial,宋体,sans-serif,tahoma\'; font-size:16px; font-weight:600; color:#333333;\">点击右键即可标记雷</span><span style=\" font-family:\'PingFang SC,Lantinghei SC,Microsoft YaHei,arial,宋体,sans-serif,tahoma\'; font-size:16px; color:#333333;\">。如果一个已打开格子周围所有的雷已经正确标出，则可以在此格上同时点击鼠标左右键以打开其周围剩余的无雷格。</span></p></body></html>"))
