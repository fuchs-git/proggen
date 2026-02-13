class Wochentag:
    def __init__(self, nummer):    # überschreiben der geerbten Methode
        self._nummer = nummer % 7  # <= nicht-öffentliches Attribut
        self._lesezugriffe = 0     # <= nicht-öffentliches Attribut

    def __str__(self):           # überschreiben der geerbten Methode
        return f'{self.get_nummer()}'

    def als_wort(self):          # eine normale Methode der Klasse
        return ("So", "Mo", "Di", "Mi", "Do", "Fr", "Sa")[self.get_nummer()]

    def get_nummer(self):        # der Getter für das Attribut nummer
        self._lesezugriffe += 1  # der Getter zählt die Lesezugriffe ...
        return self._nummer      # ... und liefert (wie jeder Getter) den Wert zurück

    def set_nummer(self, nummer):  # der Setter für das Attribut nummer
        self._nummer = nummer % 7  # der Setter schreibt einen korrigierten Wert

    def get_lesezugriffe(self):    # der Getter für das Attribut lesezugriffe
        return self._lesezugriffe  # dieser Getter tut nichts außer den Wert zu liefern


tag = Wochentag(3)
print(tag.als_wort())

tag.set_nummer(17)
print(tag.als_wort())
print(tag.get_nummer())

tag.set_nummer(-54)
print(tag.als_wort())

print("Anzahl Lesezugriffe auf _nummer:", tag.get_lesezugriffe())