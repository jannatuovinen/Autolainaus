# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'administrative.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon(QIcon.fromTheme(u"preferences-desktop-accessibility"))
        MainWindow.setWindowIcon(icon)
        self.actionMuokkaa = QAction(MainWindow)
        self.actionMuokkaa.setObjectName(u"actionMuokkaa")
        self.actionTietoja_ohjelmasta = QAction(MainWindow)
        self.actionTietoja_ohjelmasta.setObjectName(u"actionTietoja_ohjelmasta")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 641, 541))
        self.studentTab = QWidget()
        self.studentTab.setObjectName(u"studentTab")
        self.registerPersontableWidget = QTableWidget(self.studentTab)
        if (self.registerPersontableWidget.columnCount() < 10):
            self.registerPersontableWidget.setColumnCount(10)
        if (self.registerPersontableWidget.rowCount() < 5):
            self.registerPersontableWidget.setRowCount(5)
        self.registerPersontableWidget.setObjectName(u"registerPersontableWidget")
        self.registerPersontableWidget.setGeometry(QRect(10, 220, 731, 201))
        self.registerPersontableWidget.setRowCount(5)
        self.registerPersontableWidget.setColumnCount(10)
        self.registerPersonLabel = QLabel(self.studentTab)
        self.registerPersonLabel.setObjectName(u"registerPersonLabel")
        self.registerPersonLabel.setGeometry(QRect(10, 200, 121, 16))
        self.savePersonPushButton = QPushButton(self.studentTab)
        self.savePersonPushButton.setObjectName(u"savePersonPushButton")
        self.savePersonPushButton.setGeometry(QRect(110, 160, 191, 23))
        self.layoutWidget = QWidget(self.studentTab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 20, 191, 141))
        self.studentInputVerticalLayout = QVBoxLayout(self.layoutWidget)
        self.studentInputVerticalLayout.setObjectName(u"studentInputVerticalLayout")
        self.studentInputVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ssnLineEdit = QLineEdit(self.layoutWidget)
        self.ssnLineEdit.setObjectName(u"ssnLineEdit")
        font = QFont()
        font.setPointSize(10)
        self.ssnLineEdit.setFont(font)

        self.studentInputVerticalLayout.addWidget(self.ssnLineEdit)

        self.firstNameLineEdit = QLineEdit(self.layoutWidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")
        self.firstNameLineEdit.setFont(font)

        self.studentInputVerticalLayout.addWidget(self.firstNameLineEdit)

        self.lastNameLineEdit = QLineEdit(self.layoutWidget)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")
        self.lastNameLineEdit.setFont(font)

        self.studentInputVerticalLayout.addWidget(self.lastNameLineEdit)

        self.groupComboBox = QComboBox(self.layoutWidget)
        self.groupComboBox.setObjectName(u"groupComboBox")
        self.groupComboBox.setFont(font)

        self.studentInputVerticalLayout.addWidget(self.groupComboBox)

        self.vehicleClassLineEdit = QLineEdit(self.layoutWidget)
        self.vehicleClassLineEdit.setObjectName(u"vehicleClassLineEdit")
        self.vehicleClassLineEdit.setFont(font)

        self.studentInputVerticalLayout.addWidget(self.vehicleClassLineEdit)

        self.layoutWidget1 = QWidget(self.studentTab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 93, 131))
        self.studentLabelsVerticalLayout = QVBoxLayout(self.layoutWidget1)
        self.studentLabelsVerticalLayout.setObjectName(u"studentLabelsVerticalLayout")
        self.studentLabelsVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ssnLabel = QLabel(self.layoutWidget1)
        self.ssnLabel.setObjectName(u"ssnLabel")
        self.ssnLabel.setFont(font)

        self.studentLabelsVerticalLayout.addWidget(self.ssnLabel)

        self.firstNameLabel = QLabel(self.layoutWidget1)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        self.firstNameLabel.setFont(font)

        self.studentLabelsVerticalLayout.addWidget(self.firstNameLabel)

        self.lastNameLabel = QLabel(self.layoutWidget1)
        self.lastNameLabel.setObjectName(u"lastNameLabel")
        self.lastNameLabel.setFont(font)

        self.studentLabelsVerticalLayout.addWidget(self.lastNameLabel)

        self.groupLabel = QLabel(self.layoutWidget1)
        self.groupLabel.setObjectName(u"groupLabel")
        self.groupLabel.setFont(font)

        self.studentLabelsVerticalLayout.addWidget(self.groupLabel)

        self.vehicleClassLabel = QLabel(self.layoutWidget1)
        self.vehicleClassLabel.setObjectName(u"vehicleClassLabel")
        self.vehicleClassLabel.setFont(font)

        self.studentLabelsVerticalLayout.addWidget(self.vehicleClassLabel)

        self.tabWidget.addTab(self.studentTab, "")
        self.vehicleTab = QWidget()
        self.vehicleTab.setObjectName(u"vehicleTab")
        self.layoutWidget2 = QWidget(self.vehicleTab)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 20, 96, 151))
        self.vehicleLabelsVerticalLayout = QVBoxLayout(self.layoutWidget2)
        self.vehicleLabelsVerticalLayout.setObjectName(u"vehicleLabelsVerticalLayout")
        self.vehicleLabelsVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.numberPlateLabel = QLabel(self.layoutWidget2)
        self.numberPlateLabel.setObjectName(u"numberPlateLabel")
        self.numberPlateLabel.setFont(font)

        self.vehicleLabelsVerticalLayout.addWidget(self.numberPlateLabel)

        self.manufacturedLabel = QLabel(self.layoutWidget2)
        self.manufacturedLabel.setObjectName(u"manufacturedLabel")
        self.manufacturedLabel.setFont(font)

        self.vehicleLabelsVerticalLayout.addWidget(self.manufacturedLabel)

        self.modelLabel = QLabel(self.layoutWidget2)
        self.modelLabel.setObjectName(u"modelLabel")
        self.modelLabel.setFont(font)

        self.vehicleLabelsVerticalLayout.addWidget(self.modelLabel)

        self.modelYearLabel = QLabel(self.layoutWidget2)
        self.modelYearLabel.setObjectName(u"modelYearLabel")
        self.modelYearLabel.setFont(font)

        self.vehicleLabelsVerticalLayout.addWidget(self.modelYearLabel)

        self.capacityLabel = QLabel(self.layoutWidget2)
        self.capacityLabel.setObjectName(u"capacityLabel")
        self.capacityLabel.setFont(font)

        self.vehicleLabelsVerticalLayout.addWidget(self.capacityLabel)

        self.layoutWidget_2 = QWidget(self.vehicleTab)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(120, 20, 169, 161))
        self.vehicleInputsVerticalLayout = QVBoxLayout(self.layoutWidget_2)
        self.vehicleInputsVerticalLayout.setObjectName(u"vehicleInputsVerticalLayout")
        self.vehicleInputsVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.numberPlateLineEdit = QLineEdit(self.layoutWidget_2)
        self.numberPlateLineEdit.setObjectName(u"numberPlateLineEdit")
        font1 = QFont()
        font1.setPointSize(11)
        self.numberPlateLineEdit.setFont(font1)

        self.vehicleInputsVerticalLayout.addWidget(self.numberPlateLineEdit)

        self.manufactureLineEdit = QLineEdit(self.layoutWidget_2)
        self.manufactureLineEdit.setObjectName(u"manufactureLineEdit")
        self.manufactureLineEdit.setFont(font1)

        self.vehicleInputsVerticalLayout.addWidget(self.manufactureLineEdit)

        self.modelLineEdit = QLineEdit(self.layoutWidget_2)
        self.modelLineEdit.setObjectName(u"modelLineEdit")
        self.modelLineEdit.setFont(font1)

        self.vehicleInputsVerticalLayout.addWidget(self.modelLineEdit)

        self.modelYearLineEdit = QLineEdit(self.layoutWidget_2)
        self.modelYearLineEdit.setObjectName(u"modelYearLineEdit")
        self.modelYearLineEdit.setFont(font1)

        self.vehicleInputsVerticalLayout.addWidget(self.modelYearLineEdit)

        self.capacityLineEdit = QLineEdit(self.layoutWidget_2)
        self.capacityLineEdit.setObjectName(u"capacityLineEdit")
        self.capacityLineEdit.setFont(font1)

        self.vehicleInputsVerticalLayout.addWidget(self.capacityLineEdit)

        self.saveVehiclepushButton = QPushButton(self.vehicleTab)
        self.saveVehiclepushButton.setObjectName(u"saveVehiclepushButton")
        self.saveVehiclepushButton.setGeometry(QRect(120, 180, 171, 23))
        self.printBarcodepushButton = QPushButton(self.vehicleTab)
        self.printBarcodepushButton.setObjectName(u"printBarcodepushButton")
        self.printBarcodepushButton.setGeometry(QRect(10, 180, 91, 23))
        self.vehicleListTableWidget = QTableWidget(self.vehicleTab)
        if (self.vehicleListTableWidget.columnCount() < 5):
            self.vehicleListTableWidget.setColumnCount(5)
        if (self.vehicleListTableWidget.rowCount() < 10):
            self.vehicleListTableWidget.setRowCount(10)
        self.vehicleListTableWidget.setObjectName(u"vehicleListTableWidget")
        self.vehicleListTableWidget.setGeometry(QRect(20, 230, 551, 311))
        self.vehicleListTableWidget.setRowCount(10)
        self.vehicleListTableWidget.setColumnCount(5)
        self.vehicleListLabel = QLabel(self.vehicleTab)
        self.vehicleListLabel.setObjectName(u"vehicleListLabel")
        self.vehicleListLabel.setGeometry(QRect(20, 210, 61, 16))
        self.tabWidget.addTab(self.vehicleTab, "")
        self.groupTab = QWidget()
        self.groupTab.setObjectName(u"groupTab")
        self.pushButton = QPushButton(self.groupTab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 50, 75, 23))
        font2 = QFont()
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.groupTableWidget = QTableWidget(self.groupTab)
        if (self.groupTableWidget.columnCount() < 2):
            self.groupTableWidget.setColumnCount(2)
        if (self.groupTableWidget.rowCount() < 10):
            self.groupTableWidget.setRowCount(10)
        self.groupTableWidget.setObjectName(u"groupTableWidget")
        self.groupTableWidget.setGeometry(QRect(20, 120, 256, 331))
        self.groupTableWidget.setRowCount(10)
        self.groupTableWidget.setColumnCount(2)
        self.storeGroupLabel = QLabel(self.groupTab)
        self.storeGroupLabel.setObjectName(u"storeGroupLabel")
        self.storeGroupLabel.setGeometry(QRect(20, 100, 101, 16))
        self.layoutWidget3 = QWidget(self.groupTab)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 20, 81, 61))
        self.verticalLayout = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupNameLabel = QLabel(self.layoutWidget3)
        self.groupNameLabel.setObjectName(u"groupNameLabel")
        self.groupNameLabel.setFont(font)

        self.verticalLayout.addWidget(self.groupNameLabel)

        self.responsiblePersonLabel = QLabel(self.layoutWidget3)
        self.responsiblePersonLabel.setObjectName(u"responsiblePersonLabel")
        self.responsiblePersonLabel.setFont(font)

        self.verticalLayout.addWidget(self.responsiblePersonLabel)

        self.layoutWidget4 = QWidget(self.groupTab)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(140, 20, 169, 60))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupNameLineEdit = QLineEdit(self.layoutWidget4)
        self.groupNameLineEdit.setObjectName(u"groupNameLineEdit")
        self.groupNameLineEdit.setFont(font1)

        self.verticalLayout_2.addWidget(self.groupNameLineEdit)

        self.responsiblePersonLneEdit_2 = QLineEdit(self.layoutWidget4)
        self.responsiblePersonLneEdit_2.setObjectName(u"responsiblePersonLneEdit_2")
        self.responsiblePersonLneEdit_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.responsiblePersonLneEdit_2)

        self.tabWidget.addTab(self.groupTab, "")
        self.reportsTab = QWidget()
        self.reportsTab.setObjectName(u"reportsTab")
        self.reportTypeComboBox = QComboBox(self.reportsTab)
        self.reportTypeComboBox.setObjectName(u"reportTypeComboBox")
        self.reportTypeComboBox.setGeometry(QRect(20, 40, 161, 22))
        self.reportTypeComboBox.setFont(font1)
        self.raportTypeLabel = QLabel(self.reportsTab)
        self.raportTypeLabel.setObjectName(u"raportTypeLabel")
        self.raportTypeLabel.setGeometry(QRect(20, 20, 47, 13))
        self.raportTypeLabel.setFont(font)
        self.beginningDateEdit = QDateEdit(self.reportsTab)
        self.beginningDateEdit.setObjectName(u"beginningDateEdit")
        self.beginningDateEdit.setGeometry(QRect(20, 90, 110, 22))
        self.beginningDateEdit.setFont(font1)
        self.beginningLabel = QLabel(self.reportsTab)
        self.beginningLabel.setObjectName(u"beginningLabel")
        self.beginningLabel.setGeometry(QRect(20, 70, 47, 13))
        self.beginningLabel.setFont(font)
        self.endingDateEdit = QDateEdit(self.reportsTab)
        self.endingDateEdit.setObjectName(u"endingDateEdit")
        self.endingDateEdit.setGeometry(QRect(140, 90, 110, 22))
        self.endingDateEdit.setFont(font1)
        self.endingLabel = QLabel(self.reportsTab)
        self.endingLabel.setObjectName(u"endingLabel")
        self.endingLabel.setGeometry(QRect(140, 70, 47, 13))
        self.endingLabel.setFont(font)
        self.printReportPushButton = QPushButton(self.reportsTab)
        self.printReportPushButton.setObjectName(u"printReportPushButton")
        self.printReportPushButton.setGeometry(QRect(140, 130, 111, 23))
        self.tableWidget = QTableWidget(self.reportsTab)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        if (self.tableWidget.rowCount() < 22):
            self.tableWidget.setRowCount(22)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 180, 641, 331))
        self.tableWidget.setRowCount(22)
        self.tableWidget.setColumnCount(6)
        self.previewLabel = QLabel(self.reportsTab)
        self.previewLabel.setObjectName(u"previewLabel")
        self.previewLabel.setGeometry(QRect(20, 160, 47, 13))
        self.tabWidget.addTab(self.reportsTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuAsetukset = QMenu(self.menubar)
        self.menuAsetukset.setObjectName(u"menuAsetukset")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAsetukset.menuAction())
        self.menuAsetukset.addAction(self.actionMuokkaa)
        self.menuAsetukset.addAction(self.actionTietoja_ohjelmasta)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionMuokkaa.setText(QCoreApplication.translate("MainWindow", u"Muokkaa", None))
#if QT_CONFIG(tooltip)
        self.actionMuokkaa.setToolTip(QCoreApplication.translate("MainWindow", u"Muokkaa ohjelman asetuksia", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionMuokkaa.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionTietoja_ohjelmasta.setText(QCoreApplication.translate("MainWindow", u"Tietoja ohjelmasta...", None))
#if QT_CONFIG(shortcut)
        self.actionTietoja_ohjelmasta.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+T", None))
#endif // QT_CONFIG(shortcut)
        self.registerPersonLabel.setText(QCoreApplication.translate("MainWindow", u"Rekister\u00f6idyt lainaajat", None))
        self.savePersonPushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.ssnLabel.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6tunnus", None))
        self.firstNameLabel.setText(QCoreApplication.translate("MainWindow", u"Etunimi", None))
        self.lastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi", None))
        self.groupLabel.setText(QCoreApplication.translate("MainWindow", u"Ryhm\u00e4", None))
        self.vehicleClassLabel.setText(QCoreApplication.translate("MainWindow", u"Ajoneuvoluokka", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.studentTab), QCoreApplication.translate("MainWindow", u"Lainaajat", None))
        self.numberPlateLabel.setText(QCoreApplication.translate("MainWindow", u"Rekisterinumero", None))
        self.manufacturedLabel.setText(QCoreApplication.translate("MainWindow", u"Merkki", None))
        self.modelLabel.setText(QCoreApplication.translate("MainWindow", u"Malli", None))
        self.modelYearLabel.setText(QCoreApplication.translate("MainWindow", u"Vuosimalli", None))
        self.capacityLabel.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6m\u00e4\u00e4r\u00e4", None))
        self.saveVehiclepushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.printBarcodepushButton.setText(QCoreApplication.translate("MainWindow", u"Viivakoodi", None))
        self.vehicleListLabel.setText(QCoreApplication.translate("MainWindow", u"Autoluettelo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vehicleTab), QCoreApplication.translate("MainWindow", u"Autot", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.storeGroupLabel.setText(QCoreApplication.translate("MainWindow", u"Tallennetut ryhm\u00e4t", None))
        self.groupNameLabel.setText(QCoreApplication.translate("MainWindow", u"Ryhm\u00e4n nimi", None))
        self.responsiblePersonLabel.setText(QCoreApplication.translate("MainWindow", u"Vastuuhenkil\u00f6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.groupTab), QCoreApplication.translate("MainWindow", u"Ryhm\u00e4t", None))
        self.raportTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Raportit", None))
        self.beginningLabel.setText(QCoreApplication.translate("MainWindow", u"Alkaa", None))
        self.endingLabel.setText(QCoreApplication.translate("MainWindow", u"P\u00e4\u00e4ttyy", None))
        self.printReportPushButton.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))
        self.previewLabel.setText(QCoreApplication.translate("MainWindow", u"Esikatselu", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reportsTab), QCoreApplication.translate("MainWindow", u"Raportit", None))
        self.menuAsetukset.setTitle(QCoreApplication.translate("MainWindow", u"Asetukset", None))
    # retranslateUi

