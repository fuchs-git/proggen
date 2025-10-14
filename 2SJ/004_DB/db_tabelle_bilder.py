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
        # Tabelle erzeugen
        # -------------------------------------------------------------------------------------------------------------
        with db_conn.cursor() as cursor:
            cursor.execute('''
                           CREATE TABLE bilder (
                               person INTEGER PRIMARY KEY,
                               bild   bytea,
                               FOREIGN KEY (person) REFERENCES person (id)
                           )''')

except psycopg.DatabaseError as e:
    print(e, type(e))