'''
Aufgabe:
Ergänzen Sie die Datenbank prg_fitness um eine weitere Tabelle zeitslot. Hier sollen für jeden Tag der Woche die
Doppelstunden von 08:00 bis 22:00 bereits initial erfasst sein (nicht überlappend).

Die Idee ist, dass sich später Sporttreibende in diese eintragen können und auch die Möglichkeiten haben zu sehen,
wie stark das Studio in diesem Zeitslot ausgelastet sein wird.
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
        # Zeitslot Tabelle erstellen
        # -------------------------------------------------------------------------------------------------------------

        with db_conn.cursor() as cursor:
            try:
                cursor.execute('DROP TABLE zeitslot;')
            except psycopg.errors.UndefinedTable:
                print('Tabelle Zeitslots wird neu angelegt.')

            cursor.execute('''
                           CREATE TABLE zeitslot
                           (
                               id        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                               wochentag integer not null check (wochentag between 1 and 7),
                               startzeit TIME    NOT NULL,
                               endzeit   TIME    NOT NULL
                           );
                           ''')

            # ----------------------------------------------------------------------------------------------------------
            # Befüllung der Tage
            # ----------------------------------------------------------------------------------------------------------
            slots = []
            for wtag in range(1, 8):
                for stunden in range(8, 22,2):
                    start = f'{stunden:02d}:00'
                    ende = f'{stunden + 2:02d}:00'
                    slots.append((wtag, start, ende))
                cursor.executemany('INSERT INTO zeitslot(wochentag, startzeit, endzeit) VALUES (%s, %s, %s)', slots)

except psycopg.DataError as e:
    print(e, type(e))
