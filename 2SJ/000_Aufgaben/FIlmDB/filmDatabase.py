import psycopg
from datensachen import personen_liste, filme_liste, rollen_liste


class Datenbank:
    def __init__(self, password: str, setup=False):
        self.config_setup = {'user': 'postgres',
                             'password': password,
                             'dbname': 'postgres',
                             'host': 'localhost',
                             'port': 5432,
                             'autocommit': True}
        self.config_filmDB = {'user': 'postgres',
                              'password': password,
                              'dbname': 'filmdb',
                              'host': 'localhost',
                              'port': 5432,
                              'autocommit': True}

        if setup: self.db_erstellen()

    def db_erstellen(self):
        db_conn: psycopg.Connection
        try:
            with psycopg.connect(**self.config_setup) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.execute('DROP DATABASE IF EXISTS filmDB')
                    cursor.execute('CREATE DATABASE filmDB')
        except psycopg.DatabaseError as e:
            print(e, type(e))

        try:
            with psycopg.connect(**self.config_filmDB) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.execute("""CREATE TABLE person
                                      (
                                          person_id  BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                          nachname   TEXT NOT NULL,
                                          vorname    TEXT NOT NULL,
                                          geburtstag DATE NOT NULL
                                      );""")

                    cursor.execute("""CREATE TABLE film
                                      (
                                          film_id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                          titel            TEXT    NOT NULL,
                                          erscheinungsjahr INTEGER NOT NULL,
                                          fk_regie         BIGINT  NOT NULL REFERENCES person (person_id)
                                              ON UPDATE CASCADE ON DELETE RESTRICT
                                      );""")

                    cursor.execute("""CREATE TABLE hat_mitgespielt_in
                                      (
                                          fk_filme_id  BIGINT REFERENCES film (film_id),
                                          fk_person_id BIGINT REFERENCES person (person_id),
                                          rolle        TEXT NOT NULL,
                                          PRIMARY KEY (fk_filme_id, fk_person_id)
                                      );""")

        except psycopg.DatabaseError as e:
            print(e, type(e))

    def db_befuellen(self):
        db_conn: psycopg.Connection
        try:
            with psycopg.connect(**self.config_filmDB) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.executemany('''INSERT INTO person (nachname, vorname, geburtstag)
                                          VALUES (%s, %s, %s)''',
                                       personen_liste)
                    cursor.executemany(
                        '''INSERT INTO film(titel, erscheinungsjahr, fk_regie)
                           VALUES (%s, %s, (SELECT person_id FROM person WHERE nachname = %s))''',
                        filme_liste)
                    cursor.executemany(
                        '''INSERT INTO hat_mitgespielt_in(fk_filme_id, fk_person_id, rolle)
                           VALUES ((SELECT film_id FROM film WHERE titel LIKE %s),
                                   (SELECT person_id FROM person WHERE nachname = %s), %s)''',
                        rollen_liste)
        except psycopg.DatabaseError as e:
            print(e, type(e))

    def filme(self):
        db_conn: psycopg.Connection
        try:
            with psycopg.connect(**self.config_filmDB) as db_conn:
                with db_conn.cursor() as cursor:
                    return cursor.execute('''SELECT * FROM film''').fetchall()
        except psycopg.DatabaseError as e:
            print(e, type(e))

    def schauspieler(self):
        db_conn: psycopg.Connection
        try:
            with psycopg.connect(**self.config_filmDB) as db_conn:
                with db_conn.cursor() as cursor:
                    return cursor.execute('''SELECT f.titel    AS film,
                                                    p.nachname AS schauspieler_nachname,
                                                    p.vorname  AS schauspieler_vorname,
                                                    h.rolle    AS rolle
                                             FROM hat_mitgespielt_in h
                                                      JOIN film f
                                                           ON h.fk_filme_id = f.film_id
                                                      JOIN person p
                                                           ON h.fk_person_id = p.person_id''').fetchall()
        except psycopg.DatabaseError as e:
            print(e, type(e))

    def regisseur(self):
        db_conn: psycopg.Connection
        try:
            with psycopg.connect(**self.config_filmDB) as db_conn:
                with db_conn.cursor() as cursor:
                    return cursor.execute('''SELECT f.titel            AS film,
                                                    p.nachname         AS regisseur_nachname,
                                                    p.vorname          AS regisseur_vorname,
                                                    f.erscheinungsjahr AS jahr
                                             FROM film f
                                                      JOIN person p
                                                           ON f.fk_regie = p.person_id''').fetchall()
        except psycopg.DatabaseError as e:
            print(e, type(e))



filme = Datenbank(password='password', setup=False)