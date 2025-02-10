# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# ========================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit
import json # JSON-tiedoston käsittely

import time # Tuodaan aika ja päivä muokkaus mahdollisuudet

from PySide6 import QtWidgets # Qt-vimpaimet
from PySide6.QtCore import QThreadPool, Slot # Säikeistys ja Slot-dekoraattori

from lendingModules import sound # Äänikomennot
from lendingModules import dbOperations # Tietokantatoiminnot
from lendingModules import cipher # Salausmoduuli

# Tuodaan käyttöliittymän Pythoniksi käänetty tiedosto
from user_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

# Määritellään luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""
    
    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan säikeistystä varten uusi säievaranto
        self.threadPool = QThreadPool()

        # Luodaan säievaranto
        self.threadPool = QThreadPool()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # Rutiini, joka lukee asetukset, jos ne ovat olemassa
        try:
            # Avataam asetustiedosto ja muutetaan se Python sanakirjaksi
            with open('settings.json', 'rt') as settingsFile: # With sulkee tiedoston automaattisesti
                
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)

            # Puretaan salasana tietokannan käyttöä varten
            self.plainTextPassword = cipher.decryptString(self.currentSettings['password'])

        except Exception as error:
            self.openWarning()

        # Äänet oletuksena käytössä
        self.soundOn = True

        # Ohjelmaa käynnistäessä piilotetaan tarpeettomat elementit
        self.setInitialElements()

        self.ui.statusbar.showMessage('Valitse Lainaa auto tai Palauta auto')


        # OHJELMOIDUT SIGNAALIT
        # ---------------------

        # Kuin Lainaa auto painiketta on painettu kutsutaan metodia takeCar
        self.ui.takeCarPushButton.clicked.connect(self.takeCar)

        # Kuina ajokortti on luettu kutsutaan showKeys metodia
        self.ui.licenseLineEdit.returnPressed.connect(self.showKeys)

        # Kuin auton avaimenperä on luettu kutsutaan showTime metodia
        self.ui.keysLineEdit.returnPressed.connect(self.showTime)

        # Komennot kutsumaan metodeja jotka halitsee ääni nappulaa
        self.ui.soundOffPushButton.clicked.connect(self.muteSound)
        self.ui.soundOnPushButton.clicked.connect(self.takeSound)

        # Kuin Palauta auto painiketta on painettu kutsutaan metodia returnCar
        self.ui.returnCarPushButton.clicked.connect(self.returnCar)

        # Kun Ok-painiketta on painettu talenna tiedot ja palauta käyttöliittymä alkutilaan
        self.ui.okPushButton.clicked.connect(self.saveLendingData)

        # Kun palauttaessa on luettu avaimen viivakoodi kutsutaan returnStart metodia
        self.ui.keysReturnLineEdit.returnPressed.connect(self.returnStart)

        # Kun kumoa painiketta painetaan palautetaan UI-alkutilaan
        self.ui.goBackPushButton.clicked.connect(self.goBack)

    # OHJELMOIDUT SLOTIT
    # ------------------

    # Soita parametrina annettu äänitiedosto
    @Slot(str)
    def playSoundFile(self, soundFileName):
        fileAndPath = 'sounds\\' + soundFileName
        sound.playWav(fileAndPath)

    @Slot(str)
    def playSoundInThread(self, soundFileName):
        self.threadPool.start(self.playSoundFile(soundFileName))

    # Palauta käyttöliittymä alkutilaan
    def setInitialElements(self):
        self.ui.returnCarPushButton.show()
        self.ui.takeCarPushButton.show()
        self.ui.soundOnPushButton.hide()
        self.ui.borrowerLabel.hide()
        self.ui.humanLabel.hide()
        self.ui.licenseLineEdit.clear()
        self.ui.licenseLineEdit.hide()
        self.ui.nameLabel.hide()
        self.ui.carTakeLabel.hide()
        self.ui.carKeysLabel.hide()
        self.ui.keysLineEdit.clear()
        self.ui.keysLineEdit.hide()
        self.ui.carInfoLabel.hide()
        self.ui.calenderLabel.hide()
        self.ui.dateLabel.hide()
        self.ui.clockPictureLabel.hide()
        self.ui.hourLabel.hide()
        self.ui.goBackPushButton.hide()
        self.ui.okPushButton.hide()
        self.ui.keysReturnLineEdit.clear()
        self.ui.keysReturnLineEdit.hide()
        self.ui.carKeysReturnLabel.hide()
        self.ui.carTakeReturnLabel.hide()
        self.ui.veachleLabel.hide()
        self.ui.carLabel.hide()

    # Kuin Aloita lainaus nappia on painettu nämä componentit tulee esiin tai piiloutuu
    @Slot()
    def takeCar(self):
        self.ui.borrowerLabel.show()
        self.ui.humanLabel.show()
        self.ui.goBackPushButton.show()
        self.ui.licenseLineEdit.show()
        self.ui.licenseLineEdit.setFocus()
        self.ui.returnCarPushButton.hide()
        self.ui.takeCarPushButton.hide()
        self.ui.statusbar.showMessage('Lue ajokortin viivakoodi')
        self.threadPool.start(self.playWavFile)
    # Soitetaan äänitiedosto
    @Slot()
    def playWavFile(self):
        sound.playWav('sounds\\drivingLicence.wav')

    # Ajokortin lukemisen jälkeen nämä komponentint tulevat essin
    @Slot()
    def showKeys(self):
        self.ui.licenseLineEdit.hide()
        self.ui.nameLabel.show()
        self.ui.carTakeLabel.show()
        self.ui.carKeysLabel.show()
        self.ui.keysLineEdit.show()
        self.ui.keysLineEdit.setFocus()
        self.ui.statusbar.showMessage('Lue avaimen viivakoodi')
        self.threadPool.start(self.playWavKeys)

    # Soitetaan äänitiedosto
    @Slot()
    def playWavKeys(self):
        sound.playWav('sounds\\readKey.WAV')

    # Kuin avaimen viivakoodi on luettu nämä komponentit tulevat essin
    @Slot()
    def showTime(self):
        self.ui.carInfoLabel.show()
        self.ui.calenderLabel.show()
        self.ui.dateLabel.show()
        self.ui.clockPictureLabel.show()
        self.ui.hourLabel.show()
        self.ui.veachleLabel.show()
        self.ui.carLabel.show()
        self.ui.okPushButton.show()
        self.ui.statusbar.showMessage('Jos tiedot on oikein paina Ok painiketta')
        self.threadPool.start(self.playWavData)
        self.ui.dateLabel.setText(f'{time.strftime('%d.%m.%Y')}')
        self.ui.hourLabel.setText(f'{time.strftime('%H:%M')}')

    # Soitetaan äänitiedosto
    @Slot()
    def playWavData(self):
        sound.playWav('sounds\\saveData.wav')

    @Slot()
    def saveLendingData(self):
        # tallenna tiedot tietokantaan
        # Luetaan tietokanta-asetukset paikallisiin muuttujiin
        dbSettings = self.currentSettings
        plainTextPassword = self.plainTextPassword
        dbSettings['password'] = plainTextPassword # Vaihdetaan selväkieliseksi 
        
        try:
            # Luodaan tietokantayhteys-olio
            dbConnection = dbOperations.DbConnection(dbSettings)
            ssn = self.ui.licenseLineEdit.text()
            key = self.ui.keysLineEdit.text()
            dataDictionary = {'hetu': ssn,
                          'rekisterinumero': key}
            dbConnection.addToTable('lainaus', dataDictionary)

            self.setInitialElements()
            self.ui.statusbar.showMessage('Lainaus tiedot on tallenettu', 5000)
            self.threadPool.start(self.playWavOk)

        except Exception as e:
            title = 'Lainaustietojen tallentaminen ei onnistu'
            text = 'Ajokortin tai auton tiedot virheeliset, ota yhteys henkilökuntaan!'
            detailedText = str(e)
            self.openWarning(title, text, detailedText)
    
    @Slot()
    def playWavOk(self):
        sound.playWav('sounds\\lendingOk.wav')


    # Mykistetään äänet
    def muteSound(self):
        self.ui.soundOnPushButton.show()
        self.ui.soundOffPushButton.hide()
        self.ui.statusbar.showMessage('Äänet mykistetty', 5000)
        self.soundOn = False

    # Palutetaan äänet
    def takeSound(self):
        self.ui.soundOffPushButton.show()
        self.ui.soundOnPushButton.hide()
        self.ui.statusbar.showMessage('Äänet päällä', 5000)
        self.soundOn = True

    # Kuin aloita palautus nappia on painettu nämä komponentit tulevat näkyviin tai piiloutuu
    def returnCar(self):
        self.ui.carTakeReturnLabel.show()
        self.ui.carKeysReturnLabel.show()
        self.ui.keysReturnLineEdit.show()
        self.ui.keysReturnLineEdit.setFocus()
        self.ui.goBackPushButton.show()
        self.ui.takeCarPushButton.hide()
        self.ui.returnCarPushButton.hide()
        self.ui.statusbar.showMessage('Lue avaimen viivakoodi')
        self.threadPool.start(self.playWavReturn)

    # Soitetaan äänitiedosto
    @Slot()
    def playWavReturn(arg):
        sound.playWav('sounds\\redKey.wav')
            


    # Kumoa painikkeen painamisen jälkeen palataan alkunäkymään
    def returnStart(self):
        self.setInitialElements()
        self.ui.statusbar.showMessage('Palattu alkunäkymään',5000)

    def goBack(self):
        self.setInitialElements()
        self.ui.statusbar.showMessage('Toiminto peruutettiin', 5000)
    

    # Malli mahdollista virheilmoitusta varten
    def openWarning(self, title: str, text: str, detailedText:str) -> None:
        """Opens a message box for errors

        Args:
            title (str): The title of the message box
            text (str): Error message
            detailedText (str): Detailed error message
        """
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.setDetailedText(detailedText)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()


# Luodaan sovellus
app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
window = MainWindow()
window.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä
app.exec()