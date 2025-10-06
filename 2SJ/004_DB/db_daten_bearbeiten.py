import psycopg

with psycopg.connect(dbname="prg_fitness",
                     user="postgres",
                     password="password",
                     host="localhost",
                     port="5432",
                     autocommit=True) as db_conn:
    with db_conn.cursor() as cursor:
        ...
