
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

cursor.executemany('INSERT INTO person (nachname, vorname, geburtstag) VALUES (%s,%s,%s)', LISTE)

cursor.executemany(
    'INSERT INTO film(titel, erscheinungsjahr, fk_regie) VALUES  (%s, %s, (SELECT person_id FROM person WHERE nachname = %s))',
    LISTE)

cursor.executemany(
    'INSERT INTO hat_mitgespielt_in(fk_filme_id, fk_person_id, rolle) VALUES ((SELECT film_id FROM film WHERE titel LIKE %s), (SELECT person_id FROM person WHERE nachname = %s),%s)',
    LISTE)
