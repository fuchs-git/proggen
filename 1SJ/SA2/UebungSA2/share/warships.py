# Aufgabe: World of Warships - Flottenmanagement-System
# Kontext:
# Im Spiel "World of Warships" verwalten Spieler ihre Flotte von Kriegsschiffen, die unterschiedlichen Nationen und Schiffstypen angehören. Du sollst ein Flottenmanagement-System erstellen, das es erlaubt, Schiffe zu verwalten, ihre Einsätze zu planen und Statistiken zu berechnen.
#
# Dataset:
# Das Dataset besteht aus einer Liste von Kriegsschiffen mit den folgenden Attributen:
# Name des Schiffes (z. B. "Bismarck")
# Nation (z. B. "Deutschland", "USA", "Japan")
# Schiffstyp (z. B. "Schlachtschiff", "Zerstörer", "Kreuzer", "Flugzeugträger")
# Panzerung (in mm)
# Feuerkraft (in Punkten)
# Geschwindigkeit (in Knoten)
# Status (z. B. "einsatzbereit", "in Reparatur", "versenkt")
# Beispiel-Dataset:

kriegsschiffe = [
    ("Bismarck", "Deutschland", "Schlachtschiff", 320, 850, 30, "einsatzbereit"),
    ("Yamato", "Japan", "Schlachtschiff", 410, 920, 27, "einsatzbereit"),
    ("Missouri", "USA", "Schlachtschiff", 310, 870, 33, "in Reparatur"),
    ("Shimakaze", "Japan", "Zerstörer", 20, 120, 40, "einsatzbereit"),
    ("Z-23", "Deutschland", "Zerstörer", 25, 140, 38, "einsatzbereit"),
    ("Enterprise", "USA", "Flugzeugträger", 100, 300, 28, "einsatzbereit"),
    ("Graf Zeppelin", "Deutschland", "Flugzeugträger", 120, 290, 31, "in Reparatur"),
    ("Des Moines", "USA", "Kreuzer", 150, 450, 34, "einsatzbereit"),
    ("Mogami", "Japan", "Kreuzer", 140, 420, 35, "versenkt"),
    ("Montana", "USA", "Schlachtschiff", 330, 880, 28, "einsatzbereit"),
    ("Musashi", "Japan", "Schlachtschiff", 400, 900, 27, "in Reparatur"),
    ("Hindenburg", "Deutschland", "Kreuzer", 180, 460, 33, "einsatzbereit"),
    ("Kidd", "USA", "Zerstörer", 20, 130, 37, "einsatzbereit"),
    ("Atago", "Japan", "Kreuzer", 160, 430, 36, "in Reparatur"),
    ("Lexington", "USA", "Flugzeugträger", 110, 310, 29, "einsatzbereit"),
    ("Akizuki", "Japan", "Zerstörer", 30, 150, 39, "einsatzbereit"),
    ("Tirpitz", "Deutschland", "Schlachtschiff", 320, 850, 31, "einsatzbereit"),
    ("Fletcher", "USA", "Zerstörer", 25, 140, 38, "einsatzbereit"),
    ("Amagi", "Japan", "Schlachtschiff", 350, 860, 29, "einsatzbereit"),
    ("Kronstadt", "Russland", "Kreuzer", 200, 470, 32, "einsatzbereit")
]
# Klassenbeschreibung:
# Klasse: Schiff
# Attribute: Name, Nation, Schiffstyp, Panzerung, Feuerkraft, Geschwindigkeit, Status
# Methoden:
# Anzeigen der Schiffsdaten (__str__)
# Status ändern (z. B. von "einsatzbereit" zu "in Reparatur")
# Klasse: Flotte
# Attribute: Liste aller Schiffe

# Methoden:
# Hinzufügen neuer Schiffe
# Entfernen eines Schiffes
# Sortieren der Schiffe nach Attributen (z. B. Feuerkraft oder Geschwindigkeit)
# Filtern der Schiffe nach Nation oder Typ
# Anzeigen aller einsatzbereiten Schiffe
# Komplexere Funktion: Berechnung der durchschnittlichen Feuerkraft pro Nation

# Aufgaben:
# Hinzufügen eines neuen Schiffs zur Flotte: Implementiere eine Methode, um ein neues Schiff (z. B. "Alaska", "USA", "Kreuzer", 170, 440, 34, "einsatzbereit") zur Liste hinzuzufügen.
# Sortieren der Schiffe nach Feuerkraft: Implementiere eine Funktion, die die Schiffe nach ihrer Feuerkraft sortiert und die sortierte Liste ausgibt.
# Filtern nach Nation: Schreibe eine Methode, die alle Schiffe einer bestimmten Nation (z. B. "Japan") zurückgibt.
# Statusänderung eines Schiffs: Entwickle eine Funktion, mit der der Status eines bestimmten Schiffs (z. B. "Bismarck") auf "in Reparatur" geändert werden kann.
# Anzeigen aller einsatzbereiten Schiffe: Schreibe eine Methode, die alle Schiffe auflistet, die den Status "einsatzbereit" haben.
# Berechnung der durchschnittlichen Feuerkraft pro Nation: Implementiere eine Funktion, die für jede Nation die durchschnittliche Feuerkraft ihrer Schiffe berechnet.
# Simulation einer Mission: Schreibe eine Methode, die eine Liste aller Schiffe zurückgibt, die für eine Mission geeignet sind. Kriterien: Status "einsatzbereit" und eine Geschwindigkeit über 30 Knoten.