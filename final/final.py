from PyQt5 import QtCore, QtGui, QtWidgets
import image1
import image2
import image3
import image4
import image5


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1258, 835)
        MainWindow.setStyleSheet("background-color: rgb(185, 255, 165);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(480, 350, 160, 22))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(3)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.butn1 = QtWidgets.QPushButton(self.centralwidget)
        self.butn1.setGeometry(QtCore.QRect(1070, 160, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.butn1.setFont(font)
        self.butn1.setStyleSheet("border-color: rgb(50, 88, 0);\n"
"background-color: white;\n"
"border-width: 4px;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(252, 162, 255);")
        self.butn1.setObjectName("butn1")
        self.butn2 = QtWidgets.QPushButton(self.centralwidget)
        self.butn2.setGeometry(QtCore.QRect(1070, 220, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.butn2.setFont(font)
        self.butn2.setStyleSheet("border-color: rgb(50, 88, 0);\n"
"background-color: white;\n"
"border-width: 4px;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(252, 162, 255);")
        self.butn2.setObjectName("butn2")
        self.butn3 = QtWidgets.QPushButton(self.centralwidget)
        self.butn3.setGeometry(QtCore.QRect(1070, 280, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.butn3.setFont(font)
        self.butn3.setStyleSheet("border-color: rgb(50, 88, 0);\n"
"background-color: white;\n"
"border-width: 4px;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(252, 162, 255);")
        self.butn3.setObjectName("butn3")
        self.butn_on = QtWidgets.QPushButton(self.centralwidget)
        self.butn_on.setGeometry(QtCore.QRect(40, 440, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.butn_on.setFont(font)
        self.butn_on.setStyleSheet("border-color: rgb(50, 88, 0);\n"
"background-color: white;\n"
"border-width: 4px;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(255, 117, 75);")
        self.butn_on.setObjectName("butn_on")
        self.butn_off = QtWidgets.QPushButton(self.centralwidget)
        self.butn_off.setGeometry(QtCore.QRect(210, 440, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.butn_off.setFont(font)
        self.butn_off.setStyleSheet("border-color: rgb(50, 88, 0);\n"
"background-color: white;\n"
"border-width: 4px;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(255, 117, 75);")
        self.butn_off.setObjectName("butn_off")
        self.butn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.butn_exit.setGeometry(QtCore.QRect(1110, 0, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.butn_exit.setFont(font)
        self.butn_exit.setStyleSheet("border-color: rgb(50, 88, 0);\n"
"background-color: white;\n"
"border-width: 4px;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(112, 169, 255);")
        self.butn_exit.setObjectName("butn_exit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 261, 221))
        self.label.setStyleSheet("image: url(:/logo/logo.png);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(810, 120, 261, 231))
        self.label_2.setStyleSheet("image: url(:/vend/vending machine_off.png);\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 120, 241, 211))
        self.label_3.setStyleSheet("image: url(:/water/facuet off.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 620, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-color: rgb(50, 88, 0);\n"
"background-color: white;\n"
"border-width: 4px;\n"
"border-radius: 10px;\n"
"")
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(930, 700, 91, 31))
        self.spinBox.setStyleSheet("background-color: white;\n"
"border-width: 4px;\n"
"border-style: solid;\n"
"")
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(3)
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setObjectName("spinBox")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(860, 440, 221, 221))
        self.label_6.setStyleSheet("image: url(:/sauna/sauna_off.jpg);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(470, 50, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-color: rgb(50, 88, 0);\n"
"background-color: white;\n"
"border-width: 4px;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 170, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(840, 60, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-color: rgb(50, 88, 0);\n"
"background-color: white;\n"
"border-width: 4px;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 170, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(500, 390, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-color: rgb(50, 88, 0);\n"
"background-color: white;\n"
"border-width: 4px;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 170, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(930, 390, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border-color: rgb(50, 88, 0);\n"
"background-color: white;\n"
"border-width: 4px;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 170, 255);")
        self.label_10.setObjectName("label_10")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(350, 460, 311, 151))
        self.lcdNumber.setStyleSheet("background-color: rgba( 255, 255, 255, 0%)")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setDigitCount(28)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 440, 531, 231))
        self.label_4.setStyleSheet("image: url(:/aircon/air_conditioner.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(530, 700, 101, 81))
        self.dial.setStyleSheet("background-color: rgb(193, 180, 255);")
        self.dial.setObjectName("dial")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(110, 690, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-color: rgb(50, 88, 0);\n"
"background-color: white;\n"
"border-width: 4px;\n"
"border-radius: 10px;\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 260, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border-color: rgb(50, 88, 0);\n"
"background-color: white;\n"
"border-width: 4px;\n"
"border-radius: 10px;\n"
"")
        self.label_12.setObjectName("label_12")
        self.label_4.raise_()
        self.horizontalSlider.raise_()
        self.butn1.raise_()
        self.butn2.raise_()
        self.butn3.raise_()
        self.butn_on.raise_()
        self.butn_off.raise_()
        self.butn_exit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.spinBox.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.lcdNumber.raise_()
        self.dial.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1258, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.butn_on.clicked.connect(self.on)
        self.butn_off.clicked.connect(self.off)
        self.butn1.clicked.connect(self.num1)
        self.butn2.clicked.connect(self.num2)
        self.butn3.clicked.connect(self.num3)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(2)
        self.dial.setMinimum(16)
        self.dial.setMaximum(28)
        self.horizontalSlider.valueChanged.connect(self.slide)
        self.dial.valueChanged.connect(self.roll)
        self.spinBox.valueChanged.connect(self.heat)
        self.butn_exit.clicked.connect(self.exit)
        self.lcdNumber.setDigitCount(28)
        self.display_label = QtWidgets.QLabel(self.centralwidget)
        self.display_label.setObjectName("display_label")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.butn1.setText(_translate("MainWindow", "Number 1"))
        self.butn2.setText(_translate("MainWindow", "Number 2"))
        self.butn3.setText(_translate("MainWindow", "Number 3"))
        self.butn_on.setText(_translate("MainWindow", "Start"))
        self.butn_off.setText(_translate("MainWindow", "STOP"))
        self.butn_exit.setText(_translate("MainWindow", "Exit"))
        self.label_5.setText(_translate("MainWindow", "Họ tên: Lê Hữu Ấn"))
        self.label_7.setText(_translate("MainWindow", "water pumping"))
        self.label_8.setText(_translate("MainWindow", "vending machine"))
        self.label_9.setText(_translate("MainWindow", "air conditioner"))
        self.label_10.setText(_translate("MainWindow", "Sauna"))
        self.label_11.setText(_translate("MainWindow", "MSSV: 21119367"))
        self.label_12.setText(_translate("MainWindow", "Project: Homework"))
    def on(self):
        self.label_2.setStyleSheet("image: url(:/vend/vending machine_on.png);")
        self.label_3.setStyleSheet("image: url(:/water/facuet off.png);") 
    def off(self):
        self.label_2.setStyleSheet("image: url(:/vend/vending machine_off.png);")
        self.label_3.setStyleSheet("image: url(:/water/facuet off.png);")
        self.lcdNumber.display(0)
        self.spinBox.setValue(0)
        self.label_6.setStyleSheet("image: url(:/sauna/sauna_off.jpg);")
    def num1(self):
        self.label_2.setStyleSheet("image: url(:/vend/vending machine_1.png);")
    def num2(self):
        self.label_2.setStyleSheet("image: url(:/vend/vending machine_2.png);")
    def num3(self):
        self.label_2.setStyleSheet("image: url(:/vend/vending machine_3.png);")
    def slide(self):
        pipe =self.horizontalSlider.value()
        if pipe ==0:
            self.label_3.setStyleSheet("image: url(:/water/facuet levl1.png);")
        if pipe ==1:
            self.label_3.setStyleSheet("image: url(:/water/facuet levl2.png);")
        if pipe ==2:
            self.label_3.setStyleSheet("image: url(:/water/facuet levl3.png);")
    def roll(self):
        air =self.dial.value()   
        self.lcdNumber.display(air)
    def heat(self):
        fire = self.spinBox.value()
        if fire==0:
            self.label_6.setStyleSheet("image: url(:/sauna/sauna_off.jpg);")
        if fire==1:
            self.label_6.setStyleSheet("image: url(:/sauna/sauna1.jpg);")
        if fire==2:
            self.label_6.setStyleSheet("image: url(:/sauna/sauna2.jpg);")   
        if fire==3:
            self.label_6.setStyleSheet("image: url(:/sauna/sauna3.jpg);")
    def exit(self):
        sys.exit(app.exec_())    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
