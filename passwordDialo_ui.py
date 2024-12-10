# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordDialo.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 100, 81, 21))
        font = QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 92, 61))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.oldPasswordLabel = QLabel(self.widget)
        self.oldPasswordLabel.setObjectName(u"oldPasswordLabel")
        self.oldPasswordLabel.setFont(font)

        self.verticalLayout.addWidget(self.oldPasswordLabel)

        self.newPasswordLabel = QLabel(self.widget)
        self.newPasswordLabel.setObjectName(u"newPasswordLabel")
        self.newPasswordLabel.setFont(font)

        self.verticalLayout.addWidget(self.newPasswordLabel)

        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(130, 30, 169, 56))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.oldPasswordLineEdit = QLineEdit(self.widget1)
        self.oldPasswordLineEdit.setObjectName(u"oldPasswordLineEdit")
        font1 = QFont()
        font1.setPointSize(11)
        self.oldPasswordLineEdit.setFont(font1)

        self.verticalLayout_2.addWidget(self.oldPasswordLineEdit)

        self.newPasswordLineEdit = QLineEdit(self.widget1)
        self.newPasswordLineEdit.setObjectName(u"newPasswordLineEdit")
        self.newPasswordLineEdit.setFont(font1)

        self.verticalLayout_2.addWidget(self.newPasswordLineEdit)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Tallenna", None))
        self.oldPasswordLabel.setText(QCoreApplication.translate("Dialog", u"Vanha salasana", None))
        self.newPasswordLabel.setText(QCoreApplication.translate("Dialog", u"Uusi salasana", None))
    # retranslateUi

