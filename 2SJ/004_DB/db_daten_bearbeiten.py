import random

import psycopg

db_conn: psycopg.Connection
try:
    with psycopg.connect(dbname="prg_fitness",
                         user="postgres",
                         password="password",
                         host="localhost",
                         port="5432",
                         autocommit=True) as db_conn:
        # Code säubern mit psycopg
        with db_conn.cursor() as cursor:
            namen = 'Jan Johan Nico Neiko Pawel Pascal Vikor Wolfi'.split()
            for name in namen:
                cursor.execute('''INSERT INTO person (name, alter) VALUES (%s, %s) RETURNING id, name, alter''',(name, random.randint(25,65)))
                print(cursor.fetchone())

            cursor.execute('''INSERT INTO person (name, alter) VALUES (%s, %s)''',('Marco\');Drop Table person;-- -', random.randint(25,65)))


        # Daten werden schneller in die DB eingefügt und nicht mehr Stück für Stück
        personen = [('Anton', 47), ('Brita', 53), ('Charlie', 23), ('Denise', 27), ('Emil', 64), ('Frank', 81)]
        with db_conn.cursor() as cursor:
            cursor.executemany('INSERT INTO person (name,alter) VALUES (%s, %s)', personen)
            print(cursor.rowcount)

except psycopg.DatabaseError as e:
    print(e, type(e))