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
        # DB nutzen
        # -------------------------------------------------------------------------------------------------------------

        with db_conn.cursor() as cursor:
            for name, alter in cursor.execute('SELECT name, alter FROM person;'):
                print(name, alter)

        # -------------------------------------------------------------------------------------------------------------
        # Bild in die Datenbank speichern
        # -------------------------------------------------------------------------------------------------------------
        with db_conn.cursor() as cursor:
            with open('avatar2.png', 'rb') as datei:
                bild = datei.read()
                cursor.execute('INSERT INTO bilder (person,bild) VALUES (%s,%b)', (2, bild))



except psycopg.DatabaseError as e:
    print(e, type(e))
