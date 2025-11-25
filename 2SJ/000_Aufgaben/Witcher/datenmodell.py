import psycopg

class Datenbank:
    def __init__(self, password:str, setup=False) -> None:
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
            print(e, type(e))
        db_conn: psycopg.Connection
        try:
            with psycopg.connect(**self.config_witcher) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.execute('''
                                   CREATE TABLE witcher_characters
                                   (
                                       id                  BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                       name                TEXT NOT NULL,
                                       species             TEXT,
                                       gender              TEXT,
                                       age_group           TEXT,
                                       origin_or_region    TEXT,
                                       affiliation         TEXT,
                                       role_or_occupation  TEXT,
                                       notable_traits      TEXT,
                                       abilities_or_skills TEXT,
                                       first_appearance    TEXT,

                                       strength            INTEGER CHECK (strength BETWEEN 0 AND 100),
                                       health              INTEGER CHECK (health BETWEEN 0 AND 100),
                                       mana                INTEGER CHECK (mana BETWEEN 0 AND 100),
                                       level               INTEGER CHECK (level BETWEEN 0 AND 100)
                                   )
                                   ''')
        except psycopg.DatabaseError as e:
            print(e, type(e))

    def befuellen_db(self):
        db_conn: psycopg.Connection
        helden = set()
        with open('data.txt') as f:
            liste = []
            f.readline()
            # print('Name,Species,Gender,Age_Group,Origin_or_Region,Affiliation,Role_or_Occupation,Notable_Traits,Abilities_or_Skills,First_Appearance,Strength,Health,Mana,Level'.lower())
            for zeile in f:
                liste.append(zeile.replace('"', '').strip().split(','))
            print(liste)
            #for zeile in f.read().split('\n'):
            #    name, species, gender, age_group, origin_or_region, affiliation, role_or_occupation, notable_traits, abilities_or_skills, first_appearance, strength, health, mana, level = zeile.replace('"', '').split(',')
            #    helden.add((name, species, gender, age_group, origin_or_region, affiliation, role_or_occupation, notable_traits, abilities_or_skills, first_appearance, int(strength), int(health), int(mana), int(level)))

        try:
            with psycopg.connect(**self.config_witcher) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.executemany('''INSERT INTO witcher_characters (name, species, gender, age_group,
                                                                          origin_or_region, affiliation,
                                                                          role_or_occupation, notable_traits,
                                                                          abilities_or_skills, first_appearance,
                                                                          strength, health, mana, level)
                                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )

                                       ''', helden)
        except psycopg.DatabaseError as e:
            print(e, type(e))

    def lesen(self):
        character = []
        db_conn: psycopg.Connection
        try:
            with psycopg.connect(**self.config_witcher) as db_conn:
                with db_conn.cursor() as cursor:
                    for held in cursor.execute('''SELECT * FROM witcher_characters''').fetchall():
                        id, name, species, gender, age_group, origin_or_region, affiliation, role_or_occupation, notable_traits, abilities_or_skills, first_appearance, strength, health, mana, level = held
                        witcher_dict ={
                            "Name": name,
                            "Species": species,
                            "Gender": gender,
                            "Age_Group": age_group,
                            "Origin_or_Region": origin_or_region,
                            "Affiliation": affiliation,
                            "Role_or_Occupation": role_or_occupation,
                            "Notable_Traits": notable_traits,
                            "Abilities_or_Skills": abilities_or_skills,
                            "First_Appearance": first_appearance,
                            "Strength": strength, "Health": health, "Mana": mana, "Level": level,
                            "Image": f"bilder/{id}.png",
                        }
                        character.append(witcher_dict)
        except psycopg.DatabaseError as e:
            print(e, type(e))

        return character

# witcherDB = Datenbank('password', setup=True)
witcherDB = Datenbank('password')
witcherDB.befuellen_db()
witcherDB.lesen()
