# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_MainWindow
# from temp import process 

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(499, 499)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(170, 150, 181, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(170, 210, 181, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 280, 161, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 60, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        def action():
            if self.textEdit.toPlainText() and self.textEdit_2.toPlainText():
                self.table = QtWidgets.QMainWindow()
                ui_table = Ui_MainWindow()
                ui_table.setupUi(self.table)
                self.table.show()
                Dialog.close()

        self.pushButton.clicked.connect(action)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit.setPlaceholderText(_translate("Dialog", "Логин")) 
        self.textEdit_2.setPlaceholderText(_translate("Dialog", "Пароль"))
        self.pushButton.setText(_translate("Dialog", "Войти"))
        self.label.setText(_translate("Dialog", "Вход в аккаунт"))

    
            
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
