# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTON JA MODUULIEN LATAUKSET
# --------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

from PySide6 import QtWidgets # Qt-vimpaimet
from administrative_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

# Määritellään luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""

    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoituksella
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # OHJELMOIDUT SIGNAALIT
        # ---------------------

        # Kun Tulosa painiketta on klikattu, kutsutaan updatePrintedLabel-metodia
        self.ui,actionMuokkaa.triggered.connect(self.openSettingsDialog)

    
    
    
    # OHJELMOIDUT SLOTIT
    # ------------------

    # Muutetaan tulostettuLabel:n sisältö: teksti ja väri
    def openSettingsDialog(self):
        self.saveSettingsDialog = SaveSettingsDialog()
        self.saveSettingsDialog.setWindowTitle('Palvelinasetukset')

    # Avataan MessageBox
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle('Hirveetä!')
        msgBox.setText('Jotain kamalaa tapahtui')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()       

class SaveSettingsDialog(QtWidgets.QDialog, Ui_Dialog):
    """A class for to open settings dialog window"""

    
if __name__ == "__main__":