# TIETOKANTAYHTEYKSIEN TESTAUS
# ============================

import pytest # Virheilmoitusten testaus vaatii
from lendingModules import dbOperations # Testattava moduuli

settingsDictionary = {'server': 'localhost',
                      'port': '5433',
                      'database': 'testaus',
                      'userName': 'postgres',
                      'password': 'Q2werty'}

newValues = {'etunimi': 'Ossian',
             'sukunimi': 'Onneton'}

dbConnection = dbOperations.DbConnection(settingsDictionary)

# Testataan, että yhteysmerkkijono muodostuu oikein
def test_connectionString():
    assert dbConnection.connectionString == f'dbname=testaus user=postgres password=Q2werty host=localhost port=5433'

#  Testataan, että taulun kaikki tiedot saadaan ja ensimmäinen rivi on Ville Virtanen
def test_readOneRow():
    resultList = dbConnection.readAllColumnsFromTable('person') # Hakee taulun kaikki rivit listaan
    assert resultList[0] == (1, 'Ville', 'Virtanen') # Ensimmäinen rivi pitäisi olla 1 Ville Virtanen

# Testataan tietueen / rivin (record / row) lisäys tauluun (table)
def test_addRow():
    dbConnection.addToTable('person', newValues)
    resultList = dbConnection.readAllColumnsFromTable('person')
    rowCount = len(resultList)
    assert resultList[rowCount-1] == (rowCount, 'Ossian', 'Onneton')