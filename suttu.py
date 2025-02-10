# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

from PySide6 import QtWidgets # Qt-vimpaimet

# mainWindow_ui:n tilalle käännetyn pääikkunan tiedoston nimi
# ilman .py-tiedostopäätettä
from suttu_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

# Määritellään luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""
    
    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # Muuttuja (ominaisuus) viimeiseksi muokatun elementin nimen tallentamiseen
        self.lastEditedElementName = 'Ei mikään'

        # OHJELMOIDUT SIGNAALIT
        # ---------------------
        
        # Kun OK-painiketta on klikattu, kutsutaan buttonPressSLot-metodia
        self.ui.pushButton.clicked.connect(self.buttonPressSlot)

        # Kun Palauta-painiketta on klikattu siirrä ikkuna takaisin
        self.ui.ResetPositionsPushButton.clicked.connect(self.resetPositions)

        # Kun kenttä menettää fokuksen kirjataan kentän nimi ominaisuuteen lastEditedElementName
        self.ui.FirstNameLineEdit.editingFinished.connect(self.setLastEditedElement)

        # Last Focus - painike
        self.ui.lastFocusPushButton.clicked.connect(self.showLastElementName)


    # OHJELMOIDUT SLOTIT
    # ------------------

    # Tallennetaan elementin nimi
    def setLastEditedElement(self):
        self.lastEditedElementName = 'FirstNameLineEdit'

    # Käytetään elementin nimi
    def showLastElementName(self):
        message = f'Viimeksi käytetty kenttä on {self.lastEditedElementName}'
        self.ui.statusbar.showMessage(message)

        # Haetaan elementti nimen perusteella ja siirretään fokus siihen
        element = self.findChild(QtWidgets.QLineEdit, self.lastEditedElementName)
        element.setFocus()

    # Siirretään elementtejä kehyksen avulla ja kehyksen sisällä
    def buttonPressSlot(self):
        self.ui.statusbar.showMessage("Painoit sitten nappia...", 5000)
        self.ui.frame.move(300, 250)
        self.ui.label.move(100,100)

        # Luetaan pääikkunan sisällön korkeus ja leveys
        height = self.ui.centralwidget.height()
        width = self.ui.centralwidget.width()
        message = f'ikkunan korkeus on {height} ja leveys {width}'
        self.ui.statusbar.showMessage(message, 5000)

    # Siiretään elementit
    def resetPositions(self):
        self.ui.frame.move(0,0)
        self.ui.label.move(0,10)

    # Avataan MessageBox
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle('Hirveetä!')
        msgBox.setText('Jotain kamalaa tapahtui')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()


# Luodaan sovellus
app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
window = MainWindow()
window.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä
app.exec()

    