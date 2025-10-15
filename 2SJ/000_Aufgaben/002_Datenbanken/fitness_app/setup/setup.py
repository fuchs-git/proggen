'''
Datenbank anlegen und Tabellen erzeugen
'''
import psycopg
import time

db_conn: psycopg.Connection  # type hint für PyCharm
# ---------------------------------------------------------------------------------------------------------------------
# Erstellung der Datenbank prg_fitness
# ---------------------------------------------------------------------------------------------------------------------

setup_start = time.time()

try:
    with psycopg.connect(dbname="postgres",
                         user="postgres",
                         password="password",
                         host="localhost",
                         port="5432",
                         autocommit=True) as db_conn:
        with db_conn.cursor() as cursor:
            cursor.execute('DROP DATABASE IF EXISTS prg_fitness_app')
            cursor.execute('CREATE DATABASE prg_fitness_app')

    print('===> Datenbank "prg_fitness_app" wurde erzeugt')
    # -----------------------------------------------------------------------------------------------------------------
    # Verbindung zur Datenbank prg_fitness_app
    # -----------------------------------------------------------------------------------------------------------------
    with psycopg.connect(dbname="prg_fitness_app",
                         user="postgres",
                         password="password",
                         host="localhost",
                         port="5432",
                         autocommit=True) as db_conn:

        # -------------------------------------------------------------------------------------------------------------
        # Erstellung der Tabellen
        # -------------------------------------------------------------------------------------------------------------
        with db_conn.cursor() as cursor:

            cursor.execute('''CREATE TABLE person (
                id    INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name  TEXT    NOT NULL,
                alter INTEGER NOT NULL
            )''')
            print('===> Tabelle "person" wurde erzeugt')

        # -------------------------------------------------------------------------------------------------------------

            try:
                cursor.execute("DROP TABLE IF EXISTS person_zeitslot;")
                cursor.execute("DROP TABLE IF EXISTS zeitslot;")
            except psycopg.errors.UndefinedTable:
                print('Tabelle Zeitslots wird neu angelegt.')

            cursor.execute('''
                           CREATE TABLE zeitslot (
                               id        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                               wochentag INTEGER NOT NULL CHECK (wochentag BETWEEN 1 AND 7),
                               startzeit TIME    NOT NULL,
                               endzeit   TIME    NOT NULL
                           );
                           ''')

            print('===> Tabelle "zeitslot" wurde erzeugt')

        # -------------------------------------------------------------------------------------------------------------

            try:
                cursor.execute('DROP TABLE person_zeitslot;')
            except psycopg.errors.UndefinedTable:
                cursor.execute('''
                               CREATE TABLE person_zeitslot (
                                   person_id   INTEGER NOT NULL REFERENCES person (id) ON DELETE CASCADE,
                                   zeitslot_id INTEGER NOT NULL REFERENCES zeitslot (id) ON DELETE CASCADE,
                                   PRIMARY KEY (person_id, zeitslot_id)
                               );
                               ''')
            print('===> Tabelle "person_zeitslot" wurde erzeugt')

        # -------------------------------------------------------------------------------------------------------------

            with db_conn.cursor() as cursor:
                cursor.execute('''
                               CREATE TABLE bilder (
                                   person INTEGER PRIMARY KEY,
                                   bild   bytea,
                                   FOREIGN KEY (person) REFERENCES person (id)
                               )''')
                print('===> Tabelle "bilder" wurde erzeugt')

        # -------------------------------------------------------------------------------------------------------------
        # Befüllung der Tabelle Zeitslots
        # -------------------------------------------------------------------------------------------------------------

                slots = []
                for wtag in range(1, 8):
                    for stunden in range(8, 22, 2):
                        start = f'{stunden:02d}:00'
                        ende = f'{stunden + 2:02d}:00'
                        slots.append((wtag, start, ende))

                cursor.executemany('INSERT INTO zeitslot(wochentag, startzeit, endzeit) VALUES (%s, %s, %s)', slots)
            print('===> Tabelle "person_zeitslot" wurde befüllt')


except psycopg.DatabaseError as e:
    print(e, type(e))

print(f'===> Setup in {time.time() - setup_start:.2f} Sekunden abgeschlossen')
