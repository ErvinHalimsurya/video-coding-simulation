# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyle
from PyQt5.QtCore import QSize,Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
       
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1378, 866)
        btnSize = QSize(16, 16)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.encodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.encodeButton.setGeometry(QtCore.QRect(540, 560, 141, 71))
        self.encodeButton.setFlat(False)
        self.encodeButton.setEnabled(True)
        self.encodeButton.setObjectName("encodeButton")

        self.videoScreen1 = QVideoWidget(self.centralwidget)
        self.videoScreen1.setGeometry(QtCore.QRect(20, 190, 651, 331))
        self.videoScreen1.setObjectName("videoScreen1")
        self.videoScreen2 = QVideoWidget(self.centralwidget)
        self.videoScreen2.setGeometry(QtCore.QRect(730, 190, 621, 331))
        self.videoScreen2.setObjectName("videoScreen2")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(870, 0, 481, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.sourceInput = QtWidgets.QLineEdit(self.frame)
        self.sourceInput.setObjectName("sourceInput")
        self.horizontalLayout.addWidget(self.sourceInput)
        self.browseButton1 = QtWidgets.QPushButton(self.frame)
        self.browseButton1.setObjectName("browseButton1")
        self.horizontalLayout.addWidget(self.browseButton1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.DestInput = QtWidgets.QLineEdit(self.frame)
        self.DestInput.setObjectName("DestInput")
        self.horizontalLayout_2.addWidget(self.DestInput)
        self.browseButton2 = QtWidgets.QPushButton(self.frame)
        self.browseButton2.setObjectName("browseButton2")
        self.horizontalLayout_2.addWidget(self.browseButton2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.outputName = QtWidgets.QLineEdit(self.frame)
        self.outputName.setObjectName("outputName")
        self.horizontalLayout_3.addWidget(self.outputName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.decodedPathInput = QtWidgets.QLineEdit(self.frame)
        self.decodedPathInput.setObjectName("decodedPathInput")
        self.horizontalLayout_4.addWidget(self.decodedPathInput)
        self.browseButton3 = QtWidgets.QPushButton(self.frame)
        self.browseButton3.setObjectName("browseButton3")
        self.horizontalLayout_4.addWidget(self.browseButton3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.decodedName = QtWidgets.QLineEdit(self.frame)
        self.decodedName.setObjectName("decodedName")
        self.horizontalLayout_5.addWidget(self.decodedName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 660, 621, 151))
        self.textBrowser.setObjectName("textBrowser")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 261, 111))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 237, 100))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)

        self.playButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.playButton1.setGeometry(QtCore.QRect(290, 530, 93, 28))
        self.playButton1.setEnabled(False)
        self.playButton1.setFixedHeight(24)
        self.playButton1.setIconSize(btnSize)
        self.playButton1.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton1.setObjectName("playButton1")
        
        self.playButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.playButton2.setGeometry(QtCore.QRect(1010, 530, 93, 28))
        self.playButton2.setEnabled(False)
        self.playButton2.setFixedHeight(24)
        self.playButton2.setIconSize(btnSize)
        self.playButton2.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton2.setObjectName("playButton2")

        self.decodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.decodeButton.setGeometry(QtCore.QRect(720, 560, 141, 71))
        self.decodeButton.setFlat(False)
        self.decodeButton.setEnabled(True)
        self.decodeButton.setObjectName("decodeButton")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(720, 660, 621, 151))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 630, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(720, 640, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.dispButton = QtWidgets.QPushButton(self.centralwidget)
        self.dispButton.setGeometry(QtCore.QRect(1210, 620, 131, 28))
        self.dispButton.setEnabled(False)
        self.dispButton.setObjectName("dispButton")

        self.huffButton = QtWidgets.QPushButton(self.centralwidget)
        self.huffButton.setGeometry(QtCore.QRect(1042, 620, 141, 28))
        self.huffButton.setObjectName("huffButton")

        self.SourceSize = QtWidgets.QLabel(self.centralwidget)
        self.SourceSize.setGeometry(QtCore.QRect(20, 530, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.SourceSize.setFont(font)
        self.SourceSize.setObjectName("SourceSize")

        self.decodedSize = QtWidgets.QLabel(self.centralwidget)
        self.decodedSize.setGeometry(QtCore.QRect(1170, 530, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.decodedSize.setFont(font)
        self.decodedSize.setObjectName("decodedSize")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 170, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(730, 170, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1378, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.encodeButton.setText(_translate("MainWindow", "Encode"))
        self.label_2.setText(_translate("MainWindow", "Source File Path        "))
        self.browseButton1.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Encoded File Folder   "))
        self.browseButton2.setText(_translate("MainWindow", "Browse"))
        self.label_4.setText(_translate("MainWindow", "Encoded File Name    "))
        self.label_10.setText(_translate("MainWindow", "Decoded Video Folder"))
        self.browseButton3.setText(_translate("MainWindow", "Browse"))
        self.label_11.setText(_translate("MainWindow", "Decoded Video Name "))
        self.label.setText(_translate("MainWindow", "Kelompok 2 - Video Encoding \n"
"Made by :"))
        self.label_5.setText(_translate("MainWindow", "Ervin Halimsurya  - 1806195173"))
        self.label_6.setText(_translate("MainWindow", "Jonathan Richard - 1806147930"))
        self.decodeButton.setText(_translate("MainWindow", "Decode"))
        self.label_7.setText(_translate("MainWindow", "Terminal"))
        self.label_8.setText(_translate("MainWindow", "Encoded file Viewer"))
        self.dispButton.setText(_translate("MainWindow", "Display Encoded File"))
        self.huffButton.setText(_translate("MainWindow", "Display Huffman Table"))
        self.SourceSize.setText(_translate("MainWindow", "File Size :"))
        self.decodedSize.setText(_translate("MainWindow", "File Size :"))
        self.label_9.setText(_translate("MainWindow", "Source"))
        self.label_12.setText(_translate("MainWindow", "Compressed"))
from PyQt5.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
