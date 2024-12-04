# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------

# Pythonin sisäiset moduulit
import os # Polkumääritykset
import sys # Käynnistysargumentit
import json # JSON-objektien ja tiedostojen käsittely

# Asennuksen vaativat kirjastot
from PySide6 import QtWidgets # Qt-vimpaimet
# Jos laajennus ei tee _ui.py tiedostoja tee ne komennolla pyside6-uic joku.ui -o jouku_ui.py

# Käyttöliittymämoduulien lataukset
from administrative_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka
from settingsDialog_ui import Ui_Dialog as Settings_Dialog # Asetukset-dialogin luokka
from aboutDialog_ui import Ui_Dialog as About_Dialog

# Omat moduulit
import cipher

# LUOKKAMÄÄRITYKSET
# -----------------

# Määritellään pääikkunan luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""
    
    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # OHJELMOIDUT SIGNAALIT
        # ---------------------
        
        # Asetukset-valikon muokkaa toiminto avaa Asetukset-dialogi-ikkunan
        self.ui.actionMuokkaa.triggered.connect(self.openSettingsDialog)
        self.ui.actionTietoja_ohjelmasta.triggered.connect(self.openAboutDialog)
        

        
   
    # OHJELMOIDUT SLOTIT
    # ------------------

    # DIALOGIEN AVAUSMETODIT
    # ----------------------

    # Asetusdialogin avaus
    def openSettingsDialog(self):
        self.saveSettingsDialog = SaveSettingsDialog()
        self.saveSettingsDialog.setWindowTitle('Palvelinasetukset')
        self.saveSettingsDialog.exec()
        
    # Tietoja ohjelmasta -dialogin avaus
    def openAboutDialog(self):
        self.aboutDialog = AboutDialog()
        self.aboutDialog.setWindowTitle('Tietoja ohjelmasta')
        self.aboutDialog.exec() # Luodaan dialogille event loop

    # Malli mahdollisia virheilmoituksia varten
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle('Hirveetä!')
        msgBox.setText('Jotain kamalaa tapahtui')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

# Asetusten tallennusikkunan luokka
class SaveSettingsDialog(QtWidgets.QDialog, Settings_Dialog):
    """A class to open settings dialog window"""
    
    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Settings_Dialog()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # Salausavain luottamuksellisten asetusten kryptaamiseen
        # Avainta ei saa vaihtaa ohjelman käyttöönoton jälkeen!
        # Avain on luotu cipher.py
        self.secretKey = b'8Zra5xvI3derJNwLCue1iDdw0lbZm_T0zXFaBknPXI4='
        self.cryptoEngine = cipher.createChipher(self.secretKey)

        # Luetaan asetustiedosto Python-sanakirjaksi
        self.currentSettings = {}

        # Tarkistetaan ensin, että asetustiedosto on olemassa
        try:
            with open('settings.json', 'rt') as settingsFile:
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)

            self.ui.serverLineEdit.setText(self.currentSettings['server'])
            self.ui.portLineEdit.setText(self.currentSettings['port'])
            self.ui.databaseLineEdit.setText(self.currentSettings['database'])
            self.ui.userLineEdit.setText(self.currentSettings['userName'])
            self.ui.paswordLineEdit.setText(self.currentSettings['password'])
        except Exception as e:
            self.openInfo()
        

        # OHJELMOIDUT SIGNAALIT
        # ---------------------

        # Kun Tallenna-painiketta on klikattu, kutsutaan saveToJsonFile-metodia
        self.ui.saveSettingspushButton.clicked.connect(self.saveToJsonFile)
    
    # OHJELMOIDUT SLOTIT (Luokan metodit)
    # -----------------------------------
    
    # Tallennetaan käyttöliittymään syötetyt asetukset tiedostoon
    def saveToJsonFile(self):

        # Luetaan käyttöliittymästä tiedot paikallisiin muuttujiin
        server = self.ui.serverLineEdit.text()
        port = self.ui.portLineEdit.text()
        database = self.ui.databaseLineEdit.text()
        userName = self.ui.userLineEdit.text()

        # Muutetaan merkkijono tavumuotoon (byte, merkistö UTF-8)
        plainTextPassword = bytes(self.ui.paswordLineEdit.text(), 'utf-8')
       
        # Salataan ja muunnetaan tavalliseksi merkkijonoksi, jotta JSON-tallennus onnistuu
        encryptedPassword = str(cipher.encrypt(self.cryptoEngine, plainTextPassword))

        # Muodostetaan muuttujista Python-sanakirja
        settingsDictionary = {
            'server': server,
            'port': port,
            'database': database,
            'userName': userName,
            'password': encryptedPassword
        }

        # Muunnetaan sanakirja JSON-muotoon
        jsonData = json.dumps(settingsDictionary)
        
        # Avataan asetustiedosto ja kirjoitetaan asetukset
        with open('settings.json', 'wt') as settingsFile:
            settingsFile.write(jsonData)

    
    # Avataan MessageBox, jossa kerrotaan että tehdää uusi asetustiedosto
    def openInfo(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle('Luodaan uusi asetustiedosto')
        msgBox.setText('Syötä kaikkien kenttien tiedot!')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

class AboutDialog(QtWidgets.QDialog, About_Dialog):
    """A class to show About Dialog."""
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = About_Dialog()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

    


if __name__ == "__main__":
    
    # Luodaan sovellus ja asetetaan tyyliksi Fusion
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.setWindowTitle('Autolainauksen hallinta')
    window.show()

    # Käynnistetään sovellus ja tapahtumienkäsittelijä
    app.exec()

    