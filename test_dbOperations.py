# TIETOKANTAYHTEYKSIEN TESTAUS
# ============================

import pytest # Virheilmoitusten testaus vaatii
import dbOperations # Testattava moduuli

settingsDictionary = {'server': 'localhost',
                      'port': '5432',
                      'database': 'testaus',
                      'userName': 'postgres',
                      'password': 'Q2werty'}

dbConnection = dbOperations.DbConnection(settingsDictionary)

# Testataan, että yhteysmerkkijono muodostuu oikein
def test_connectionString():
    assert dbConnection.connectionString == f'dbname=testaus user=postgres password=Q2werty host=localhost port=5432'

# Testataan, että taulun kaikki tiedot saadaan
def test_readOneRow():
    resultlist = dbConnection.readAllColumnsFromTable('person') # Hakee taulun kaikki rivit listaan
    assert resultlist[0] == (1, 'Ville', 'Virtanen') # Ensimmäinen rivi pitäisi olla 1 Ville Virtanen

# TODO: Mieti mitä muita testejä pitää kirjoittaa