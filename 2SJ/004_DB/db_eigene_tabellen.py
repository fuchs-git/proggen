import psycopg

try:
    with psycopg.connect(dbname="postgres",
                         user="postgres",
                         password="password",
                         host="localhost",
                         port="5432",
                         autocommit=True) as db_conn:
        with db_conn.cursor() as cursor:
            cursor.execute('DROP DATABASE IF EXISTS prg_fitness')
            cursor.execute('CREATE DATABASE prg_fitness')

    with psycopg.connect(dbname="prg_fitness",
                         user="postgres",
                         password="password",
                         host="localhost",
                         port="5432",
                         autocommit=True) as db_conn:
        with db_conn.cursor() as cursor:
            try:
                cursor.execute('DROP TABLE person;')
            except psycopg.errors.UndefinedTable:
                print('Lege Tabelle neu an')
            cursor.execute('''CREATE TABLE person (
                                  id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                  name TEXT NOT NULL,
                                  alter INTEGER NOT NULL
                              )''')

except psycopg.DatabaseError as e:
    print(e, type(e))