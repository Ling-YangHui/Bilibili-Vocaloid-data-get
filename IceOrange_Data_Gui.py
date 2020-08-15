import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.Qt import *
import tkinter as tk
from getVideoList import mainRun
import threading
from threading import Thread,Lock
import datetime


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(460, 10, 20, 571))
        self.line.setStyleSheet("*{color:rgb(200, 199, 197)}")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 421, 551))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(30, 130, 361, 380))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 380))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet("*{background-color:white;}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -90, 338, 470))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 470))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setKerning(True)
        self.scrollAreaWidgetContents.setFont(font)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.S1_LTY = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S1_LTY.setGeometry(QtCore.QRect(15, 10, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S1_LTY.setFont(font)
        self.S1_LTY.setObjectName("S1_LTY")
        self.S2_YZL = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S2_YZL.setGeometry(QtCore.QRect(15, 40, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S2_YZL.setFont(font)
        self.S2_YZL.setObjectName("S2_YZL")
        self.S3_YH = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S3_YH.setGeometry(QtCore.QRect(15, 70, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S3_YH.setFont(font)
        self.S3_YH.setObjectName("S3_YH")
        self.S4_MQX = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S4_MQX.setGeometry(QtCore.QRect(15, 100, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S4_MQX.setFont(font)
        self.S4_MQX.setObjectName("S4_MQX")
        self.S5_YZLY = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S5_YZLY.setGeometry(QtCore.QRect(15, 130, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S5_YZLY.setFont(font)
        self.S5_YZLY.setObjectName("S5_YZLY")
        self.S6_ZYMK = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S6_ZYMK.setGeometry(QtCore.QRect(15, 160, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S6_ZYMK.setFont(font)
        self.S6_ZYMK.setObjectName("S6_ZYMK")
        self.S7_XC = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S7_XC.setGeometry(QtCore.QRect(15, 190, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S7_XC.setFont(font)
        self.S7_XC.setObjectName("S7_XC")
        self.S8_XH = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S8_XH.setGeometry(QtCore.QRect(15, 220, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S8_XH.setFont(font)
        self.S8_XH.setObjectName("S8_XH")
        self.S9_CYWL = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S9_CYWL.setGeometry(QtCore.QRect(15, 250, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S9_CYWL.setFont(font)
        self.S9_CYWL.setObjectName("S9_CYWL")
        self.S10_HY = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S10_HY.setGeometry(QtCore.QRect(15, 280, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S10_HY.setFont(font)
        self.S10_HY.setObjectName("S10_HY")
        self.S12_SY = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S12_SY.setGeometry(QtCore.QRect(15, 340, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S12_SY.setFont(font)
        self.S12_SY.setObjectName("S12_SY")
        self.S11_CY = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S11_CY.setGeometry(QtCore.QRect(15, 310, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S11_CY.setFont(font)
        self.S11_CY.setObjectName("S11_CY")
        self.S13_CQ = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S13_CQ.setGeometry(QtCore.QRect(15, 370, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S13_CQ.setFont(font)
        self.S13_CQ.setObjectName("S13_CQ")
        self.S14_SynthV = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S14_SynthV.setGeometry(QtCore.QRect(15, 400, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S14_SynthV.setFont(font)
        self.S14_SynthV.setObjectName("S14_SynthV")
        self.S15_AK = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.S15_AK.setGeometry(QtCore.QRect(15, 430, 100, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.S15_AK.setFont(font)
        self.S15_AK.setObjectName("S15_AK")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.Synthesizercn = QtWidgets.QRadioButton(self.groupBox)
        self.Synthesizercn.setGeometry(QtCore.QRect(20, 54, 201, 40))
        self.Synthesizercn.setObjectName("Synthesizercn")
        self.VOCALOIDcn = QtWidgets.QRadioButton(self.groupBox)
        self.VOCALOIDcn.setGeometry(QtCore.QRect(20, 24, 150, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.VOCALOIDcn.setFont(font)
        self.VOCALOIDcn.setObjectName("VOCALOIDcn")
        self.SelfDefine = QtWidgets.QRadioButton(self.groupBox)
        self.SelfDefine.setGeometry(QtCore.QRect(20, 84, 115, 40))
        self.SelfDefine.setObjectName("SelfDefine")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(500, 20, 371, 211))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 80, 72, 21))
        self.label.setObjectName("label")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEdit_2.setGeometry(QtCore.QRect(20, 110, 171, 31))
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(self.endYear,self.endMonth,self.endDay), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_1 = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEdit_1.setGeometry(QtCore.QRect(20, 40, 171, 31))
        self.dateEdit_1.setDateTime(QtCore.QDateTime(QtCore.QDate(self.startYear,self.startMonth,self.startDay), QtCore.QTime(0, 0, 0)))
        self.dateEdit_1.setCalendarPopup(True)
        self.dateEdit_1.setObjectName("dateEdit_1")
        self.dateWarningLabel = QtWidgets.QLabel(self.groupBox_2)
        self.dateWarningLabel.setGeometry(QtCore.QRect(180, 80, 181, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        font.setWeight(50)
        self.dateWarningLabel.setFont(font)
        self.dateWarningLabel.setStyleSheet("color: red")
        self.dateWarningLabel.setObjectName("label_3")
        self.noLimitTime = QtWidgets.QCheckBox(self.groupBox_2)
        self.noLimitTime.setGeometry(QtCore.QRect(20, 170, 161, 19))
        self.noLimitTime.setObjectName("noLimitTime")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(500, 250, 371, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 331, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 72, 15))
        self.label_2.setObjectName("label_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(500, 370, 371, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.graphDrawing = QtWidgets.QCheckBox(self.groupBox_4)
        self.graphDrawing.setGeometry(QtCore.QRect(30, 30, 191, 31))
        self.graphDrawing.setObjectName("graphDrawing")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 60, 221, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(770, 490, 101, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setAutoFillBackground(True)
        self.commandLinkButton.setStyleSheet("font: 14pt \"宋体\" rgb(0, 0, 0);\n")
        self.commandLinkButton.setObjectName("commandLinkButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.VOCALOIDcn.toggled['bool'].connect(self.S15_AK.setDisabled)
        self.VOCALOIDcn.toggled['bool'].connect(self.S13_CQ.setDisabled)
        self.VOCALOIDcn.toggled['bool'].connect(self.S11_CY.setDisabled)
        self.VOCALOIDcn.toggled['bool'].connect(self.S9_CYWL.setDisabled)
        self.VOCALOIDcn.toggled['bool'].connect(self.S10_HY.setDisabled)
        self.VOCALOIDcn.toggled['bool'].connect(self.S1_LTY.setDisabled)
        self.VOCALOIDcn.toggled['bool'].connect(self.S4_MQX.setDisabled)
        self.VOCALOIDcn.toggled['bool'].connect(self.S12_SY.setDisabled)
        self.VOCALOIDcn.toggled['bool'].connect(self.S7_XC.setDisabled)
        self.VOCALOIDcn.toggled['bool'].connect(self.S6_ZYMK.setDisabled)
        self.VOCALOIDcn.toggled['bool'].connect(self.S5_YZLY.setDisabled)
        self.VOCALOIDcn.toggled['bool'].connect(self.S2_YZL.setDisabled)
        self.VOCALOIDcn.toggled['bool'].connect(self.S3_YH.setDisabled)
        self.VOCALOIDcn.toggled['bool'].connect(self.S8_XH.setDisabled)
        self.VOCALOIDcn.toggled['bool'].connect(self.S14_SynthV.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S10_HY.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S11_CY.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S12_SY.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S13_CQ.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S15_AK.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S1_LTY.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S2_YZL.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S3_YH.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S4_MQX.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S5_YZLY.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S6_ZYMK.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S7_XC.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S8_XH.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S9_CYWL.setDisabled)
        self.Synthesizercn.toggled['bool'].connect(self.S14_SynthV.setDisabled)

        #自定义按钮状态
        self.S1_LTY.setDisabled(True)
        self.S2_YZL.setDisabled(True)
        self.S3_YH.setDisabled(True)
        self.S4_MQX.setDisabled(True)
        self.S5_YZLY.setDisabled(True)
        self.S6_ZYMK.setDisabled(True)
        self.S7_XC.setDisabled(True)
        self.S8_XH.setDisabled(True)
        self.S9_CYWL.setDisabled(True)
        self.S10_HY.setDisabled(True)
        self.S11_CY.setDisabled(True)
        self.S12_SY.setDisabled(True)
        self.S13_CQ.setDisabled(True)
        self.S14_SynthV.setDisabled(True)
        self.S15_AK.setDisabled(True)

        #自定义事件触发部分
        self.SelfDefine.toggled['bool'].connect(self.S1_LTY.setEnabled)
        self.SelfDefine.toggled['bool'].connect(self.S2_YZL.setEnabled)
        self.SelfDefine.toggled['bool'].connect(self.S3_YH.setEnabled)
        self.SelfDefine.toggled['bool'].connect(self.S4_MQX.setEnabled)
        self.SelfDefine.toggled['bool'].connect(self.S5_YZLY.setEnabled)
        self.SelfDefine.toggled['bool'].connect(self.S6_ZYMK.setEnabled)
        self.SelfDefine.toggled['bool'].connect(self.S7_XC.setEnabled)
        self.SelfDefine.toggled['bool'].connect(self.S8_XH.setEnabled)
        self.SelfDefine.toggled['bool'].connect(self.S9_CYWL.setEnabled)
        self.SelfDefine.toggled['bool'].connect(self.S10_HY.setEnabled)
        self.SelfDefine.toggled['bool'].connect(self.S11_CY.setEnabled)
        self.SelfDefine.toggled['bool'].connect(self.S12_SY.setEnabled)
        self.SelfDefine.toggled['bool'].connect(self.S13_CQ.setEnabled)
        self.SelfDefine.toggled['bool'].connect(self.S14_SynthV.setEnabled)
        self.SelfDefine.toggled['bool'].connect(self.S15_AK.setEnabled)

        self.commandLinkButton.clicked.connect(lambda:self.run())
        self.VOCALOIDcn.toggled['bool'].connect(lambda:self.addKeyword(-1))
        self.Synthesizercn.toggled['bool'].connect(lambda:self.addKeyword(-2))
        self.SelfDefine.toggled['bool'].connect(lambda:self.addKeyword(0))
        self.S1_LTY.toggled['bool'].connect(lambda:self.addKeyword(1))
        self.S2_YZL.toggled['bool'].connect(lambda:self.addKeyword(2))
        self.S3_YH.toggled['bool'].connect(lambda:self.addKeyword(3))
        self.S4_MQX.toggled['bool'].connect(lambda:self.addKeyword(4))
        self.S5_YZLY.toggled['bool'].connect(lambda:self.addKeyword(5))
        self.S6_ZYMK.toggled['bool'].connect(lambda:self.addKeyword(6))
        self.S7_XC.toggled['bool'].connect(lambda:self.addKeyword(7))
        self.S8_XH.toggled['bool'].connect(lambda:self.addKeyword(8))
        self.S9_CYWL.toggled['bool'].connect(lambda:self.addKeyword(9))
        self.S10_HY.toggled['bool'].connect(lambda:self.addKeyword(10))
        self.S11_CY.toggled['bool'].connect(lambda:self.addKeyword(11))
        self.S12_SY.toggled['bool'].connect(lambda:self.addKeyword(12))
        self.S13_CQ.toggled['bool'].connect(lambda:self.addKeyword(13))
        self.S14_SynthV.toggled['bool'].connect(lambda:self.addKeyword(14))
        self.S15_AK.toggled['bool'].connect(lambda:self.addKeyword(15))

        self.dateEdit_1.dateChanged.connect(lambda:self.setTime(1))
        self.dateEdit_2.dateChanged.connect(lambda:self.setTime(2))
        self.noLimitTime.toggled['bool'].connect(lambda:self.changeTimeLimit())

        self.graphDrawing.toggled['bool'].connect(lambda:self.setDrawGraph())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "冰数据"))
        self.groupBox.setTitle(_translate("MainWindow", "模式"))
        self.S1_LTY.setText(_translate("MainWindow", "洛天依"))
        self.S2_YZL.setText(_translate("MainWindow", "乐正绫"))
        self.S3_YH.setText(_translate("MainWindow", "言和"))
        self.S4_MQX.setText(_translate("MainWindow", "墨清弦"))
        self.S5_YZLY.setText(_translate("MainWindow", "乐正龙牙"))
        self.S6_ZYMK.setText(_translate("MainWindow", "徵羽摩柯"))
        self.S7_XC.setText(_translate("MainWindow", "星尘"))
        self.S8_XH.setText(_translate("MainWindow", "心华"))
        self.S9_CYWL.setText(_translate("MainWindow", "初音未来"))
        self.S10_HY.setText(_translate("MainWindow", "海伊"))
        self.S11_CY.setText(_translate("MainWindow", "赤羽"))
        self.S12_SY.setText(_translate("MainWindow", "诗岸"))
        self.S13_CQ.setText(_translate("MainWindow", "苍穹"))
        self.S14_SynthV.setText(_translate("MainWindow", "SynthV"))
        self.S15_AK.setText(_translate("MainWindow", "艾可"))
        self.Synthesizercn.setText(_translate("MainWindow", "Synthesizer V中文曲"))
        self.VOCALOIDcn.setText(_translate("MainWindow", "VOCALOID中文曲"))
        self.SelfDefine.setText(_translate("MainWindow", "自定义"))
        self.groupBox_2.setTitle(_translate("MainWindow", "时间限制"))
        self.label.setText(_translate("MainWindow", "至"))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "yyyy年  M月d日"))
        self.dateEdit_1.setDisplayFormat(_translate("MainWindow", "yyyy年  M月d日"))
        self.dateWarningLabel.setText(_translate("MainWindow", "起始时间不能晚于结束时间"))
        self.noLimitTime.setText(_translate("MainWindow", "时间不限"))
        self.groupBox_3.setTitle(_translate("MainWindow", "输出"))
        self.label_2.setText(_translate("MainWindow", "输出目录"))
        self.groupBox_4.setTitle(_translate("MainWindow", "选项"))
        self.graphDrawing.setText(_translate("MainWindow", "绘制分布图"))
        self.checkBox_2.setText(_translate("MainWindow", "仅限VOCALOID-UTAU分区"))
        self.commandLinkButton.setText(_translate("MainWindow", "运行"))
        
        self.dateWarningLabel.close()

    def __init__(self):
        super().__init__()
        self.Run = mainRun() #运行函数类
        self.keywordList = [] #传入的名单
        self.keyword = ['','洛天依','乐正绫','言和','墨清弦','乐正龙牙','徵羽摩柯','星尘','心华','初音未来','海伊','赤羽','诗岸','苍穹','SynthV','艾可']
        self.VCN = ['洛天依','乐正绫','言和','墨清弦','乐正龙牙','徵羽摩柯','星尘','心华','初音未来']
        self.SCN = ['海伊','赤羽','诗岸','苍穹','SynthV','艾可']#添加牧心
        #星尘Minus的算法问题待议，根据萌娘百科、VC周刊、SV周刊的做法
        self.chosenList = [] #选择列表
        for i in range (16):
            self.chosenList.append(False)
        self.nowState = 0 #当前选择状态 【-1：VCN；-2：SCN；0：SDF】

        self.endYear = int(datetime.datetime.now().strftime('%Y'))
        self.endMonth = int(datetime.datetime.now().strftime('%m'))
        self.endDay = int(datetime.datetime.now().strftime('%d'))
        self.endDate = datetime.datetime.now().strftime('%Y%m%d')
        startDate = datetime.datetime.now() + datetime.timedelta(days=-31)
        self.startYear = int(startDate.strftime('%Y'))
        self.startMonth = int(startDate.strftime('%m'))
        self.startDay = int(startDate.strftime('%d'))
        self.startDate = startDate.strftime('%Y%m%d')
        self.endDateCache = self.endDate
        self.startDateCache = self.startDate
        self.isNoLimit = 0

        self.isDateWarning = 0
        self.drawGraph = 0

    def showNoKeywordWarning(self,saying,head):
        warningBox = QMessageBox(QMessageBox.Critical, head, saying,QMessageBox.NoButton,self.centralwidget)
        button = warningBox.addButton('好吧',QMessageBox.YesRole)
        warningBox.setIcon(1)
        warningBox.setGeometry(900,500,0,0)
        warningBox.show()
        button.clicked.connect(warningBox.close)

    def showProgressWindow(self):
        self.progressWin = QProgressDialog(self.centralwidget)
        self.progressWin.setWindowModality(Qt.ApplicationModal)
        self.progressWin.setMinimum(0)
        self.progressWin.setMaximum(100)
        self.progressWin.setGeometry(900,450,300,120)
        self.progressWin.setStyleSheet('font: 10pt \"宋体\" rgb(0,0,0)')
        self.progressWin.show()

    def changeProgressWindow(self,mode,num,keyword,percent):
        if mode == 0:
            self.progressWin.setWindowTitle('正在处理中' + str(num) + '/' + str(self.keywordList.__len__()))
            self.progressWin.setLabelText(keyword)
            self.progressWin.setValue(0)
        elif mode == 1:
            self.progressWin.setValue(percent)

    def addKeyword(self,num):
        if num == -1:
            if self.nowState != -1:
                self.keywordList.clear()
                for word in self.VCN:
                    self.keywordList.append(word)
                self.nowState = -1
        elif num == -2:
            if self.nowState != -2:
                self.keywordList.clear()
                self.isSelfDefine = 0
                for word in self.SCN:
                    self.keywordList.append(word)
                self.nowState = -2
        elif num == 0:
            if self.nowState != 0:
                self.keywordList.clear()
                self.nowState = 0
        else:
            if self.chosenList[num] == False:
                self.chosenList[num] = True
            else:
                self.chosenList[num] = False
    
    def setTime(self,num):
        if num == 1:
            qdate = self.dateEdit_1.dateTime()
            self.startDate = qdate.toString('yyyyMMdd')
            self.startDateCache = self.startDate
        elif num == 2:
            qdate = self.dateEdit_2.dateTime()
            self.endDate = qdate.toString('yyyyMMdd')
            self.endDateCache = self.endDate
        if int(self.endDate) < int(self.startDate) and self.isDateWarning == 0:
            self.isDateWarning = 1
            self.dateWarningLabel.show()
        elif int(self.endDate) > int(self.startDate) and self.isDateWarning == 1:
            self.dateWarningLabel.close()

    def changeTimeLimit(self):
        if self.isNoLimit == 0:
            self.dateEdit_1.setDisabled(True)
            self.dateEdit_2.setDisabled(True)
            self.startDate = '19990101'
            self.endDate = '20260826'
            self.isNoLimit = 1
        else:
            self.dateEdit_1.setEnabled(True)
            self.dateEdit_2.setEnabled(True)
            self.startDate = self.startDateCache
            self.endDate = self.endDateCache
            self.isNoLimit = 0

    def setDrawGraph(self):
        if self.drawGraph == 0:
            self.drawGraph = 1
        else:
            self.drawGraph = 0
        
    def run(self):
        if int(self.startDate) > int(self.endDate):
            self.showNoKeywordWarning("<p>起始时间不能晚于截至时间</p>","请不要这样做")
            return
        if self.nowState != 0:
            self.Run.main(self.keywordList,self.startDate,self.endDate,self.drawGraph,self,True)
        else:
            for i in range(self.chosenList.__len__()):
                if self.chosenList[i] == True:
                    self.keywordList.append(self.keyword[i])
            if self.keywordList.__len__() == 0:
                self.showNoKeywordWarning("<p>没有选中任何的关键字</p><p>这样做可能会导致程序崩溃</p>","请不要这样做")
                return
            self.Run.main(self.keywordList,self.startDate,self.endDate,self.drawGraph,self,True)
        self.keywordList.clear()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())