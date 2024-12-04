# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsDialog.ui'
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
        Dialog.resize(291, 219)
        self.saveSettingspushButton = QPushButton(Dialog)
        self.saveSettingspushButton.setObjectName(u"saveSettingspushButton")
        self.saveSettingspushButton.setGeometry(QRect(180, 180, 81, 23))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.saveSettingspushButton.setFont(font)
        self.saveSettingspushButton.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 91, 151))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ServerLabel = QLabel(self.layoutWidget)
        self.ServerLabel.setObjectName(u"ServerLabel")
        font1 = QFont()
        font1.setPointSize(10)
        self.ServerLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.ServerLabel)

        self.portLabel = QLabel(self.layoutWidget)
        self.portLabel.setObjectName(u"portLabel")
        self.portLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.portLabel)

        self.databaseLabel = QLabel(self.layoutWidget)
        self.databaseLabel.setObjectName(u"databaseLabel")
        self.databaseLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.databaseLabel)

        self.userLabel = QLabel(self.layoutWidget)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.userLabel)

        self.passwordLabel = QLabel(self.layoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.passwordLabel)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(120, 20, 135, 146))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.serverLineEdit = QLineEdit(self.layoutWidget1)
        self.serverLineEdit.setObjectName(u"serverLineEdit")
        font2 = QFont()
        font2.setPointSize(11)
        self.serverLineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.serverLineEdit)

        self.portLineEdit = QLineEdit(self.layoutWidget1)
        self.portLineEdit.setObjectName(u"portLineEdit")
        self.portLineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.portLineEdit)

        self.databaseLineEdit = QLineEdit(self.layoutWidget1)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")
        self.databaseLineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.databaseLineEdit)

        self.userLineEdit = QLineEdit(self.layoutWidget1)
        self.userLineEdit.setObjectName(u"userLineEdit")
        self.userLineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.userLineEdit)

        self.paswordLineEdit = QLineEdit(self.layoutWidget1)
        self.paswordLineEdit.setObjectName(u"paswordLineEdit")
        self.paswordLineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.paswordLineEdit)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.saveSettingspushButton.setText(QCoreApplication.translate("Dialog", u"Tallenna", None))
        self.ServerLabel.setText(QCoreApplication.translate("Dialog", u"Palvelin", None))
        self.portLabel.setText(QCoreApplication.translate("Dialog", u"Portti", None))
        self.databaseLabel.setText(QCoreApplication.translate("Dialog", u"Tietokanta", None))
        self.userLabel.setText(QCoreApplication.translate("Dialog", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.passwordLabel.setText(QCoreApplication.translate("Dialog", u"Salasana", None))
    # retranslateUi

