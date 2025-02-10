# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'suttu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import suttuResources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 20, 191, 381))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 171, 201))
        self.label.setPixmap(QPixmap(u":/pictures/uiPictures/student.png"))
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 230, 141, 61))
        font = QFont()
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 310, 71, 41))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(223, 32, 112);\n"
"color: rgb(255, 255, 255);")
        self.ResetPositionsPushButton = QPushButton(self.centralwidget)
        self.ResetPositionsPushButton.setObjectName(u"ResetPositionsPushButton")
        self.ResetPositionsPushButton.setGeometry(QRect(370, 50, 101, 41))
        self.ResetPositionsPushButton.setFont(font1)
        self.ResetPositionsPushButton.setStyleSheet(u"background-color: rgb(0, 33, 72);\n"
"color: rgb(255, 255, 255);")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(102, 431, 373, 58))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.LastNameLineEdit = QLineEdit(self.widget)
        self.LastNameLineEdit.setObjectName(u"LastNameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.LastNameLineEdit)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.pushButton_2)

        self.FirstNameLineEdit = QLineEdit(self.widget)
        self.FirstNameLineEdit.setObjectName(u"FirstNameLineEdit")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.FirstNameLineEdit)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pushButton_3)


        self.horizontalLayout.addLayout(self.formLayout)

        self.lastFocusPushButton = QPushButton(self.widget)
        self.lastFocusPushButton.setObjectName(u"lastFocusPushButton")
        self.lastFocusPushButton.setStyleSheet(u"background-color: rgb(255, 170, 0);")

        self.horizontalLayout.addWidget(self.lastFocusPushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Testi", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.ResetPositionsPushButton.setText(QCoreApplication.translate("MainWindow", u"Palauta", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.lastFocusPushButton.setText(QCoreApplication.translate("MainWindow", u"Last Focus", None))
    # retranslateUi

