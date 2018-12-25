from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mineSweeperGUI

# import sweeper
if __name__ == "__main__":
    app = QtWidgets.QApplication (sys.argv)
    MainWindow = QtWidgets.QMainWindow ()
    ui = mineSweeperGUI.MineSweeperGUI (MainWindow)
    MainWindow.show()
    sys.exit (app.exec_())
