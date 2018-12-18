# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pd.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
"""
AUTHOR: Olaniyan Clement
Phone No: 08167515092
email: clementolaniyan95@gmail.com
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(460, 399)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        TabWidget.setWindowIcon(icon)
        TabWidget.setStyleSheet("background-color: rgb(170, 170, 127);")
        TabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        TabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab = QtWidgets.QWidget()
        self.tab.setMinimumSize(QtCore.QSize(7, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tab.setFont(font)
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(180, 60, 113, 20))
        self.lineEdit.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"\n"
"")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 90, 113, 20))
        self.lineEdit_2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 120, 113, 20))
        self.lineEdit_3.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 150, 113, 20))
        self.lineEdit_4.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 240, 113, 20))
        self.lineEdit_5.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"")
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 180, 113, 20))
        self.lineEdit_6.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setClearButtonEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 210, 113, 20))
        self.lineEdit_7.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_7.setClearButtonEnabled(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_8.setGeometry(QtCore.QRect(180, 270, 113, 20))
        self.lineEdit_8.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.lineEdit_8.setPlaceholderText("")
        self.lineEdit_8.setClearButtonEnabled(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_9.setGeometry(QtCore.QRect(180, 300, 113, 20))
        self.lineEdit_9.setAutoFillBackground(False)
        self.lineEdit_9.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.lineEdit_9.setPlaceholderText("")
        self.lineEdit_9.setClearButtonEnabled(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(310, 60, 41, 22))
        self.spinBox.setObjectName("spinBox")
        self.credit1 = QtWidgets.QSpinBox(self.tab)
        self.credit1.setGeometry(QtCore.QRect(310, 90, 41, 22))
        self.credit1.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.credit1.setObjectName("credit1")
        self.credit2 = QtWidgets.QSpinBox(self.tab)
        self.credit2.setGeometry(QtCore.QRect(310, 120, 41, 22))
        self.credit2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.credit2.setObjectName("credit2")
        self.credit3 = QtWidgets.QSpinBox(self.tab)
        self.credit3.setGeometry(QtCore.QRect(310, 150, 41, 22))
        self.credit3.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.credit3.setObjectName("credit3")
        self.credit4 = QtWidgets.QSpinBox(self.tab)
        self.credit4.setGeometry(QtCore.QRect(310, 180, 41, 22))
        self.credit4.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.credit4.setObjectName("credit4")
        self.credit5 = QtWidgets.QSpinBox(self.tab)
        self.credit5.setGeometry(QtCore.QRect(310, 210, 41, 22))
        self.credit5.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.credit5.setObjectName("credit5")
        self.credit8 = QtWidgets.QSpinBox(self.tab)
        self.credit8.setGeometry(QtCore.QRect(310, 300, 41, 22))
        self.credit8.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.credit8.setObjectName("credit8")
        self.credit6 = QtWidgets.QSpinBox(self.tab)
        self.credit6.setGeometry(QtCore.QRect(310, 240, 41, 22))
        self.credit6.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.credit6.setObjectName("credit6")
        self.spinBox_9 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_9.setGeometry(QtCore.QRect(310, 270, 41, 22))
        self.spinBox_9.setObjectName("spinBox_9")
        self.credit0 = QtWidgets.QSpinBox(self.tab)
        self.credit0.setGeometry(QtCore.QRect(310, 60, 41, 22))
        self.credit0.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.credit0.setProperty("value", 1)
        self.credit0.setObjectName("credit0")
        self.credit7 = QtWidgets.QSpinBox(self.tab)
        self.credit7.setGeometry(QtCore.QRect(310, 270, 41, 22))
        self.credit7.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.credit7.setObjectName("credit7")
        self.unit0 = QtWidgets.QSpinBox(self.tab)
        self.unit0.setGeometry(QtCore.QRect(370, 60, 41, 22))
        self.unit0.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.unit0.setProperty("value", 1)
        self.unit0.setObjectName("unit0")
        self.spinBox_13 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_13.setGeometry(QtCore.QRect(370, 270, 41, 22))
        self.spinBox_13.setObjectName("spinBox_13")
        self.unit6 = QtWidgets.QSpinBox(self.tab)
        self.unit6.setGeometry(QtCore.QRect(370, 240, 41, 22))
        self.unit6.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.unit6.setObjectName("unit6")
        self.unit1 = QtWidgets.QSpinBox(self.tab)
        self.unit1.setGeometry(QtCore.QRect(370, 90, 41, 22))
        self.unit1.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.unit1.setObjectName("unit1")
        self.unit7 = QtWidgets.QSpinBox(self.tab)
        self.unit7.setGeometry(QtCore.QRect(370, 270, 41, 22))
        self.unit7.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.unit7.setObjectName("unit7")
        self.unit3 = QtWidgets.QSpinBox(self.tab)
        self.unit3.setGeometry(QtCore.QRect(370, 150, 41, 22))
        self.unit3.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.unit3.setObjectName("unit3")
        self.unit8 = QtWidgets.QSpinBox(self.tab)
        self.unit8.setGeometry(QtCore.QRect(370, 300, 41, 22))
        self.unit8.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.unit8.setObjectName("unit8")
        self.unit2 = QtWidgets.QSpinBox(self.tab)
        self.unit2.setGeometry(QtCore.QRect(370, 120, 41, 22))
        self.unit2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.unit2.setObjectName("unit2")
        self.unit4 = QtWidgets.QSpinBox(self.tab)
        self.unit4.setGeometry(QtCore.QRect(370, 180, 41, 22))
        self.unit4.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.unit4.setObjectName("unit4")
        self.unit5 = QtWidgets.QSpinBox(self.tab)
        self.unit5.setGeometry(QtCore.QRect(370, 210, 41, 22))
        self.unit5.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.unit5.setObjectName("unit5")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(190, 30, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(310, 30, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(370, 30, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 91, 101))
        self.label_4.setStyleSheet("background-color: rgb(230, 219, 255);\n"
"border-radius:  3px ;\n"
"border-left: 3px solid grey;\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_10.setGeometry(QtCore.QRect(180, 300, 113, 20))
        self.lineEdit_10.setAutoFillBackground(False)
        self.lineEdit_10.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.lineEdit_10.setPlaceholderText("")
        self.lineEdit_10.setClearButtonEnabled(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_11.setGeometry(QtCore.QRect(180, 330, 113, 20))
        self.lineEdit_11.setAutoFillBackground(False)
        self.lineEdit_11.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.lineEdit_11.setPlaceholderText("")
        self.lineEdit_11.setClearButtonEnabled(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.unit9 = QtWidgets.QSpinBox(self.tab)
        self.unit9.setGeometry(QtCore.QRect(370, 330, 41, 22))
        self.unit9.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.unit9.setObjectName("unit9")
        self.credit9 = QtWidgets.QSpinBox(self.tab)
        self.credit9.setGeometry(QtCore.QRect(310, 330, 41, 22))
        self.credit9.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.credit9.setObjectName("credit9")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(20, 320, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 255);\n"
"border-radius: 2px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        TabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        TabWidget.addTab(self.tab_2, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)
        self.pushButton.clicked.connect(self.gp)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "CGP Calculator"))
        self.label.setText(_translate("TabWidget", "Couse Tittle"))
        self.label_2.setText(_translate("TabWidget", "Credits"))
        self.label_3.setText(_translate("TabWidget", "Uinits"))
        self.label_4.setText(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:2px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">70 - 100 = 5C </span></p>\n"
"<p style=\" margin-top:5px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">60 - 69 = 4C</span></p>\n"
"<p style=\" margin-top:2px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">50 - 59 =  3C</span></p>\n"
"<p style=\" margin-top:2px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">45 - 49 = 2C</span></p>\n"
"<p style=\" margin-top:2px; margin-bottom:4px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">0 - 44 = 0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:2px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("TabWidget", "Calculate"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Calculator"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "About"))

    def gp(self):
        i = 0
        pointArr = list()
        credArr = list()
        multArr = list()
        for x in range(10):
            strpoint = "credit{}".format(x)
            strcredit = "unit{}".format(x)
            pv = "self.{}.value()".format(strpoint)
            cv = "self.{}.value()".format(strcredit)
            point = eval(pv)
            credit = eval(cv)
            mult = point * credit
            print(mult)
            pointArr.insert(i, point)
            credArr.insert(i, credit)
            multArr.insert(i, mult)
            i += 1
            if pointArr:
                result = (sum(multArr)) / (sum(credArr))

            print(sum(pointArr))
        win = QtWidgets.QMessageBox()
        win.setWindowTitle("Result")
        win.setText("Your GPA is {:.2f}".format(result))
        win.show()
        win.exec_()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())

