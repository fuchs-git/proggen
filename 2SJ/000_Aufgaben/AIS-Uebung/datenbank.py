import psycopg


class Datenbank:
    def __init__(self, password: str, install: bool = False):
        self.config_setup = {'user': 'postgres',
                             'password': password,
                             'dbname': 'postgres',
                             'host': 'localhost',
                             'port': 5432,
                             'autocommit': True}
        self.config_ais = {'user': 'postgres',
                           'password': password,
                           'dbname': 'ais',
                           'host': 'localhost',
                           'port': 5432,
                           'autocommit': True}

        if install:
            self.erstelle_db()

    def erstelle_db(self):

        try:
            db_conn: psycopg.Connection
            with psycopg.connect(**self.config_setup) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.execute('DROP DATABASE IF EXISTS ais')
                    cursor.execute('CREATE DATABASE ais')
        except psycopg.DatabaseError as e:
            print(e, type(e))

        try:
            db_conn: psycopg.Connection
            with psycopg.connect(**self.config_ais) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.execute("""
                                   CREATE TABLE vessel (
                                       mmsi INT PRIMARY KEY,
                                       name TEXT,
                                       typ  TEXT
                                   )
                                   """)

                    cursor.execute("""
                                   CREATE TABLE aisdata (
                                       mmsi         INT REFERENCES vessel (mmsi),
                                       basedatetime TIMESTAMP,
                                       lat          DECIMAL,
                                       lon          DECIMAL,
                                       PRIMARY KEY (mmsi, basedatetime))""")
        except psycopg.DatabaseError as e:
            print(e, type(e))

if __name__ == '__main__':
    # db = Datenbank('password', install=True)
    ...
