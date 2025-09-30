# Thema: Ressourcenmanagement in Satisfactory
# Dataset:
# Das Dataset enthält 20 Produktionsgebäude (z. B. Minen, Schmelzen, Fabriken), die in einer Liste von Objekten gespeichert werden. Jedes Gebäude hat folgende Attribute:
# Name: Name des Gebäudes (z. B. "Eisenmine A").
# Ressource: Welche Ressource verarbeitet oder produziert wird (z. B. "Eisen", "Kupfer", "Kohlenstoff").
# Produktion (Einheiten/Minute): Wie viele Einheiten das Gebäude pro Minute produziert (z. B. 60).
# Energieverbrauch (MW): Wie viel Energie das Gebäude benötigt (z. B. 20 MW).
# Status: Ob das Gebäude aktiv ist ("Online") oder nicht ("Offline").
# Beispiel-Dataset:
# Python
gebaeude = [
    ("Eisenmine A", "Eisen", 60, 20, "Online"),
    ("Kupfermine A", "Kupfer", 45, 18, "Online"),
    ("Kohlenstoffmine A", "Kohlenstoff", 50, 25, "Offline"),
    ("Schmelze 1", "Eisen", 30, 15, "Online"),
    ("Schmelze 2", "Kupfer", 25, 12, "Online"),
    ("Assembler 1", "Eisenplatten", 15, 50, "Online"),
    ("Assembler 2", "Rohre", 10, 50, "Offline"),
    ("Kohlekraftwerk A", "Energie", 0, -50, "Online"),
    ("Eisenmine B", "Eisen", 80, 25, "Online"),
    ("Kupfermine B", "Kupfer", 40, 18, "Offline"),
    ("Ölraffinerie A", "Kunststoff", 30, 70, "Online"),
    ("Ölraffinerie B", "Gummi", 35, 65, "Offline"),
    ("Schmelze 3", "Eisen", 40, 20, "Online"),
    ("Assembler 3", "Rotoren", 8, 55, "Online"),
    ("Kohlenstoffmine B", "Kohlenstoff", 60, 30, "Online"),
    ("Ölfeld A", "Rohöl", 100, 45, "Online"),
    ("Schmelze 4", "Kupfer", 20, 10, "Offline"),
    ("Biomassegenerator A", "Energie", 0, -10, "Online"),
    ("Schmelze 5", "Eisen", 35, 18, "Offline"),
    ("Assembler 4", "Modulare Rahmen", 5, 60, "Online")
]

# Verwendung von Klassen:
# Klasse Gebäude:
# Diese Klasse repräsentiert ein einzelnes Produktionsgebäude.
# Attribute: name, ressource, produktion, energieverbrauch, status.
# Methoden:
# Anzeigen der Gebäudeinformationen.
# Ändern des Status (Online/Offline).
# Klasse Fabrik:
# Diese Klasse verwaltet die gesamte Fabrik mit mehreren Gebäuden.
# Methoden:
# Hinzufügen eines neuen Gebäudes.
# Sortieren der Gebäude nach einem Attribut (z. B. Energieverbrauch oder Produktion).
# Filtern der Gebäude nach Ressource oder Status.
# Berechnung des Gesamtenergieverbrauchs.
# Anzeige der Gesamtproduktion nach Ressource (z. B. "Wieviel Eisen wird pro Minute produziert?").

# Textaufgaben:
# Füge ein neues Gebäude hinzu:
# Füge ein neues Gebäude mit den folgenden Attributen hinzu:
# Name: "Ölraffinerie C", Ressource: "Treibstoff", Produktion: 40, Energieverbrauch: 60, Status: "Online".
# Sortieren nach Energieverbrauch:
# Sortiere die Liste der Gebäude nach Energieverbrauch in absteigender Reihenfolge. Gib den Namen und den Energieverbrauch der Gebäude aus.
# Filtern nach Ressource:
# Zeige alle Gebäude an, die die Ressource "Eisen" verarbeiten oder produzieren. Gib den Namen, die Produktion und den Status dieser Gebäude aus.
# Berechnung des Gesamtenergieverbrauchs:
# Berechne den Gesamtenergieverbrauch aller Online-Gebäude in der Fabrik. Gib das Ergebnis aus.
# Statusänderung:
# Ändere den Status von "Schmelze 4" und "Kupfermine B" auf "Online". Aktualisiere die Daten entsprechend und gib die geänderten Gebäude aus.
# Gesamtproduktion nach Ressource:
# Berechne, wie viele Einheiten der Ressource "Eisen" pro Minute in der Fabrik produziert werden. Berücksichtige nur Online-Gebäude.
# Identifiziere die ineffizientesten Gebäude:
# Zeige alle Gebäude an, deren Produktion (Einheiten/Minute) kleiner als 20 ist und deren Energieverbrauch größer als 50 MW ist. Gib die Namen dieser Gebäude aus.
