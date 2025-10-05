import psycopg

db_conn = psycopg.connect(dbname='prg_fitness',
                          user='postgres',
                          password='password',
                          host='localhost',
                          port='5432',
                          autocommit=True)
cursor = db_conn.cursor()

#cursor.execute('''INSERT INTO person (name, alter) VALUES ('Anton', 47)''')

# Anzeige
cursor.execute('''SELECT * from person''')
for zeile in cursor.fetchall():
    print(zeile)
# (1, 'Anton', 47)
# (2, 'Anton', 47)
# (3, 'Anton', 47)


print(*cursor.fetchall())
# [(1, 'Anton', 47), (2, 'Anton', 47), (3, 'Anton', 47)]

# Daten löschen
cursor.execute('''DELETE FROM person WHERE id>0''')
print(cursor.rowcount)
print(cursor.fetchall)


# Daten einfügen
# personen = [('Anton', 47), ('Brita', 53), ('Charlie', 23), ('Denise', 27), ('Emil', 64), ('Frank', 81)]
# for person in personen:
#     cursor.execute('''INSERT INTO person (name,alter) VALUES (%s, %s)''', person)

personen = [('Anton', 47), ('Brita', 53), ('Charlie', 23), ('Denise', 27), ('Emil', 64), ('Frank', 81)]
with db_conn.cursor() as cursor:
    cursor.executemany('INSERT INTO person (name,alter) VALUES (%s, %s)', personen)
