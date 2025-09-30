# Aufgabe: "World of Warcraft - Gildenmanagement"
# Du bist der Anführer einer Gilde in World of Warcraft. Dein Ziel ist es, deine Gildenmitglieder zu verwalten und die Gilde auf Raid-Erfolge vorzubereiten. Dazu musst du Mitglieder mit verschiedenen Klassen, Berufen und Ausrüstungsstufen effizient organisieren. Deine Aufgabe ist es, ein Python-Programm zu schreiben, das die Gildenmitglieder verwaltet und verschiedene Operationen darauf ermöglicht.
#
#
gildenmitglieder = [
    ("Arthas", "Paladin", "Schmied", 90, 1200),
    ("Jaina", "Magier", "Verzauberer", 85, 1150),
    ("Thrall", "Schamane", "Ingenieur", 80, 1100),
    ("Valeera", "Schurke", "Lederer", 92, 1250),
    ("Anduin", "Priester", "Kräuterkundler", 88, 1170),
    ("Gul'dan", "Hexenmeister", "Alchemist", 84, 1130),
    ("Sylvanas", "Jäger", "Koch", 89, 1180),
    ("Garrosh", "Krieger", "Bergbauer", 91, 1210),
    ("Tyrande", "Druide", "Schneider", 87, 1160),
    ("Illidan", "Dämonenjäger", "Verzauberer", 93, 1260),
    ("Kael'thas", "Magier", "Alchemist", 86, 1140),
    ("Varok", "Krieger", "Schmied", 88, 1190),
    ("Maiev", "Schurke", "Lederer", 89, 1180),
    ("Malfurion", "Druide", "Kräuterkundler", 90, 1200),
    ("Vol'jin", "Schamane", "Ingenieur", 85, 1150),
    ("Chen", "Mönch", "Koch", 87, 1160),
    ("Kil'jaeden", "Hexenmeister", "Verzauberer", 94, 1270),
    ("Anub'arak", "Todesritter", "Bergbauer", 92, 1220),
    ("Zul'jin", "Jäger", "Schneider", 88, 1190),
    ("Kel'Thuzad", "Magier", "Alchemist", 95, 1280)
]
# Erläuterung der Datenstruktur:
# Jedes Mitglied wird durch ein Tuple repräsentiert:
# (Name, Klasse, Beruf, Level, Ausrüstungsstufe)
# Name (str): Der Name des Charakters.
# Klasse (str): Die Spielklasse des Mitglieds (z. B. Magier, Paladin, etc.).
# Beruf (str): Der Beruf des Mitglieds (z. B. Schmied, Alchemist, etc.).
# Level (int): Das Level des Mitglieds (maximal 95).
# Ausrüstungsstufe (int): Die Stärke der Ausrüstung des Mitglieds (je höher, desto besser).
# Anforderungen:

# Klassenstruktur:
# Erstelle die Klasse Gildenmitglied, um die einzelnen Mitglieder zu repräsentieren.
# Erstelle die Klasse Gilde, um die gesamte Gilde und deren Verwaltung zu repräsentieren.

# Methodenanforderungen:
# Die Klassen müssen Methoden für folgende Funktionen enthalten:
# Hinzufügen eines neuen Mitglieds: Eine Methode, die ein neues Mitglied in die Gilde aufnimmt.
# Sortieren der Mitglieder: Sortiere die Mitglieder basierend auf einem Attribut, z. B. Level oder Ausrüstungsstufe.
# Filtern der Mitglieder: Zeige nur Mitglieder mit bestimmten Attributen (z. B. alle Mitglieder mit einem Level über 90).
# Anzeigen der Mitglieder nach Klassen: Gruppiere und zeige die Mitglieder basierend auf ihrer Klasse.
# Berechnungen: Berechne die durchschnittliche Ausrüstungsstufe aller Mitglieder oder die Anzahl der Mitglieder pro Beruf.
# Empfehlungen: Erstelle eine Funktion, die die 5 stärksten Mitglieder (nach Ausrüstungsstufe) für einen Raid empfiehlt.
#
# Füge ein neues Mitglied namens Bolvar hinzu. Es ist ein Paladin mit dem Beruf Bergbauer, Level 89 und einer Ausrüstungsstufe von 1210.
# Sortiere die Mitglieder der Gilde nach ihrer Ausrüstungsstufe in absteigender Reihenfolge und gib die Liste aus.
# Filtere alle Mitglieder, die einen Beruf als Alchemist haben, und gib ihre Namen aus.
# Zeige alle Mitglieder, die ein Level von 90 oder höher haben, sortiert nach ihrem Level.
# Gruppiere die Mitglieder nach ihrer Klasse und zeige die Anzahl der Mitglieder pro Klasse an.
# Berechne die durchschnittliche Ausrüstungsstufe aller Mitglieder in der Gilde.
# Finde die 5 Mitglieder mit der höchsten Ausrüstungsstufe und gib deren Namen und Klasse aus.
# Ändere den Beruf von Jaina von Verzauberer zu Alchemist.
# Finde heraus, welcher Beruf in der Gilde am häufigsten vertreten ist.
# Entferne ein Mitglied namens Gul'dan aus der Gilde.