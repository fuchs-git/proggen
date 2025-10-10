'''
Zeitslots mit Sporttreibenden
Ergänzen Sie nun die Datenbank prg_fitness um die Möglichkeit, Beziehungen zwischen Personen (Sporttreibenden)
und Zeitslots erfassen zu können.

Sporttreibende können dabei mehr als einen Zeitslot wählen und ein Zeitslot kann auch von mehreren Sporttreibenden
gewählt werden.
'''

import psycopg

db_conn: psycopg.Connection  # type hint für PyCharm
# ---------------------------------------------------------------------------------------------------------------------
# Verbindung mit der DB aufbauen
# ---------------------------------------------------------------------------------------------------------------------

try:
    with psycopg.connect(dbname="prg_fitness",
                         user="postgres",
                         password="password",
                         host="localhost",
                         port="5432",
                         autocommit=True) as db_conn:
        # -------------------------------------------------------------------------------------------------------------
        # Person-Zeitslot Tabelle erstellen
        # -------------------------------------------------------------------------------------------------------------

        with db_conn.cursor() as cursor:
            try:
                cursor.execute('DROP TABLE person_zeitslot;')
            except psycopg.errors.UndefinedTable:
                print('Tabelle person_zeitslot wird neu angelegt.')
            cursor.execute('''
                           CREATE TABLE person_zeitslot
                           (
                               person_id   INTEGER NOT NULL REFERENCES person (id),
                               zeitslot_id INTEGER NOT NULL REFERENCES zeitslot (id),
                               PRIMARY KEY (person_id, zeitslot_id)
                           );
                           ''')


except psycopg.DatabaseError as e:
    print(e, type(e))