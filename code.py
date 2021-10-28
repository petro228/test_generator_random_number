from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import random
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ДОСЛІДЖЕННЯ ГЕНЕРАТОРІВ ВИПАДКОВИХ ЧИСЕЛ")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 331, 211))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 171, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 131, 16))
        self.label_3.setObjectName("label_3")
        self.adapt_const_Edit = QtWidgets.QLineEdit(self.groupBox)
        self.adapt_const_Edit.setGeometry(QtCore.QRect(200, 40, 113, 22))
        self.adapt_const_Edit.setObjectName("adapt_const_Edit")
        self.mult_const_Edit = QtWidgets.QLineEdit(self.groupBox)
        self.mult_const_Edit.setGeometry(QtCore.QRect(200, 80, 113, 22))
        self.mult_const_Edit.setObjectName("mult_const_Edit")
        self.bit_Edit = QtWidgets.QLineEdit(self.groupBox)
        self.bit_Edit.setGeometry(QtCore.QRect(200, 120, 113, 22))
        self.bit_Edit.setObjectName("bit_Edit")
        self.defolt_btn = QtWidgets.QPushButton(self.groupBox)
        self.defolt_btn.setGeometry(QtCore.QRect(30, 170, 251, 28))
        self.defolt_btn.setObjectName("defolt_btn")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 230, 331, 311))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(15, 21, 301, 271))
        self.textBrowser.setObjectName("textBrowser")
        self.MplWidget = PlotWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(389, 269, 381, 261))
        self.MplWidget.setObjectName("MplWidget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 20, 171, 211))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 151, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.go_test_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.go_test_btn.setObjectName("go_test_btn")
        self.verticalLayout.addWidget(self.go_test_btn)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(600, 20, 171, 201))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 151, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.obsag_Edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.obsag_Edit.setObjectName("obsag_Edit")
        self.verticalLayout_3.addWidget(self.obsag_Edit)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.interval_Edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.interval_Edit.setObjectName("interval_Edit")
        self.verticalLayout_3.addWidget(self.interval_Edit)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 240, 151, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        grid = QtWidgets.QGridLayout(self.centralwidget)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.test()
        self.checkBox_fanc()
        self.checkBox_fanc_2()
        self.defolt_btn_func()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ДОСЛІДЖЕННЯ ГЕНЕРАТОРІВ ВИПАДКОВИХ ЧИСЕЛ"))
        self.groupBox.setTitle(_translate("MainWindow", "Налаштування генератора "))
        self.label.setText(_translate("MainWindow", "Адитивна константа "))
        self.label_2.setText(_translate("MainWindow", "Мультплікативна константа "))
        self.label_3.setText(_translate("MainWindow", "Кількість біт у масці"))
        self.defolt_btn.setText(_translate("MainWindow", "Повернути стандартні константи"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Результати тесту"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Тести"))
        self.checkBox.setText(_translate("MainWindow", "На період"))
        self.checkBox_2.setText(_translate("MainWindow", "На рівномірність"))
        self.go_test_btn.setText(_translate("MainWindow", "Виконатити тест"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Налаштування тестів"))
        self.label_5.setText(_translate("MainWindow", "Обсяг вибірки"))
        self.label_6.setText(_translate("MainWindow", "Відступ від початку"))
        self.label_4.setText(_translate("MainWindow", "Графічне приставленя"))
        self.checkBox.setChecked(True)
        self.MplWidget.setBackground("w")
        self.adapt_const_Edit.setText("9")
        self.mult_const_Edit.setText("13")
        self.bit_Edit.setText("31")
        self.obsag_Edit.setText("100")
        self.interval_Edit.setText("10")


    def defolt_btn_func(self):
        self.defolt_btn.clicked.connect(lambda: self.btn())

    def btn(self):
        self.adapt_const_Edit.setText("11")
        self.mult_const_Edit.setText("25214903917")
        self.bit_Edit.setText("8")
        self.obsag_Edit.setText("100")
        self.interval_Edit.setText("10")
    def plot(self, x, y):

        self.MplWidget.plot(x, y,clear=True,stepMode=True, fillLevel=0, brush=(0,0,255,150))

    def checkBox_fanc(self):
        self.checkBox.clicked.connect(lambda: self.checkBox_())

    def checkBox_fanc_2(self):
        self.checkBox_2.clicked.connect(lambda: self.checkBox__())

    def checkBox_(self):
        self.checkBox.setChecked(True)
        self.checkBox_2.setChecked(False)
        self.label_6.setText("Відступ від початку")
    def checkBox__(self):
        self.checkBox_2.setChecked(True)
        self.checkBox.setChecked(False)
        self.label_6.setText("Кількість інтервалів")
    def test(self):
        self.go_test_btn.clicked.connect(lambda: self.run_test())


    def run_test(self):
        self.textBrowser.clear()

        try:
            adut_const = int(self.adapt_const_Edit.text())
            mult_const = int(self.mult_const_Edit.text())
            bit = int(self.bit_Edit.text())
            vubirka = int(self.obsag_Edit.text())
            vilna_zaminna=int(self.interval_Edit.text())
        except ValueError:
            self.textBrowser.append("Error")
            raise
        i=0

        random_namder=[]
        rand=random.randint(0,99)
        while i<vubirka:
            rand=(adut_const+(mult_const*rand))%bit
            random_namder.append(rand/bit)
            self.textBrowser.append(str(random_namder[i]))
            i+=1
        if self.checkBox.isChecked():
            i=vilna_zaminna+1

            while i <vubirka-1:
                if random_namder[vilna_zaminna]==random_namder[i]:
                    break
                i+=1
            self.textBrowser.append("Період послідовності="+str(i-vilna_zaminna))
        else:
            interval = []
            interval.append(0)
            interval.append(round(1/vilna_zaminna,3))
            i=1
            while i<vilna_zaminna:
                interval.append(round(interval[1] + interval[i],3))
                i+=1
            i=0
            j=0
            t=0
            inretval_kilkist = []
            while j<vilna_zaminna:
                while i < vubirka-1:
                    if interval[j]<random_namder[i]<interval[j+1]:
                        t+=1
                    i+=1
                i=0
                inretval_kilkist.append(t)
                t=0
                j+=1

            self.plot(interval, inretval_kilkist)
            #новий метод підрахунку мат.спот і дисперсії
            killk = []
            unic_number = []
            unic_number.append(random_namder[0])
            i=0
            j=0
            t=0
            while i<vubirka:
                while j<len(unic_number):
                    if random_namder[i]!=unic_number[j]:
                        t+=1
                    j+=1
                if t==len(unic_number):
                    unic_number.append(random_namder[i])
                t=0
                j=0
                i+=1
            i = 0
            j = 0
            t = 0
            while i < len(unic_number):
                while j < vubirka:
                    if random_namder[j]==unic_number[i]:
                        t+=1
                    j+=1
                j=0
                i+=1
                killk.append(t)
                t=0

            mat_spod = 0
            mat_spod2 = 0
            i = 0
            while i < len(unic_number):
                mat_spod += unic_number[i] * (killk[i] / vubirka)
                mat_spod2 += (killk[i] / vubirka) * unic_number[i] ** 2
                i = i + 1
            despersia = mat_spod2 - mat_spod ** 2
            #print("Математичне сподівання:", mat_spod)
            #print("Дисперсія:", despersia)
            self.textBrowser.append("Математичне сподівання:" + str(mat_spod))
            self.textBrowser.append("Дисперсія:" + str(despersia))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())







