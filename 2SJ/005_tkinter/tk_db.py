import psycopg
from psycopg.rows import dict_row

class Datenbank:

    def createDB(self):
        try:
            with psycopg.connect(dbname="postgres",
                                 user="postgres",
                                 password="password",
                                 host="localhost",
                                 port="5432",
                                 autocommit=True) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.execute('CREATE DATABASE tk_click')

        except psycopg.DatabaseError as e:
            print(e, type(e))

    def createTbl(self):
        with psycopg.connect(dbname="tk_click",
                             user="postgres",
                             password="password",
                             host="localhost",
                             port="5432",
                             autocommit=True) as db_conn:
            with db_conn.cursor() as cursor:
                cursor.execute('CREATE TABLE speicher (zahl INTEGER NOT NULL)')
                cursor.execute('insert into speicher (zahl) VALUES (0)')

    def speichern(self, wert):
        with psycopg.connect(dbname="tk_click",
                             user="postgres",
                             password="password",
                             host="localhost",
                             port="5432",
                             autocommit=True) as db_conn:
            with db_conn.cursor() as cursor:
                cursor.execute('UPDATE speicher set zahl = %s', (wert,))

    def read(self):
        with psycopg.connect(dbname="tk_click",
                             user="postgres",
                             password="password",
                             host="localhost",
                             port="5432",
                             autocommit=True) as db_conn:
            with db_conn.cursor() as cursor:
                cursor.execute('SELECT zahl from speicher')
                return cursor.fetchone()[0]