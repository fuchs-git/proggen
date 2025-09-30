import psycopg

db_conn = psycopg.connect(dbname="postgres",
                          user="postgres",
                          password="password",
                          host="localhost",
                          port="5432",
                          autocommit=True)
cursor = db_conn.cursor()
cursor.execute('CREATE DATABASE prg_fitness')
cursor.close()
db_conn.close()
