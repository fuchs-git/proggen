import psycopg

try:
    # Automatisches close (wie bei Dateien)
    with psycopg.connect(dbname="postgres",
                         user="postgres",
                         password="password",
                         host="localhost",
                         port="5432",
                         autocommit=True) as db_conn:

        with db_conn.cursor() as cursor:
            cursor.execute('CREATE DATABASE prg_fitness')

except psycopg.errors.DuplicateDatabase:
    print('Datenbank existiert bereits.')
    pass
except psycopg.DatabaseError as e:
    print(e, type(e))

# Manuelles schließen
# cursor = db_conn.cursor()
# cursor.execute('CREATE DATABASE prg_fitness')
# cursor.close()
# db_conn.close()
