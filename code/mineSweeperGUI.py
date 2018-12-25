from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QCoreApplication
from PyQt5.QtGui import QPalette, QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QLineEdit, QInputDialog
import superGUI, mineLabel, selfDefinedParameter, heroDialog, rule, symbolDialog, limit
import random, sip, pygame


class MineSweeperGUI(superGUI.Ui_MainWindow):
    def __init__(self, MainWindow):
        file = r'media/background.mp3'
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1, 0)
        self.row = 9
        self.column = 9
        self.mineNum = 10
        self.rank = 0
        self.finish = False
        self.mainWindow = MainWindow
        self.mainWindow.setWindowIcon(QIcon("media/mine.jpg"))
        self.mainWindow.setFixedSize(self.mainWindow.minimumSize())
        self.setupUi(self.mainWindow)
        self.mineLabel = []
        self.initMineArea()
        self.createMine()
        self.label_2.leftRelease.connect(self.gameStart)
        pixmap = QPixmap("media/underway.png")
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.red)  # 设置字体颜色
        self.label_3.setPalette(pe)
        self.label_3.setFont(QFont("Roman times", 15, QFont.Bold))
        self.label.setPalette(pe)
        self.label.setFont(QFont("Roman times", 15, QFont.Bold))
        self.label.setText(str(self.mineNum))
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeCount)
        self.timeStart = False

        # 绑定菜单栏事件
        self.action.triggered.connect(self.gameStart)
        self.action_B.triggered.connect(self.action_BEvent)
        self.action_I.triggered.connect(self.action_IEvent)
        self.action_E.triggered.connect(self.action_Event)
        self.action_C.triggered.connect(self.action_CEvent)
        self.action_T.triggered.connect(self.action_TEvent)
        self.action_R.triggered.connect(self.action_REvent)
        self.action_S_2.triggered.connect(self.action_SEvent)
        self.action_L_2.triggered.connect(self.action_LEvent)
        self.action_X_2.triggered.connect(QCoreApplication.instance().quit)
        self.actionChecked('B')  # 默认选择初级

    def outOfBorder(self, i, j):
        if i < 0 or i >= self.row or j < 0 or j >= self.column:
            return True
        return False

    def createMine(self):
        num = self.mineNum
        while num > 0:
            r = random.randint(0, self.row - 1)
            c = random.randint(0, self.column - 1)
            if self.mineLabel[r][c].num != -1:
                self.mineLabel[r][c].num = -1
                num -= 1
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if not self.outOfBorder(i, j) and (
                                self.mineLabel[i][j].num != -1):
                            self.mineLabel[i][j].num += 1

    def initMineArea(self):
        self.gridLayout.setSpacing(0)
        for i in range(0, self.row):
            self.mineLabel.append([])
            for j in range(0, self.column):
                label = mineLabel.mineLabel(i, j, 0, "")
                label.setMinimumSize(18, 18)
                label.setFrameShape(QtWidgets.QFrame.WinPanel)
                label.setFrameShadow(QtWidgets.QFrame.Raised)
                label.setAlignment(Qt.AlignCenter)

                # 绑定雷区点击事件
                label.leftPressed.connect(self.mineAreaLeftPressed)
                label.leftAndRightPressed.connect(self.mineAreaLeftAndRightPressed)
                label.leftAndRightRelease.connect(self.mineAreaLeftAndRightRelease)
                label.leftRelease.connect(self.mineAreaLeftRelease)
                label.rightRelease.connect(self.mineAreaRightRelease)

                self.mineLabel[i].append(label)
                self.gridLayout.addWidget(label, i, j)

    def timeCount(self):
        self.label_3.setText(str(int(self.label_3.text()) + 1))

    def setFontColor(self, i, j):
        if self.mineLabel[i][j].num == 1:
            self.mineLabel[i][j].setStyleSheet("color:blue;")
        elif self.mineLabel[i][j].num == 2:
            self.mineLabel[i][j].setStyleSheet("color:brown;")
        elif self.mineLabel[i][j].num == 3:
            self.mineLabel[i][j].setStyleSheet("color:red;")
        elif self.mineLabel[i][j].num == 4:
            self.mineLabel[i][j].setStyleSheet("color:purple;")
        elif self.mineLabel[i][j].num == 5:
            self.mineLabel[i][j].setStyleSheet("color:orange;")
        elif self.mineLabel[i][j].num == 6:
            self.mineLabel[i][j].setStyleSheet("color:pink;")
        elif self.mineLabel[i][j].num == 7:
            self.mineLabel[i][j].setStyleSheet("color:#00aa00;")
        elif self.mineLabel[i][j].num == 8:
            self.mineLabel[i][j].setStyleSheet("color:black;")

    def DFS(self, i, j, start0):
        if self.mineLabel[i][j].status == 0:
            self.mineLabel[i][j].status = 1
            self.mineLabel[i][j].setFrameShape(QtWidgets.QFrame.Panel)
            self.mineLabel[i][j].setFrameShadow(QtWidgets.QFrame.Sunken)
            if self.mineLabel[i][j].num > 0:
                if not self.timeStart:
                    self.timeStart = True
                    self.timer.start()
                self.setFontColor(i, j)
                self.mineLabel[i][j].setFont(QFont("Roman times", 15, QFont.Bold))
                self.mineLabel[i][j].setText(str(self.mineLabel[i][j].num))
            if self.isGameFinished():
                self.gameWin()
            if (start0 and self.mineLabel[i][j].num == 0) or (
                    not start0 and self.mineLabel[i][j].num == 0):
                for r in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        if not self.outOfBorder(r, c) and self.mineLabel[r][
                            c].status == 0 and self.mineLabel[r][
                            c].num != -1:
                            self.DFS(r, c, start0)

    def mineAreaLeftRelease(self, i, j):
        if not self.finish:
            if self.mineLabel[i][j].num >= 0:
                self.DFS(i, j, self.mineLabel[i][j].num == 0)
                if self.isGameFinished():
                    self.gameWin()
            else:
                self.gameFailed()

    def mineAreaRightRelease(self, i, j):
        if not self.finish:
            if self.mineLabel[i][j].status == 0:
                pixmap = QPixmap("media/flag.jpg")
                self.mineLabel[i][j].setPixmap(pixmap)
                self.mineLabel[i][j].setScaledContents(True)
                self.mineLabel[i][j].status = 2
                self.label.setText(str(int(self.label.text()) - 1))
            elif self.mineLabel[i][j].status == 2:
                self.mineLabel[i][j].setPixmap(QPixmap("media/question.jpg"))
                self.mineLabel[i][j].status = 3
                self.label.setText(str(int(self.label.text()) + 1))
            elif self.mineLabel[i][j].status == 3:
                self.mineLabel[i][j].setPixmap(QPixmap(""))
                self.mineLabel[i][j].status = 0

    def mineAreaLeftPressed(self, i, j):
        if not self.finish:
            if self.mineLabel[i][j].status == 0:
                self.mineLabel[i][j].setFrameShape(QtWidgets.QFrame.Panel)
                self.mineLabel[i][j].setFrameShadow(QtWidgets.QFrame.Sunken)

    def mineAreaLeftAndRightPressed(self, i, j):
        if not self.finish:
            if self.mineLabel[i][j].status == 1:
                count = 0
                for r in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        if not self.outOfBorder(r, c):
                            if self.mineLabel[r][c].status == 0 or self.mineLabel[r][c].status == 3:
                                self.mineLabel[r][c].setFrameShape(QtWidgets.QFrame.Panel)
                                self.mineLabel[r][c].setFrameShadow(QtWidgets.QFrame.Sunken)
                            elif self.mineLabel[r][c].status == 2:
                                count += 1
                return count == self.mineLabel[i][j].num
            else:
                return False

    def mineAreaLeftAndRightRelease(self, i, j):
        if not self.finish:
            if self.mineLabel[i][j].status == 1:
                if self.mineAreaLeftAndRightPressed(i, j):
                    Fail = False
                    for r in range(i - 1, i + 2):
                        for c in range(j - 1, j + 2):
                            if not self.outOfBorder(r, c):
                                if self.mineLabel[r][c].status == 0 or self.mineLabel[r][c].status == 3:
                                    if self.mineLabel[r][c].status == 3:
                                        self.mineLabel[r][c].setPixmap(QPixmap(""))
                                        self.mineLabel[r][c].setScaledContents(True)
                                        self.mineLabel[r][c].status = 0
                                    if self.mineLabel[r][c].num >= 0:
                                        self.DFS(r, c, self.mineLabel[r][c].num == 0)
                                    else:
                                        Fail = True
                    if Fail:
                        self.gameFailed()
                else:
                    for r in range(i - 1, i + 2):
                        for c in range(j - 1, j + 2):
                            if not self.outOfBorder(r, c):
                                if self.mineLabel[r][c].status == 0 or self.mineLabel[r][c].status == 3:
                                    self.mineLabel[r][c].setFrameShape(QtWidgets.QFrame.WinPanel)
                                    self.mineLabel[r][c].setFrameShadow(QtWidgets.QFrame.Raised)

    def gameStart(self):
        for i in self.mineLabel:
            for j in i:
                self.gridLayout.removeWidget(j)
                sip.delete(j)
        self.label.setText(str(self.mineNum))
        pixmap = QPixmap("media/underway.png")
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        self.label_3.setText("0")
        self.timeStart = False
        self.finish = False
        self.timer.stop()
        self.mineLabel.clear()
        self.mineLabel = []
        self.initMineArea()
        self.createMine()
        self.mainWindow.setMinimumSize(0, 0)
        self.mainWindow.resize(self.mainWindow.minimumSize())

    def gameFinished(self):
        for i in self.mineLabel:
            for j in i:
                if j.num == -1 or j.status == 2:
                    j.setFrameShape(QtWidgets.QFrame.Panel)
                    j.setFrameShadow(QtWidgets.QFrame.Sunken)
                    if j.num == -1 and j.status == 2:
                        pixmap = QPixmap("media/correct.jpg")
                    elif j.num == -1:
                        pixmap = QPixmap("media/mine.jpg")
                    else:
                        pixmap = QPixmap("media/mistake.jpg")
                    j.setPixmap(pixmap)
                    j.setScaledContents(True)
                j.status = 1
        self.timer.stop()
        self.finish = True

    def isGameFinished(self):
        for i in self.mineLabel:
            for j in i:
                if j.status == 0 and j.num != -1:
                    return False
        return True

    def gameWin(self):
        pixmap = QPixmap("media/win.png")
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        self.gameFinished()
        try:
            with open("hero.txt")as file:
                data = file.readlines()
        except FileNotFoundError:
            with open("hero.txt", "w") as file2:
                file2.write("9999\n匿名\n9999\n匿名\n9999\n匿名")
            with open("hero.txt") as file3:
                data = file3.readlines()
        if self.rank < 3 and int(data[self.rank * 2].rstrip()) > int(
                self.label_3.text()):
            dic = ["初级", "中级", "高级"]
            s, ok = QInputDialog.getText(self.mainWindow, "已破纪录", "已破" + dic[
                int(self.rank)] + "记录,请留尊姓大名:",
                                         QLineEdit.Normal, "匿名")
            if ok and s.strip():
                data[self.rank * 2] = self.label_3.text() + "\n"
                data[self.rank * 2 + 1] = s + "\n"
                with open("hero.txt", "w") as file2:
                    for i in data:
                        file2.write(i)
                ui = heroDialog.Ui_Dialog()
                ui.Dialog.setModal(True)
                ui.Dialog.show()
                ui.Dialog.exec_()

    def gameFailed(self):
        pixmap = QPixmap("media/fail.png")
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        self.gameFinished()

    def actionChecked(self, k):
        self.action_B.setChecked(False)
        self.action_I.setChecked(False)
        self.action_E.setChecked(False)
        self.action_C.setChecked(False)
        if k == 'B':
            self.action_B.setChecked(True)
        elif k == 'I':
            self.action_I.setChecked(True)
        elif k == 'E':
            self.action_E.setChecked(True)
        elif k == 'C':
            self.action_C.setChecked(True)

    def action_BEvent(self):
        self.actionChecked('B')
        self.row = 9
        self.column = 9
        self.mineNum = 10
        self.rank = 0
        self.gameStart()

    def action_IEvent(self):
        self.actionChecked('I')
        self.row = 16
        self.column = 16
        self.mineNum = 40
        self.rank = 1
        self.gameStart()

    def action_Event(self):
        self.actionChecked('E')
        self.row = 16
        self.column = 30
        self.mineNum = 99
        self.rank = 2
        self.gameStart()

    def action_CEvent(self):
        self.actionChecked('C')
        ui = selfDefinedParameter.Ui_Dialog(self.row, self.column,
                                            self.mineNum)
        ui.Dialog.setModal(True)
        ui.Dialog.show()
        ui.Dialog.exec_()
        if ui.alter:
            self.row = ui.row
            self.column = ui.column
            self.mineNum = ui.mineNum
            self.rank = 3
            self.gameStart()

    def action_TEvent(self):
        ui = heroDialog.Ui_Dialog()
        ui.Dialog.setModal(True)
        ui.Dialog.show()
        ui.Dialog.exec_()

    def action_REvent(self):
        Dialog = QtWidgets.QDialog()
        ui = rule.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def action_SEvent(self):
        Dialog = QtWidgets.QDialog()
        ui = symbolDialog.SymbolDialog(Dialog)
        Dialog.show()
        Dialog.exec_()

    def action_LEvent(self):
        Dialog = QtWidgets.QDialog()
        ui = limit.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
