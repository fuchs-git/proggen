import psycopg

class Datenbank:
    def __init__(self, password:str, setup=False) -> None:
        self.befuellen_db()
        self.config_setup = {'user': 'postgres',
                       'password': password,
                       'dbname': 'postgres',
                       'host': 'localhost',
                       'port': 5432,
                       'autocommit': True}
        self.config_witcher = {'user': 'postgres',
                             'password': password,
                             'dbname': 'witcher',
                             'host': 'localhost',
                             'port': 5432,
                             'autocommit': True}

        if setup: self.erstelle_db()

    def erstelle_db(self):
        db_conn: psycopg.Connection
        try:
            with psycopg.connect(**self.config_setup) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.execute('DROP DATABASE IF EXISTS witcher')
                    cursor.execute('CREATE DATABASE witcher')
        except psycopg.DatabaseError as e:
            print('Setup Fehler', e, type(e))

        db_conn: psycopg.Connection
        try:
            with psycopg.connect(**self.config_witcher) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.execute('DROP DATABASE IF EXISTS witcher')
                    cursor.execute('CREATE DATABASE witcher')
        except psycopg.DatabaseError as e:
            print('Setup Fehler', e, type(e))

    def befuellen_db(self):
        helden = []
        with open("data.txt", "r") as f:
            f.readline()
            #name, species, gender, age_Group, origin_or_Region, affiliation, role_or_Occupation, notable_Traits, abilities_or_Skills, first_Appearance, strength, health, mana, level
            for line in f.read().split('\n'):
                helden.append(line.replace('"','').split(','))
            print(*helden)


#witcher = Datenbank('password', setup=True)



