# HALLINTASOVELLUKSEN PÄÄIKKUNAN JA DIALOGIEN KOODI
# =================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------

# Pythonin sisäiset moduulit
import os # Polkumääritykset
import sys # Käynnistysargumentit
import json # JSON-objektien ja tiedostojen käsittely

# Asennuksen vaativat kirjastot
from PySide6 import QtWidgets # Qt-vimpaimet


# Käyttöliittymämoduulien lataukset
from administrative_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka
from settingsDialog_ui import Ui_Dialog as Settings_Dialog # Asetukset-dialogin luokka
from passwordDialog_ui import Ui_Dialog as Password_Dialog # Salasanan muutos -dialogin luokka
from aboutDialog_ui import Ui_Dialog as About_Dialog

# Omat moduulit
import cipher # Salaus
import dbOperations # PostgreSQL-tietokantayhteydet

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

        # Rutiini, joka lukee asetukset, jos ne ovat olemassa
        try:
            # Avataam asetustiedosto ja muutetaan se Python sanakirjaksi
            with open('settings.json', 'rt') as settingsFile: # With sulkee tiedoston automaattisesti
                
                # TODO: Mieti kannattaako muuttaa json.load(settingsFile)-komennoksi
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)

            print('Käyttäjätunnus on', self.currentSettings['userName'])
            print('Tietokanta on', self.currentSettings['database'])

            # Huom! Salasana pitää tallentaa JSON-tiedostoon tavallisena merkkijonona,
            # ei byte string muodossa. Fernet-salauskirjastossa avain on aina tavumuodossa.
            # Salausta varten merkkijono on muutettava aina tavumuotoon. Salattu teksti 
            # voidaan tallentaa merkkijononona ja salakirjoitus purkaa suoraan merkkijonosta!
            
            # TODO: Poista print-komennot, ei tarvita enää!   
                
        except Exception as e:
            
            print('Asetusten lataamisessa tapahtui virhe: ', str(e))
            self.openSettingsDialog()

        # OHJELMOIDUT SIGNAALIT
        # ---------------------
        
        # Asetukset-valikon Muokkaa-toiminto avaa Asetukset-dialogi-ikkunan
        self.ui.actionMuokkaa.triggered.connect(self.openSettingsDialog)
        # Asetukset-valikon Salasana-toiminto avaa Salasana-dialogin
        self.ui.actionVaihda_salasana.triggered.connect(self.openPasswordDialog)
        self.ui.actionTietoja_ohjelmasta.triggered.connect(self.openAboutDialog)
        
    # OHJELMOIDUT SLOTIT
    # ==================

    # DIALOGIEN AVAUSMETODIT
    # ----------------------

    # Asetusdialogin avaus
    def openSettingsDialog(self):
        self.saveSettingsDialog = SaveSettingsDialog() # Luodaan luokasta olio
        self.saveSettingsDialog.setWindowTitle('Palvelinasetukset')
        self.saveSettingsDialog.exec() # Luodaan dialogille oma event loop
    
    # Salasanan vaihtodialogin avaus
    def openPasswordDialog(self):
        self.savePasswordDialog = SavePasswordDialog()
        self.savePasswordDialog.setWindowTitle('Vaihda salasana')
        self.savePasswordDialog.exec()

    # Tietoja ohjelmasta -dialogin avaus
    def openAboutDialog(self):
        self.aboutDialog = AboutDialog()
        self.aboutDialog.setWindowTitle('Tietoja ohjelmasta')
        self.aboutDialog.exec() # Luodaan dialogille event loop

    # Malli mahdollista virheilmoitusta varten
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
        
        # Luetaan asetustiedosto Python-sanakirjaksi
        self.currentSettings = {}

        # Tarkistetaan ensin, että asetustiedosto on olemassa
        # TODO: Yksinkertaista asetusten luku käyttämällä json.load-metodia
        try:
            with open('settings.json', 'rt') as settingsFile:
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)

            self.ui.serverLineEdit.setText(self.currentSettings['server'])
            self.ui.portLineEdit.setText(self.currentSettings['port'])
            self.ui.databaseLineEdit.setText(self.currentSettings['database'])
            self.ui.userLineEdit.setText(self.currentSettings['userName'])
            
            
            #self.ui.paswordLineEdit.setText(self.currentSettings['password'])
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

        # Muodostetaan muuttujista Python-sanakirja
        settingsDictionary = {
            'server': server,
            'port': port,
            'database': database,
            'userName': userName
        }

        # Muunnetaan sanakirja JSON-muotoon
        # TODO: Yksinkertaista muttamalla json.dump-metodia käyttäväksi
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
        msgBox.exec() # Luodaan Msg Box:lle oma event loop

class SavePasswordDialog(QtWidgets.QDialog, Password_Dialog):
    """A class to show Change Password Dialog"""
    def __init__(self):
        super().__init__()

        self.ui = Password_Dialog()
        self.ui.setupUi(self)

        
        # Tarkistetaan onko password.json tiedosto olemassa
        self.chekPassword()

        # SIGNAALIT
        self.ui.savePasswordPushButton.clicked.connect(self.savePassword)
    # SLOTIT


    def chekPassword(self):
        # Luetaan käyttöliittymästä tiedot paikallisiin muuttujiin
        try:
            with open('password.json','rt') as pwFile:
                pwJsonData = pwFile.read()

            pwData = json.loads(pwJsonData)
            encryptedOldPassword = pwData['password']
            print(encryptedOldPassword)
            oldPasswordInput = self.ui.oldPasswordLineEdit.text()
            newPasswordInput = self.ui.newPasswordLineEdit.text()
            
        except Exception as e:
            print('Salasanan lataamisessa tapahtui virhe:', str(e))
            self.ui.oldPasswordLineEdit.setEnabled(False)
            self.ui.newPasswordLineEdit.setEnabled(True)
            self.ui.savePasswordPushButton.setEnabled(True)
        
    def savePassword(self):
        plainTextPassword = self.ui.newPasswordLineEdit.text()
        encryptedPassword = cipher.encryptString(plainTextPassword)
        pwDictionary = {'password': encryptedPassword}

        with open('password.json','wt') as pwFile:
                pwData = json.dumps(pwDictionary)
                pwFile.write(pwData)

            

class AboutDialog(QtWidgets.QDialog, About_Dialog):
    """A class to show About dialog."""
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui =About_Dialog()

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

    