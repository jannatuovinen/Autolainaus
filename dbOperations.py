# MODUULI POSTGRESQL TIETOKANTAPALVELIMEN KÄYTTÄMISEEN
# ====================================================

# KIRJASTOT JA MODUULIT
# ---------------------

# Ladattavat kirjastot
import psycopg2

# Sisäiset kirjastot
import json

# Omat moduulit
import cipher


# LUOKAT
# ------

class DbConnection():
    """A class to crate PostgreSQL Database connections and various data operations"""
    
    # Konstruktori
    def __init__(self, settings: dict):
        self.server = settings['server']
        self.port = settings['port']
        self.databaseName = settings['database']
        self.userName = settings['userName']
        self.password = settings['password']

        # Yhteysmerkkijono
        self.connectionString = f'dbname={self.databaseName} user={self.userName} password={self.password} host={self.server} port={self.port}'

        
        print("Yhteysmerkkijono on:", self.connectionString)
    # Metodi tietojen lisäämiseen (INSERT)
    def  addToTable(self, table: str, data: dict) -> str:
        """Inserts a record (row) to a table according to a dictionary
        containing field names (columns) as keys and values

        Args:
            table (str): Name of the table
            data (dict): Fields names and values

        Returns:
            str: Information about succesfull operation or an error message
        """

        # Muodostetaan lista sarakkeiden (kenttien) nimistä ja arvoista SQL lausetta varten
        keys = data.keys() # Luetaan sanakirjan avaimet
        columns = '' # SQL-lauseeseen tarvittava sarakelista
        values = '' # SQL-lauseen arvot merkkijonona

        # Luetaan kaikki avaimet sekä arvot ja lisätään ne listoihin
        for key in keys:
            columns += key + ', ' # Lisätään pilkku
            rawValue = data[key]

            # Lisätään puolilainausmerkit, jos kyseessä on merkkijono
            if isinstance(rawValue, str):
                value = f'\'{rawValue}\'' # \'mahdollistaa puolilainausmerkin lisäämisen
            else: 
                value = rawValue
            values += value + ', ' # lisätään arvo sekä pilkku ja välilyönti

        # Poistetaan sarakkeista ja arvoista viimeinen pilkku ja välilyönti
        columns = columns[:-2]
        values = values[:-2]

        # Määritellään tilaviestiksi tyhjä merkkijono
        message = ''

        # Yritetään avata yhteys tietokantaan ja lisätä tietue
        try:
            # Luodaan yhteys tietokantaan
            currentConnection = psycopg2.connect(self.connectionString)

            # Luodaan kursosi suorittamaan tietokantaoperaatiota
            cursor = currentConnection.cursor()

            # Määritellään lopullinen SQL-lause
            sqlClause = f'INSERT INTO {table} ({columns}) VALUES ({values})'
            print('SQL-lause omn:', sqlClause)

            # Suoritetaan SQL-lause
            cursor.execute(sqlClause)

            # Vahvistetaan tapahtuma (transaction)
            currentConnection.commit()

        except (Exception, psycopg2.Error) as e:
            message = 'Tietokantayhteyden muodostamisessa tapahtui virhe: ' + str(e)

        finally:
            if message == '':
                message = f'Tietue lisättiin tauluun {table}'

            # Selvitetään muodostuiko yhteysolio
            if currentConnection:
                cursor.close() # Tuhotaan kursori
                currentConnection.close() # Tuhotaan yhteys

            return message
        
if __name__ == "__main__":

    testDictionary = {'server': '127.0.0.1',
                      'port': '5432',
                      'database': 'testi',
                      'userName': 'user',
                       'password': 'salasana'}
    
    tableDictionary = {'etunimi': 'Uolevi',
                       'sukunimi': 'Untamo'}
    

    dbConnection = DbConnection(testDictionary)

    print('Yhteysmerkkijono on:', dbConnection.connectionString)

    dbConnection.addToTable('testitaulu', tableDictionary)