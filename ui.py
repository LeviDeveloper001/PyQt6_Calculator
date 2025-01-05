from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(280, 400)
        MainWindow.setMinimumSize(QtCore.QSize(280, 400))
        MainWindow.setMaximumSize(QtCore.QSize(280, 400))
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("background-color: rgb(71, 71, 71);\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.main_label.setEnabled(False)
        self.main_label.setGeometry(QtCore.QRect(10, 0, 271, 61))
        self.main_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.main_label.setStyleSheet("color: rgb(170, 0, 0);")
        self.main_label.setObjectName("main_label")
        self.button_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_2.setEnabled(False)
        self.button_2.setGeometry(QtCore.QRect(140, 190, 68, 68))
        self.button_2.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_2.setObjectName("button_2")
        self.button_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_1.setEnabled(False)
        self.button_1.setGeometry(QtCore.QRect(70, 190, 68, 68))
        self.button_1.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_1.setObjectName("button_1")
        self.button_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_3.setEnabled(False)
        self.button_3.setGeometry(QtCore.QRect(210, 190, 68, 68))
        self.button_3.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_3.setObjectName("button_3")
        self.button_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_4.setEnabled(False)
        self.button_4.setGeometry(QtCore.QRect(70, 260, 68, 68))
        self.button_4.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_4.setObjectName("button_4")
        self.button_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_5.setEnabled(False)
        self.button_5.setGeometry(QtCore.QRect(140, 260, 68, 68))
        self.button_5.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_5.setObjectName("button_5")
        self.button_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_6.setEnabled(False)
        self.button_6.setGeometry(QtCore.QRect(210, 260, 68, 68))
        self.button_6.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_6.setObjectName("button_6")
        self.button_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_7.setEnabled(False)
        self.button_7.setGeometry(QtCore.QRect(70, 330, 68, 68))
        self.button_7.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_7.setObjectName("button_7")
        self.button_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_8.setEnabled(False)
        self.button_8.setGeometry(QtCore.QRect(140, 330, 68, 68))
        self.button_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.button_8.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_8.setObjectName("button_8")
        self.button_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_9.setEnabled(False)
        self.button_9.setGeometry(QtCore.QRect(210, 330, 68, 68))
        self.button_9.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_9.setObjectName("button_9")
        self.button_0 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_0.setEnabled(False)
        self.button_0.setGeometry(QtCore.QRect(0, 260, 68, 68))
        self.button_0.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_0.setObjectName("button_0")
        self.button_equal = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_equal.setEnabled(False)
        self.button_equal.setGeometry(QtCore.QRect(0, 330, 68, 68))
        self.button_equal.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_equal.setObjectName("button_equal")
        self.button_plus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_plus.setEnabled(False)
        self.button_plus.setGeometry(QtCore.QRect(140, 120, 68, 68))
        self.button_plus.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_plus.setCheckable(False)
        self.button_plus.setObjectName("button_plus")
        self.button_clear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_clear.setEnabled(False)
        self.button_clear.setGeometry(QtCore.QRect(0, 190, 68, 68))
        self.button_clear.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_clear.setObjectName("button_clear")
        self.button_divide = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_divide.setEnabled(False)
        self.button_divide.setGeometry(QtCore.QRect(70, 120, 68, 68))
        self.button_divide.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_divide.setObjectName("button_divide")
        self.button_minus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_minus.setEnabled(False)
        self.button_minus.setGeometry(QtCore.QRect(0, 120, 68, 68))
        self.button_minus.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_minus.setObjectName("button_minus")
        self.button_multiplying = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_multiplying.setEnabled(False)
        self.button_multiplying.setGeometry(QtCore.QRect(210, 120, 68, 68))
        self.button_multiplying.setStyleSheet("font: 30pt \"MS Shell Dlg 2\";\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid red;\n"
"border-radius: 5px;")
        self.button_multiplying.setObjectName("button_multiplying")
        self.result_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(6, 63, 271, 51))
        self.result_label.setStyleSheet("color: rgb(170, 0, 0);\n"
"text-align: center;\n"
"background-color: rgb(85, 170, 127);\n"
"font: 25pt \"MS Shell Dlg 2\";")
        self.result_label.setObjectName("result_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Calculator</span></p></body></html>"))
        self.button_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_1.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_7.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_0.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_equal.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_equal.setText(_translate("MainWindow", "="))
        self.button_plus.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_clear.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_clear.setText(_translate("MainWindow", "C"))
        self.button_divide.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_divide.setText(_translate("MainWindow", "/"))
        self.button_minus.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_multiplying.setToolTip(_translate("MainWindow", "<html><head/><body><p>1</p></body></html>"))
        self.button_multiplying.setText(_translate("MainWindow", "*"))
        self.result_label.setText(_translate("MainWindow", "0"))
