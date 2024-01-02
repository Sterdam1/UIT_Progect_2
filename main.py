# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from db_requests import db
from functools import partial
from EDI import *

class Ui_MainWindow(object):
    def setupMainWindow(self, MainWindow):
        self.suki = []
        self.last_text = ''
        self.last_action = {}
        self.listy = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 861, 651))
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.items = QtWidgets.QWidget()
        self.items.setObjectName("items")
        self.comboBox_4 = QtWidgets.QComboBox(self.items)
        self.comboBox_4.setGeometry(50, 460, 121, 31)
        self.comboBox_4.setObjectName('comboBox_4')
        self.comboBox_4.insertItems(0, ['По возрастанию', 'По убыванию', 'По умолчанию'])
        self.comboBox_4.setCurrentIndex(2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.items)
        self.lineEdit_2.setGeometry(180, 460, 141, 31)
        self.lineEdit_2.setPlaceholderText('Поиск')
        self.lineEdit_2.setObjectName('lineEdit_2')
        self.pushButton_2 = QtWidgets.QPushButton(self.items)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 460, 181, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.items)
        self.tableWidget_2.setGeometry(QtCore.QRect(60, 120, 661, 301))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setRowCount(0)
        self.gen_table(self.tableWidget_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.items)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 460, 181, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_4 = QtWidgets.QPushButton(self.items)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 50, 181, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.items)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 50, 181, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.items)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.items, "")
        self.storages = QtWidgets.QWidget()
        self.storages.setObjectName("storages")
        self.comboBox_5 = QtWidgets.QComboBox(self.storages)
        self.comboBox_5.setGeometry(50, 460, 121, 31)
        self.comboBox_5.setObjectName('comboBox_5')
        self.comboBox_5.insertItems(0, ['По возрастанию', 'По убыванию', 'По умолчанию'])
        self.comboBox_5.setCurrentIndex(2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.storages)
        self.lineEdit_3.setGeometry(180, 460, 141, 31)
        self.lineEdit_3.setPlaceholderText('Поиск')
        self.lineEdit_3.setObjectName('lineEdit_3')
        self.pushButton_6 = QtWidgets.QPushButton(self.storages)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 50, 181, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.storages)
        self.label_3.setGeometry(QtCore.QRect(70, 30, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.storages)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 460, 181, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setEnabled(False)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.storages)
        self.tableWidget_3.setGeometry(QtCore.QRect(60, 120, 661, 301))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.gen_table(self.tableWidget_3, name = 'Depots')
        self.pushButton_8 = QtWidgets.QPushButton(self.storages)
        self.pushButton_8.setGeometry(QtCore.QRect(540, 460, 181, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.storages)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 50, 181, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.tabWidget.addTab(self.storages, "")
        self.people = QtWidgets.QWidget()
        self.people.setObjectName("people")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.people)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, -4, 864, 651))
        self.tabWidget_2.setMovable(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.clients = QtWidgets.QWidget()
        self.clients.setObjectName("clients")
        self.comboBox_6 = QtWidgets.QComboBox(self.clients)
        self.comboBox_6.setGeometry(50, 460, 121, 31)
        self.comboBox_6.setObjectName('comboBox_6')
        self.comboBox_6.insertItems(0, ['По возрастанию', 'По убыванию', 'По умолчанию'])
        self.comboBox_6.setCurrentIndex(2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.clients)
        self.lineEdit_4.setGeometry(180, 460, 141, 31)
        self.lineEdit_4.setPlaceholderText('Поиск')
        self.lineEdit_4.setObjectName('lineEdit_4')
        self.pushButton_18 = QtWidgets.QPushButton(self.clients)
        self.pushButton_18.setGeometry(QtCore.QRect(340, 50, 181, 31))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_15 = QtWidgets.QPushButton(self.clients)
        self.pushButton_15.setGeometry(QtCore.QRect(540, 50, 181, 31))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_17 = QtWidgets.QPushButton(self.clients)
        self.pushButton_17.setGeometry(QtCore.QRect(540, 460, 181, 31))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_16 = QtWidgets.QPushButton(self.clients)
        self.pushButton_16.setGeometry(QtCore.QRect(340, 460, 181, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.setEnabled(False)
        self.tableWidget_6 = QtWidgets.QTableWidget(self.clients)
        self.tableWidget_6.setGeometry(QtCore.QRect(60, 120, 661, 301))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.gen_table(widget=self.tableWidget_6, name='Contractors', type='Покупатель')
        self.label_6 = QtWidgets.QLabel(self.clients)
        self.label_6.setGeometry(QtCore.QRect(70, 30, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tabWidget_2.addTab(self.clients, "")
        self.suppliers = QtWidgets.QWidget()
        self.suppliers.setObjectName("suppliers")
        self.comboBox_7 = QtWidgets.QComboBox(self.suppliers)
        self.comboBox_7.setGeometry(50, 460, 121, 31)
        self.comboBox_7.setObjectName('comboBox_7')
        self.comboBox_7.insertItems(0, ['По возрастанию', 'По убыванию', 'По умолчанию'])
        self.comboBox_7.setCurrentIndex(2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.suppliers)
        self.lineEdit_5.setGeometry(180, 460, 141, 31)
        self.lineEdit_5.setPlaceholderText('Поиск')
        self.lineEdit_5.setObjectName('lineEdit_5')
        self.pushButton_19 = QtWidgets.QPushButton(self.suppliers)
        self.pushButton_19.setGeometry(QtCore.QRect(540, 50, 181, 31))
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_7 = QtWidgets.QLabel(self.suppliers)
        self.label_7.setGeometry(QtCore.QRect(70, 30, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_20 = QtWidgets.QPushButton(self.suppliers)
        self.pushButton_20.setGeometry(QtCore.QRect(340, 460, 181, 31))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.setEnabled(False)
        self.tableWidget_7 = QtWidgets.QTableWidget(self.suppliers)
        self.tableWidget_7.setGeometry(QtCore.QRect(60, 120, 661, 301))
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(0)
        self.tableWidget_7.setRowCount(0)
        self.gen_table(widget=self.tableWidget_7, name='Contractors', type='Поставщик')
        self.pushButton_21 = QtWidgets.QPushButton(self.suppliers)
        self.pushButton_21.setGeometry(QtCore.QRect(540, 460, 181, 31))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.suppliers)
        self.pushButton_22.setGeometry(QtCore.QRect(340, 50, 181, 31))
        self.pushButton_22.setObjectName("pushButton_22")
        self.tabWidget_2.addTab(self.suppliers, "")
        self.contractors = QtWidgets.QWidget()
        self.contractors.setObjectName("contractors")
        self.comboBox_8 = QtWidgets.QComboBox(self.contractors)
        self.comboBox_8.setGeometry(50, 460, 121, 31)
        self.comboBox_8.setObjectName('comboBox_8')
        self.comboBox_8.insertItems(0, ['По возрастанию', 'По убыванию', 'По умолчанию'])
        self.comboBox_8.setCurrentIndex(2)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.contractors)
        self.lineEdit_6.setGeometry(180, 460, 141, 31)
        self.lineEdit_6.setPlaceholderText('Поиск')
        self.lineEdit_6.setObjectName('lineEdit_6')
        self.pushButton_23 = QtWidgets.QPushButton(self.contractors)
        self.pushButton_23.setGeometry(QtCore.QRect(540, 50, 181, 31))
        self.pushButton_23.setObjectName("pushButton_23")
        self.label_8 = QtWidgets.QLabel(self.contractors)
        self.label_8.setGeometry(QtCore.QRect(70, 30, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_24 = QtWidgets.QPushButton(self.contractors)
        self.pushButton_24.setGeometry(QtCore.QRect(340, 460, 181, 31))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_24.setEnabled(False)
        self.tableWidget_8 = QtWidgets.QTableWidget(self.contractors)
        self.tableWidget_8.setGeometry(QtCore.QRect(60, 120, 661, 301))
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(0)
        self.tableWidget_8.setRowCount(0)
        self.gen_table(widget=self.tableWidget_8, name='Contractors', type='Подрядчик')
        self.pushButton_25 = QtWidgets.QPushButton(self.contractors)
        self.pushButton_25.setGeometry(QtCore.QRect(540, 460, 181, 31))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.contractors)
        self.pushButton_26.setGeometry(QtCore.QRect(340, 50, 181, 31))
        self.pushButton_26.setObjectName("pushButton_26")
        self.tabWidget_2.addTab(self.contractors, "")
        self.tabWidget.addTab(self.people, "")
        self.create_order = QtWidgets.QWidget()
        self.create_order.setObjectName("create_order")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.create_order)
        self.lineEdit_7.setGeometry(380, 460, 141, 31)
        self.lineEdit_7.setPlaceholderText('Поиск')
        self.lineEdit_7.setObjectName('lineEdit_7')
        self.pushButton = QtWidgets.QPushButton(self.create_order)
        self.pushButton.setGeometry(QtCore.QRect(540, 460, 181, 31))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.create_order)
        self.tableWidget.setGeometry(QtCore.QRect(60, 120, 661, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gen_table(widget=self.tableWidget)
        self.label = QtWidgets.QLabel(self.create_order)
        self.label.setGeometry(QtCore.QRect(540, 40, 181, 21))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.create_order)
        self.comboBox.setGeometry(QtCore.QRect(540, 70, 181, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox.setPlaceholderText('Выбрать клиента')
        self.comboBox.currentTextChanged.connect(self.order_btn_switch)
        self.fill_comboBox(self.comboBox, name='Contractors', id=1)
        self.label_9 = QtWidgets.QLabel(self.create_order)
        self.label_9.setGeometry(QtCore.QRect(60, 30, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.create_order, "")
        self.order_list = QtWidgets.QWidget()
        self.order_list.setObjectName("order_list")
        self.pushButton_10 = QtWidgets.QPushButton(self.order_list)
        self.pushButton_10.setGeometry(QtCore.QRect(230, 440, 151, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_4 = QtWidgets.QLabel(self.order_list)
        self.label_4.setGeometry(QtCore.QRect(70, 30, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_11 = QtWidgets.QPushButton(self.order_list)
        self.pushButton_11.setGeometry(QtCore.QRect(60, 440, 151, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.order_list)
        self.tableWidget_4.setGeometry(QtCore.QRect(60, 120, 661, 301))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.gen_table(self.tableWidget_4, 'Oder')
        self.pushButton_12 = QtWidgets.QPushButton(self.order_list)
        self.pushButton_12.setGeometry(QtCore.QRect(570, 440, 151, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_14 = QtWidgets.QPushButton(self.order_list)
        self.pushButton_14.setGeometry(QtCore.QRect(400, 440, 151, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.tabWidget.addTab(self.order_list, "")
        self.remains = QtWidgets.QWidget()
        self.remains.setObjectName("remains")
        self.pushButton_13 = QtWidgets.QPushButton(self.remains)
        self.pushButton_13.setGeometry(QtCore.QRect(540, 50, 181, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_5 = QtWidgets.QLabel(self.remains)
        self.label_5.setGeometry(QtCore.QRect(70, 30, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.remains)
        self.tableWidget_5.setGeometry(QtCore.QRect(60, 120, 661, 301))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)

        self.textEdit = QtWidgets.QTextEdit(self.create_order)
        self.textEdit.setGeometry(QtCore.QRect(130, 500, 221, 41))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.create_order)
        self.lineEdit.setGeometry(QtCore.QRect(130, 470, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.create_order)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 550, 221, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_10 = QtWidgets.QLabel(self.create_order)
        self.label_10.setGeometry(QtCore.QRect(60, 470, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.create_order)
        self.label_11.setGeometry(QtCore.QRect(60, 510, 47, 13))
        self.label_11.setObjectName("label_11")
        self.comboBox_2 = QtWidgets.QComboBox(self.remains)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 50, 181, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setPlaceholderText('Выбрать склад')
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_2.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.fill_comboBox(self.comboBox_2)
        self.comboBox_2.currentIndexChanged.connect(partial(self.gen_table, self.tableWidget_5, 'Goods', ['Depots',self.comboBox_2]))
        self.comboBox_3 = QtWidgets.QComboBox(self.create_order)
        self.comboBox_3.setGeometry(QtCore.QRect(60, 80, 181, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.setPlaceholderText('Выбрать склад')
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_3.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox_3.currentIndexChanged.connect(
            partial(self.gen_table, self.tableWidget, 'Goods', ['Depots', self.comboBox_3]))
        self.fill_comboBox(self.comboBox_3)
        self.tabWidget.addTab(self.remains, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_12 = QtWidgets.QLabel(self.create_order)
        self.label_12.setGeometry(QtCore.QRect(60, 560, 71, 16))
        self.label_12.setObjectName("label_12")
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.gen_order)
        self.lineEdit.textChanged.connect(self.order_btn_switch) # телефон
        self.textEdit.textChanged.connect(self.order_btn_switch) # адрес
        # self.textEdit_2 # комментарий

        # add row buttons, last param takes a list or buttons we need to disable
        self.pushButton_4.clicked.connect(partial(self.add_row, self.tableWidget_2, [self.pushButton_3, self.pushButton_5, self.pushButton_4]))
        self.pushButton_9.clicked.connect(partial(self.add_row, self.tableWidget_3, [self.pushButton_7, self.pushButton_9, self.pushButton_6]))
        self.pushButton_18.clicked.connect(partial(self.add_row, self.tableWidget_6, [self.pushButton_16, self.pushButton_18, self.pushButton_15]))
        self.pushButton_22.clicked.connect(partial(self.add_row, self.tableWidget_7, [self.pushButton_20, self.pushButton_22, self.pushButton_19]))
        self.pushButton_26.clicked.connect(partial(self.add_row, self.tableWidget_8, [self.pushButton_24, self.pushButton_26, self.pushButton_23]))
        
        # del row buttons, last param takes a list or buttons we need to disable
        self.pushButton_5.clicked.connect(partial(self.del_row, self.tableWidget_2, [self.pushButton_3, self.pushButton_5, self.pushButton_4]))
        self.pushButton_6.clicked.connect(partial(self.del_row, self.tableWidget_3, [self.pushButton_7, self.pushButton_9, self.pushButton_6]))
        self.pushButton_15.clicked.connect(partial(self.del_row, self.tableWidget_6, [self.pushButton_16, self.pushButton_18, self.pushButton_15]))
        self.pushButton_19.clicked.connect(partial(self.del_row, self.tableWidget_7, [self.pushButton_20, self.pushButton_22, self.pushButton_19]))
        self.pushButton_23.clicked.connect(partial(self.del_row, self.tableWidget_8,  [self.pushButton_24, self.pushButton_26, self.pushButton_23]))

        # save buttons, last param takes a list or buttons we need to enable
        self.pushButton_3.clicked.connect(partial(self.save_table, self.tableWidget_2, 'Goods', [self.pushButton_3, self.pushButton_5, self.pushButton_4]))
        self.pushButton_7.clicked.connect(partial(self.save_table, self.tableWidget_3, 'Depots', [self.pushButton_7, self.pushButton_9, self.pushButton_6]))
        self.pushButton_16.clicked.connect(partial(self.save_table, self.tableWidget_6, 'Contractors', [self.pushButton_16, self.pushButton_18, self.pushButton_15]))
        self.pushButton_20.clicked.connect(partial(self.save_table, self.tableWidget_7, 'Contractors', [self.pushButton_20, self.pushButton_22, self.pushButton_19]))
        self.pushButton_24.clicked.connect(partial(self.save_table, self.tableWidget_8, 'Contractors', [self.pushButton_24, self.pushButton_26, self.pushButton_23]))

        # cansel buttons
        self.pushButton_2.clicked.connect(partial(self.cancel_action, self.tableWidget_2, [self.pushButton_3, self.pushButton_5, self.pushButton_4]))
        self.pushButton_8.clicked.connect(partial(self.cancel_action, self.tableWidget_3, [self.pushButton_7, self.pushButton_9, self.pushButton_6]))
        self.pushButton_17.clicked.connect(partial(self.cancel_action, self.tableWidget_6, [self.pushButton_16, self.pushButton_18, self.pushButton_15]))
        self.pushButton_21.clicked.connect(partial(self.cancel_action, self.tableWidget_7, [self.pushButton_20, self.pushButton_22, self.pushButton_19]))
        self.pushButton_25.clicked.connect(partial(self.cancel_action, self.tableWidget_8, [self.pushButton_24, self.pushButton_26, self.pushButton_23]))

        # search by column with lineEdit 
        self.lineEdit_2.textChanged.connect(partial(self.seach_by_column, self.tableWidget_2, self.lineEdit_2))
        self.lineEdit_3.textChanged.connect(partial(self.seach_by_column, self.tableWidget_3, self.lineEdit_3))
        self.lineEdit_4.textChanged.connect(partial(self.seach_by_column, self.tableWidget_6, self.lineEdit_4))
        self.lineEdit_5.textChanged.connect(partial(self.seach_by_column, self.tableWidget_7, self.lineEdit_5))
        self.lineEdit_6.textChanged.connect(partial(self.seach_by_column, self.tableWidget_8, self.lineEdit_6))
        self.lineEdit_7.textChanged.connect(partial(self.seach_by_column, self.tableWidget, self.lineEdit_7))

        # filter column by modes
        self.comboBox_4.currentIndexChanged.connect(partial(self.sort_items_by_column, self.tableWidget_2, self.comboBox_4, 'Goods', None))
        self.comboBox_5.currentIndexChanged.connect(partial(self.sort_items_by_column, self.tableWidget_3, self.comboBox_5, 'Depots', None))
        self.comboBox_6.currentIndexChanged.connect(partial(self.sort_items_by_column, self.tableWidget_6, self.comboBox_6, 'Contractors', 'Покупатель'))
        self.comboBox_7.currentIndexChanged.connect(partial(self.sort_items_by_column, self.tableWidget_7, self.comboBox_7, 'Contractors', 'Поставщик'))
        self.comboBox_8.currentIndexChanged.connect(partial(self.sort_items_by_column, self.tableWidget_8, self.comboBox_8, 'Contractors', 'Подрядчик'))

        self.tableWidget_3.cellClicked.connect(partial(self.cell_cliked, self.tableWidget_3))

        self.tableWidget_3.itemChanged.connect(partial(self.cell_changed, self.tableWidget_3, self.pushButton_7))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def cell_cliked(self, widget):
        print(self.last_action)
        if 'edit_row' in self.last_action:
            row, col = int(list(self.last_action['edit_row'].keys())[-1].split(' ')[0]), int(list(self.last_action['edit_row'].keys())[-1].split(' ')[1]) 
            if f'{widget.currentRow()} {widget.currentColumn()}' not in self.last_action['edit_row']:
                self.last_text = widget.item(widget.currentRow(), widget.currentColumn()).text()
                widget.item(row, col).setFlags(widget.item(row, col).flags() & QtCore.Qt.ItemFlag.ItemIsEnabled)   
                
        else:
            self.last_text = widget.item(widget.currentRow(), widget.currentColumn()).text()
        
        if self.last_text not in self.suki:
            self.suki.append(self.last_text)
        

    def cell_changed(self, widget, button):
        if 'edit_row' in self.last_action:
            print(widget.currentItem().text(), self.last_text)
            if widget.currentItem().text() not in self.suki and widget.currentItem().text() != self.last_text:
                self.last_action['edit_row'][f'{widget.currentRow()} {widget.currentColumn()}'] = {'id': int(widget.item(widget.currentRow(), 0).text()),
                                                                                            'last_text': self.last_text}
        else:
            
            self.last_action = {'edit_row': 
                                    {f'{widget.currentRow()} {widget.currentColumn()}':
                                        {'id': int(widget.item(widget.currentRow(), 0).text()),
                                        'last_text': self.last_text}}}
                
        
        
        # widget.item(widget.currentRow(), widget.currentColumn()).setFlags(widget.item(widget.currentRow(), widget.currentColumn()).flags() & QtCore.Qt.ItemFlag.ItemIsEditable)
        print(self.last_action['edit_row'])
        button.setEnabled(True)                                
        

    def gen_order(self):
        counter = 15 # <- select max(number)+1 FROM Docs WHERE prefix = 'ПР'
        adress = self.textEdit.toPlainText()
        tel = self.lineEdit.text()
        client = self.comboBox.currentText()
        order_dict = {}
        order_list = []
        for i in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(i, self.tableWidget.columnCount() - 1).text() != '0':
                good_id = self.tableWidget.item(i,0).text()
                name = self.tableWidget.item(i, 1).text()
                price = self.tableWidget.item(i, 2).text()
                vendor_code = self.tableWidget.item(i, 4).text()
                mass = self.tableWidget.item(i, 5).text()
                amount = self.tableWidget.item(i, 13).text()
                order_list.append((good_id, vendor_code, amount)) # для дэйтабейзы?
                order_dict[name] = {'price': price, # для документов
                                    'vendor_code': vendor_code,
                                    'mass': mass,
                                    'amount': amount}
        edi_export(date=f'{time.localtime().tm_mday}.{time.localtime().tm_mon}.{time.localtime().tm_year} {time.localtime().tm_hour}-{time.localtime().tm_min}',
                   sender='ООО Рога и Копыта',
                   reciever=client,
                   number=str(counter+1),
                   goods=order_dict)

        # всё это в базу нахренячить #Андрей
        # и соответствующие документы посоздавать

        # cброс полей
        self.textEdit.clear()
        self.lineEdit.clear()
        self.comboBox.setCurrentText('')
        msgbox = QtWidgets.QMessageBox()
        msgbox.setText('Заказ создан')
        msgbox.about(MainWindow, 'Уведомление', 'Заказ создан')
        if self.comboBox_3.currentText():
            self.gen_table(self.tableWidget,'Goods', ['Depots', self.comboBox_3])
        else:
            self.gen_table(self.tableWidget)
        self.tabWidget.setCurrentIndex(4)  # перекид на список заказов


    def order_btn_switch(self):
        tel = self.lineEdit.text()
        adress = self.textEdit.toPlainText()
        client = self.comboBox.currentText()
        flag = False
        for i in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(i, self.tableWidget.columnCount()-1).text() != '0':
                flag = True
        if (len(tel) == 13 or (tel.isdigit() and len(tel) == 7)) \
                and len(adress) > 5 and flag and client:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)

    def sort_items_by_column(self, widget, combo, name, type):
        if combo.currentText() == 'По возрастанию':
            widget.sortByColumn(widget.currentColumn(), QtCore.Qt.AscendingOrder)
        elif combo.currentText() == 'По убыванию':
            widget.sortByColumn(widget.currentColumn(), QtCore.Qt.DescendingOrder)
        elif combo.currentText() == 'По умолчанию':
            self.gen_table(widget=widget, name=name, type=type)

    def seach_by_column(self, widget, lineEdit):
        column = widget.currentColumn()
        if column > 0:
            for row in range(widget.rowCount()):
                item = widget.item(row, column)
                match = lineEdit.text().lower() not in item.text().lower()
                if match:
                    widget.hideRow(row)
                else:
                    widget.showRow(row)

    def add_row(self, widget, buttons):
        widget.insertRow(widget.rowCount())
        if widget.rowCount() < 2:
            item = QtWidgets.QTableWidgetItem('1')
        else:
            item = QtWidgets.QTableWidgetItem(f'{int(widget.item(widget.rowCount()-2, 0).text())+1}')
        widget.setItem(widget.rowCount()-1, 0, QtWidgets.QTableWidgetItem(item))
        for b in buttons[1:]:
            b.setEnabled(False)
        buttons[0].setEnabled(True)
        self.last_action = {'add_row': widget.rowCount()-1}
        
    def del_row(self, widget, buttons):
        data = []
        for col in range(widget.columnCount()):
            it = widget.item(widget.currentRow(), col)
            text = it.text() if it is not None else ""
            data.append(text)
        self.last_action = {'del_row': {'row': widget.currentRow(), 'list': data, 'id': int(widget.item(widget.currentRow(), 0).text())}}
        widget.removeRow(widget.currentRow())
        for b in buttons[1:]:
            b.setEnabled(False)
        buttons[0].setEnabled(True)
          
    def save_table(self, widget, name, buttons):
        for b in buttons[1:]:
            b.setEnabled(True) 
        buttons[0].setEnabled(False)
        if 'add_row' in self.last_action:
            self.listy = tuple(widget.item(widget.rowCount()-1, col).text() for col in range(widget.columnCount()))
            db.insert(name=name, values=self.listy)
        elif 'del_row' in self.last_action:
            print(self.last_action['del_row']['row'], self.last_action['del_row']['id'])
            db.del_table_content_by_ids(name=name, ids=[self.last_action['del_row']['id']])
        elif 'edit_row' in self.last_action:
            columns = db.get_columns(name)
            
            for loc in self.last_action['edit_row'].keys():
                db.update_cell(name, self.last_action['edit_row'][loc]['id'], columns[int(loc.split(' ')[1])], 
                               widget.item(int(loc.split(' ')[0]), int(loc.split(' ')[1])).text())
        self.last_action = {}

    def cancel_action(self, widget, buttons):
        if self.last_action:
            if 'add_row' in self.last_action:
                widget.removeRow(self.last_action['add_row'])
            elif 'del_row' in self.last_action:
                widget.insertRow(self.last_action['del_row']['row'])
                for i in range(widget.columnCount()):
                    self.tableWidget_2.setItem(self.last_action['del_row']['row'], i, QtWidgets.QTableWidgetItem(self.last_action['del_row']['list'][i]))
            
            for b in buttons[1:]:
                b.setEnabled(True)
            buttons[0].setEnabled(False)
            self.last_action = {}

    def fill_comboBox(self, widget, name='Depots', id = 0):
        """
        filling comboBoxes with database content

        :param widget: comboBox to fill
        :param name: table form which cobmoBox will be filled
        :param id: index of tuple that is going to be an item in comboBox
        """
        items = db.get_table_by_name(name)
        if name == 'Contractors':
            widget.addItems([i[id] for i in items if i[-1] == 'Покупатель'])
        else:
            widget.addItems([i[id] for i in items])
        if name == 'Depots':
            widget.addItem('Все')

    def gen_table(self, widget, name = 'Goods', type = None):
        """
        Generating table with database content
        
        :param widget: tableWidget to generate
        :param name: table form which tableWidget will be generated
        :param type: special variable to generate tables with cobmoBoxes singals, can we list ['Depots', 'name of depot'] or string 'Подрядчик'
        """
        table_colums = db.get_rus_columns(name)
        if name == 'Goods':
            table_colums[3], table_colums[7] = 'название категории', 'название склада'
            table_items = db.get_fancy_goods(with_id=True) 
        else:
            table_items = db.get_table_by_name(name, with_id=True)
        # print(table_items)

        temp = []
        if type:
            if len(type)>2:
                temp = [p for p in table_items if p[-1] == type]
            elif type[0] == 'Depots' and type[1].currentText() == 'Все':
                temp = [d for d in table_items]
            elif type[0] == 'Depots':
                temp = [d for d in table_items if d[7] == type[1].currentText()]
            table_items = temp

        widget.setColumnCount(len(table_colums))
        widget.setHorizontalHeaderLabels(table_colums)
        widget.horizontalHeader().setDefaultSectionSize(150)
        widget.setRowCount(len(table_items))

        for row in range(widget.rowCount()):
            for col in range(widget.columnCount()):
                widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
                widget.setItem(row, col, QtWidgets.QTableWidgetItem(str(table_items[row][col])))

        if widget.objectName() == 'tableWidget':
            widget.insertColumn(widget.columnCount())
            widget.setHorizontalHeaderItem(widget.columnCount()-1, QtWidgets.QTableWidgetItem('Кол-во для заказа'))
            
            for row in range(widget.rowCount()):
                widget.setItem(row, widget.columnCount()-1, QtWidgets.QTableWidgetItem('0'))
        widget.setColumnHidden(0, True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Телефон"))
        self.label_11.setText(_translate("MainWindow", "Адрес"))
        self.label_12.setText(_translate("MainWindow", "Комментарий"))
        self.pushButton_2.setText(_translate("MainWindow", "Отменить"))
        self.pushButton_3.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_4.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_5.setText(_translate("MainWindow", "Удалить"))
        self.label_2.setText(_translate("MainWindow", "Товары"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.items), _translate("MainWindow", "Список товаров"))
        self.pushButton_6.setText(_translate("MainWindow", "Удалить"))
        self.label_3.setText(_translate("MainWindow", "Склады"))
        self.pushButton_7.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_8.setText(_translate("MainWindow", "Отменить"))
        self.pushButton_9.setText(_translate("MainWindow", "Добавить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.storages), _translate("MainWindow", "Список складов"))
        self.pushButton_18.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_15.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_17.setText(_translate("MainWindow", "Отменить"))
        self.pushButton_16.setText(_translate("MainWindow", "Сохранить"))
        self.label_6.setText(_translate("MainWindow", "Клиенты"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.clients), _translate("MainWindow", "Клиенты"))
        self.pushButton_19.setText(_translate("MainWindow", "Удалить"))
        self.label_7.setText(_translate("MainWindow", "Подставщики"))
        self.pushButton_20.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_21.setText(_translate("MainWindow", "Отменить"))
        self.pushButton_22.setText(_translate("MainWindow", "Добавить"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.suppliers), _translate("MainWindow", "Поставщики"))
        self.pushButton_23.setText(_translate("MainWindow", "Удалить"))
        self.label_8.setText(_translate("MainWindow", "Подрядчики"))
        self.pushButton_24.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_25.setText(_translate("MainWindow", "Отменить"))
        self.pushButton_26.setText(_translate("MainWindow", "Добавить"))    
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.contractors), _translate("MainWindow", "Подрядчики"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.people), _translate("MainWindow", "Контрагенты"))
        self.pushButton.setText(_translate("MainWindow", "Создать заказ"))
        self.label.setText(_translate("MainWindow", "Выбрать клиента"))
        self.comboBox.setPlaceholderText(_translate("MainWindow", "Выбрать клиента"))
        self.label_9.setText(_translate("MainWindow", "Создание заказа"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.create_order), _translate("MainWindow", "Создать заказ"))
        self.pushButton_10.setText(_translate("MainWindow", "Удалить"))
        self.label_4.setText(_translate("MainWindow", "Заказы"))
        self.pushButton_11.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_12.setText(_translate("MainWindow", "Редактировать"))
        self.pushButton_14.setText(_translate("MainWindow", "Отменить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.order_list), _translate("MainWindow", "Список заказов"))
        self.pushButton_13.setText(_translate("MainWindow", "Списать товар"))
        self.label_5.setText(_translate("MainWindow", "Остатки"))
        self.comboBox_2.setPlaceholderText(_translate("MainWindow", "Выбрать склад"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.remains), _translate("MainWindow", "Остатки"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupMainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
