# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mainWindow.ui'
##
# Created by: Qt User Interface Compiler version 6.5.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QTime, Qt, SIGNAL)
from PySide6.QtGui import (QShortcut, QKeySequence)
from PySide6.QtWidgets import (QCheckBox, QDoubleSpinBox, QFrame,
                               QLCDNumber, QLabel, QLineEdit, QListWidget,
                               QListWidgetItem, QProgressBar, QPushButton, QStatusBar, QTimeEdit,
                               QToolButton, QWidget)

from functions import *


class Ui_MainWindow(object):

    data = {}
    t = 0

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 231, 256, 341))
        self.listWidget.itemSelectionChanged.connect(self.makeEditable)
        delete = QShortcut(QKeySequence(Qt.Key_Delete), self.listWidget)
        delete.connect(SIGNAL("activated()"), self.delCurrent)
        down = QShortcut(QKeySequence("Alt+Down"), self.listWidget)
        up = QShortcut(QKeySequence("Alt+Up"), self.listWidget)
        down.connect(SIGNAL("activated()"), self.goDown)
        up.connect(SIGNAL("activated()"), self.goUp)
        self.listWidget_2 = QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(535, 230, 241, 341))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(660, 90, 113, 21))
        self.doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(500, 90, 62, 22))
        self.doubleSpinBox.setMinimum(float("-inf"))
        self.doubleSpinBox.setMaximum(float("inf"))
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox_2 = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setGeometry(QRect(580, 90, 62, 22))
        self.doubleSpinBox_2.setMinimum(float("-inf"))
        self.doubleSpinBox_2.setMaximum(float("inf"))
        self.doubleSpinBox_2.setDecimals(0)
        self.doubleSpinBox_3 = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox_3.setGeometry(QRect(70, 90, 70, 22))
        self.doubleSpinBox_3.setMinimum(float("-inf"))
        self.doubleSpinBox_3.setMaximum(float("inf"))
        self.timeEdit = QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(360, 90, 118, 22))
        self.timeEdit.setDisplayFormat("HH:mm:ss")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(260, 90, 75, 20))
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(170, 90, 75, 20))
        self.checkBox_2.toggled.connect(
            lambda checked: checked and self.checkBox.setCheckState(Qt.Unchecked))
        self.checkBox.toggled.connect(
            lambda checked: checked and self.checkBox_2.setCheckState(Qt.Unchecked))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 130, 75, 24))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 130, 75, 24))
        self.pushButton_2.hide()
        self.pushButton_2.clicked.connect(self.edit)
        self.pushButton.clicked.connect(self.get)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(710, 70, 61, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(590, 70, 49, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(510, 70, 49, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(420, 70, 49, 16))
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(380, 340, 64, 23))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(360, 410, 118, 23))
        self.progressBar.setValue(0)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 200, 781, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(40, 10, 21, 22))
        self.toolButton.clicked.connect(self.execute)
        self.toolButton_2 = QToolButton(self.centralwidget)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(80, 10, 21, 22))
        self.toolButton_2.clicked.connect(self.Off)
        self.toolButton_3 = QToolButton(self.centralwidget)
        self.toolButton_3.clicked.connect(self.miniMax)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setGeometry(QRect(60, 10, 21, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.checkBox.setText(QCoreApplication.translate(
            "MainWindow", u"\u0641\u0631\u0648\u0634", None))
        self.checkBox_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u062e\u0631\u06cc\u062f", None))
        self.pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"\u0627\u0631\u0633\u0627\u0644", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u0627\u062f\u06cc\u062a", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"\u0646\u0645\u0627\u062f \u0633\u0647\u0627\u0645", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u062a\u0639\u062f\u0627\u062f", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"\u0642\u06cc\u0645\u062a", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"\u0632\u0645\u0627\u0646", None))
        self.toolButton.setText(
            QCoreApplication.translate("MainWindow", u"On", None))
        self.toolButton_2.setText(
            QCoreApplication.translate("MainWindow", u"Off", None))
        self.toolButton_3.setText(
            QCoreApplication.translate("MainWindow", u"||", None))

    def get(self):
        self.listWidget_2.clear()
        text = self.lineEdit.text()
        count = self.doubleSpinBox_2.cleanText()
        price = self.doubleSpinBox.cleanText()
        time = self.timeEdit.time()
        buy = self.checkBox_2.isChecked()
        sell = self.checkBox.isChecked()
        buyOrsell = None
        if buy:
            buyOrsell = 1
            self.checkBox_2.setCheckState(Qt.Unchecked)
        elif sell:
            buyOrsell = 0
            self.checkBox.setCheckState(Qt.Unchecked)
        self.lineEdit.clear()
        self.doubleSpinBox.clear()
        self.doubleSpinBox_2.clear()
        self.timeEdit.setTime(QTime(0, 0))
        self.t = self.doubleSpinBox_3.cleanText()
        self.listWidget.addItem("{}: {}".format(
            text, (int(count), int(price), time.toString(), buyOrsell)))
        self.data[text] = [count, price, time.toString(), buyOrsell]
        self.lcdNumber.display(len(self.data.keys()))

    def makeEditable(self):
        self.pushButton_2.show()
        self.pushButton.hide()
        index = self.listWidget.row(self.listWidget.currentItem())
        self.key = list(self.data.keys())[index]
        self.value = list(self.data.values())[index]
        self.value[2] = self.value[2].strip("''")
        self.lineEdit.setText(self.key)
        self.doubleSpinBox_2.setValue(int(self.value[0]))
        self.doubleSpinBox.setValue(int(self.value[1]))
        self.timeEdit.setTime(QTime(int(self.value[2][0]+self.value[2][1]), int(self.value[2][3]+self.value[2][4]), int(self.value[2][6]+self.value[2][7])))
        if int(self.value[3]) == 1:
            self.checkBox_2.setCheckState(Qt.Checked)
        elif int(self.value[3]) == 0:
            self.checkBox.setCheckState(Qt.Checked)

    def edit(self):
        text = self.lineEdit.text()
        count = self.doubleSpinBox_2.cleanText()
        price = self.doubleSpinBox.cleanText()
        time = self.timeEdit.time()
        buy = self.checkBox_2.isChecked()
        sell = self.checkBox.isChecked()
        buyOrsell = None
        if buy:
            buyOrsell = 1
            self.checkBox_2.setCheckState(Qt.Unchecked)
        elif sell:
            buyOrsell = 0
            self.checkBox.setCheckState(Qt.Unchecked)
        self.lineEdit.clear()
        self.doubleSpinBox.clear()
        self.doubleSpinBox_2.clear()
        self.timeEdit.setTime(QTime(0, 0))
        self.t = self.doubleSpinBox_3.cleanText()
        index = self.listWidget.row(self.listWidget.currentItem())
        self.listWidget.takeItem(index)
        self.listWidget.clearSelection()
        item = QListWidgetItem("{}: {}".format(
            text, (int(count), int(price), time.toString(), buyOrsell)))
        self.listWidget.insertItem(index, item)
        self.data[text] = [count, price, time.toString(), buyOrsell]
        self.pushButton.show()
        self.pushButton_2.hide()
        self.lineEdit.clear()
        self.doubleSpinBox.clear()
        self.doubleSpinBox_2.clear()
        self.timeEdit.setTime(QTime(0, 0))
        self.t = self.doubleSpinBox_3.cleanText()
        
    def execute(self):

        done = 0
        num = len(self.data.keys())
        url = 'https://silver.spshayan.ir/Account/Login'
        self.session = createSession(url)
        session = self.session
        wait(session, url, "https://silver.spshayan.ir/Home/Default/page-1")
        versionDialogCloser(session)

        # stocks = stockInfoGetter()

        for stock in self.data.items():

            done += 1
            searchStock(session, stock[0])
            details = stock[1]
            sleep(1)
            error = checkOrderable(session)
            if error == 1:
                self.listWidget_2.addItem("{} ممنوع، متوقف است".format(stock[0]))
            else:
                if details[2] == "00:00:00":
                    sleep(float(self.t))
                else:
                    print(details[2])
                    executionWait(details[2])
                if details[3] == 1:
                    selectBuy(session)
                else:
                    selectSell(session)
                stockCount(session, int(details[1]))
                sleep(0.5)
                stockPrice(session, int(details[0]))
                sleep(0.5)
                sendOrder(session)
                sleep(0.5)
                orderConfirmation(session)
                self.listWidget_2.addItem("سفارش {} با موفقیت انجام شد".format(stock[0]))
                self.progressBar.setValue((done/num)*100)
            self.lcdNumber.display(num)
            resetSession(session)
            selectBuy(session)
            resetSearch(session)
        self.data= {}
        self.t = 0
        self.listWidget.clear()

    def Off(self):
        self.session.quit()
        self.data= {}
        self.t = 0
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.progressBar.setValue(0)
        self.lcdNumber.display(0)
    
    def miniMax(self):
        is_maximized = self.session.get_window_position()['x'] == 0
        if is_maximized:
            self.session.minimize_window()
        else:
            self.session.maximize_window()

    def goDown(self):
        rowno = self.listWidget.currentRow()
        val = self.listWidget.takeItem(rowno)
        if val:
            self.listWidget.insertItem(rowno+1, val.text())
            self.listWidget.setCurrentRow(rowno+1)
        self.listWidget.clearSelection()
        items = self.getAll()
        self.pushButton.show()
        self.pushButton_2.hide()
        self.data = {}
        for i in range(len(items)):
            self.data[items[i][0]] = items[i][1].strip('"()"').split(', ')

    def goUp(self):
        rowno = self.listWidget.currentRow()
        val = self.listWidget.takeItem(
            self.listWidget.currentRow())
        if val:
            self.listWidget.insertItem(rowno-1, val.text())
            self.listWidget.setCurrentRow(rowno-1)
        self.listWidget.clearSelection()
        items = self.getAll()
        self.pushButton.show()
        self.pushButton_2.hide()
        self.data = {}
        for i in range(len(items)):
            self.data[items[i][0]] = items[i][1].strip('"()"').split(', ')
        print(self.data)

    def delCurrent(self):
        self.listWidget.takeItem(
            self.listWidget.currentRow())
        index = self.listWidget.row(self.listWidget.currentItem())
        key = self.data.keys()[index]
        self.data.pop(key)
        self.listWidget.clearSelection()
        self.pushButton.show()
        self.pushButton_2.hide()
        print(self.data)

    def getAll(self):
        items = []
        for x in range(self.listWidget.count()):
            items.append(self.listWidget.item(x).text().split(": "))
        return items
    # retranslateUi
