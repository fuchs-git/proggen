import psycopg
from psycopg.rows import dict_row

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
            # cursor.execute('SELECT name, alter FROM person;')
            # print(cursor.fetchall())
            # for name, alter in cursor.fetchall():
            #     print(name, alter)

            # besser
            for name, alter in cursor.execute('select name, alter from person;'):
                print(name, alter)

        # als Dictionary
        # with db_conn.cursor(row_factory=dict_row) as cursor:
        #     cursor.execute('SELECT id, name, alter FROM person')
        #     for row in cursor.fetchall():
        #         print(row)

except psycopg.DatabaseError as e:
    print(e, type(e))