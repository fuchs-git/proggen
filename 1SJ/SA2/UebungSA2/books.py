books_dataset = [
    ("Der Hobbit", "J.R.R. Tolkien", 1937, "978-3-86680-192-9"),
    ("The Lord of the Rings", "J.R.R. Tolkien", 1954, "978-3-86680-193-6"),
    ("To Kill a Mockingbird", "Harper Lee", 1960, "0-06-112008-1"),
    ("Go Set a Watchman", "Harper Lee", 2015, "978-0-06-240985-0"),
    ("1984", "George Orwell", 1949, "978-3-596-19063-1"),
    ("Animal Farm", "George Orwell", 1945, "978-0-452-28423-4"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "978-3-15-009039-6"),
    ("Tender Is the Night", "F. Scott Fitzgerald", 1934, "978-0-7432-7356-0"),
    ("Pride and Prejudice", "Jane Austen", 1813, "978-1-85326-000-0"),
    ("Sense and Sensibility", "Jane Austen", 1811, "978-0-14-043550-1"),
    ("One Hundred Years of Solitude", "Gabriel Garcia Marquez", 1967, "978-0-06-088328-7"),
    ("Love in the Time of Cholera", "Gabriel Garcia Marquez", 1985, "978-0-307-47436-1"),
    ("The Catcher in the Rye", "J.D. Salinger", 1951, "978-0-316-76948-0"),
    ("Franny and Zooey", "J.D. Salinger", 1961, "978-0-316-76946-6"),
    ("The Chronicles of Narnia", "C.S. Lewis", 1950, "978-0-06-623850-0"),
    ("The Screwtape Letters", "C.S. Lewis", 1942, "978-0-06-065293-7"),
    ("Moby-Dick", "Herman Melville", 1851, "978-0-553-21311-9"),
    ("Bartleby, the Scrivener", "Herman Melville", 1853, "978-0-19-953635-9"),
    ("The Shining", "Stephen King", 1977, "978-0-385-12167-5"),
    ("It", "Stephen King", 1986, "978-0-670-81302-8"),
    ("Der Prozess", "Franz Kafka", 1925, "978-3-596-90155-0"),  # Weitere Bücher hinzugefügt
]  # Fügen Sie hier zur Übung mal weitere Bücher hinzu ...


# 1. Aufgabe
# Erstelle eine Klasse Buch. Bücher kennen ihren Titel, den Autor, den Jahrgang der Ausgabe und ihre ISBN-Nummer.
class Books:
    """
    meine Buch Klasse :-*
    """
    def __init__(self, titel, autor, jahr, isbn):
        self.titel = titel
        self.autor = autor
        self.jahr = jahr
        self.isbn = isbn
        self.status = False

    def __repr__(self):
        return f'{self.titel} - {self.autor} - {self.jahr}' #// {"gelesen" if self.status else "ungelesen"}'

    def gelesen(self):
        self.status = True


class Buchsammlung:
    "Das ist meine Buchsammlung"
    def __init__(self, sammlung):
        self.sammlung = sammlung

    def __str__(self):
        for item in self.sammlung:
            print(item)
        return "\b" # SCHMUTZ!!!

    def anzahl(self):
        return len([x for x in self.sammlung])

    def hinzu(self, buch):
        if buch in self.sammlung:
            print(f'Das Buch "{buch}" ist bereits in der Sammlung.')
        else:
            print(f'Das Buch "{buch}" wurde hinzugefügt.')
            a = [x for x in self.sammlung]
            a.append(buch)
            self.sammlung = a

    def autor(self, autor):
        return [x for x in self.sammlung if x.autor == autor]
        #return [x for x in self.sammlung if x.autor == autor]
        # return f'Bücher von {autor}: ' +" // ".join([x.titel for x in a])

    def lesen(self):
        for b in self.sammlung:
            if not b.status:
                b.gelesen()
                return f'{b.titel} - {"gelesen" if b.status else "ungelesen"}.'

    def ungelesen(self):
        return len([x for x in self.sammlung if not x.status])

    def sortieren(self):
        return [(x.jahr, x.titel) for x in self.sammlung]



buchsammlung = [Books(*x) for x in books_dataset]
#print(*buchsammlung, sep='\n')

# Zudem wissen Bücher, ob sie schon gelesen wurden. Bei Erstellung eines Buches ist es anfangs immer ungelesen.
# Ein Buch kann sich selbst darstellen im Format: Titel - Autor - Jahrgang
buch = Books("Das Leiden", "FSBwIT", 2025,"1337-7331-42-0")
buch.gelesen()
#print(buch)


# 2. Aufgabe
# Erstelle eine Klasse Buchsammlung. Eine Buchsammlung kennt all seine Bücher und die Anzahl der Bücher.
bs = Buchsammlung(buchsammlung)
# print(bs.anzahl())

# Die Buchsammlung kann sich selbst darstellen, indem alle Bücher untereinander ausgegeben werden.
# print(bs)

# Man kann der Buchsammlung ein Buch hinzufügen, solange noch kein Buch mit dem gleichen Titel, Autor und Jahrgang
# vorhanden ist. Der Anwender ist über einen sinnvollen Rückgabewert zu informieren, ob das Hinzufügen erfolgreich was
# oder nicht.
# Fügen Sie der Buchsammlung alle Bücher aus der Variablen books_dataset hinzu.
# Fügen Sie der Buchsammlung ein zusätzliches Buch hinzu.
bs.hinzu(buch)
bs.hinzu(buch)

# Man kann sich von der Buchsammlung eine Liste aller Bücher eines bestimmten Autors ausgeben lassen.

print(bs.autor('Gabriel Garcia Marquez'))


# Man kann in der Buchsammlung lesen. Dazu wird das erste ungelesene Buch zurückgegeben und dessen Status auf gelesen
# gesetzt. Wurden schon alle Bücher gelesen, wird ein zufälliges Buch zurückzugeben.

print(bs.lesen())
print(bs.lesen())
print(bs.lesen())

# Man kann die Buchsammlung nach der Anzahl der ungelesenen Bücher fragen.
print(bs.ungelesen())

# Man kann die Bücher der Buchsammlung nach dem Jahrgang sortiert ausgeben lassen.
print(bs.sortieren())
# Hinweis:
# "sich selbst darstellen" bedeutet, "auf Nachfrage eine entsprechende String-Repräsentation liefern"
# "Man kann" bedeutet, dass die Klasse das kann, wenn man sie danach fragt.
# "eine Klasse fragen" bedeutet, sich von einer Methode der Klasse etwas zurückgeben lassen

print(f'\n aaa')
