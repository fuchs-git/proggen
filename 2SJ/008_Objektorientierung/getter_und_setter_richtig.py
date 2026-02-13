class Wochentag:
    def __init__(self, nummer):
        self._lesezugriffe = 0     # nicht-öffentliches Attribut ...
                                   # ... für die Property lesezugriffe
        self._schreibzugriffe = 0  # nicht-öffentliches Attribut ...
                                   # ... für die Property schreibzugriffe
        self.nummer = nummer       # <= hier wird direkt der Setter aufgerufen, ...
                                   # ... um für die Property nummer das ...
                                   # ... nicht-öffentliche Attribut _nummer anzulegen
                                   # man könnte hier auch direkt auf das ...
                                   # ... Attribut _nummer zugreifen, müsste dann aber ...
                                   # ... alles nachbauen, was der Setter auch noch macht
                                   # da wir den Setter benutzen, welcher das Attribut ...
                                   # ... _schreibzugriffe benutzt, muss dieses Attribut
                                   # ... hier vorher angelegt werden

    def __str__(self):
        return f'{self.nummer}' # hier wird via Getter auf die Property zugegriffen
                                # man könnte hier auch direkt auf das Attribut ...
                                # ... _nummer zugreifen, müsste dann aber alles ...
                                # ... nachbauen, was der Getter auch noch macht

    def als_wort(self):  # eine normale Methode der Klasse
                         # hier wird über den Getter auf die Property zugegriffen
                         # man könnte hier auch direkt auf das Attribut _nummer ...
                         # ... zugreifen, müsste dann aber alles nachbauen, was ...
                         # ... der Getter auch noch macht
        return ("So", "Mo", "Di", "Mi", "Do", "Fr", "Sa")[self.nummer]

    @property
    def nummer(self):  # der Getter für die Property nummer
        self._lesezugriffe += 1
        return self._nummer

    @nummer.setter
    def nummer(self, wert):  # der Setter für die Property nummer
        self._schreibzugriffe += 1
        self._nummer = wert % 7  # der Name des Übergabeparameters (wert) ...
                                 # ... wird nur in der Dokumentation sichtbar sein

    @property
    def lesezugriffe(self):  # der Getter für die Property lesezugriffe
        return self._lesezugriffe  # für diese Property gibt es keinen Setter

    @property
    def schreibgriffe(self):  # der Getter für die Property schreibzugriffe
        return self._schreibzugriffe  # für diese Property gibt es keinen Setter


tag = Wochentag(3)
print(tag.als_wort())

tag.nummer = 16
print(tag.als_wort())
print(tag.nummer)

tag.nummer = -55
print(tag.als_wort())

print("Anzahl Lesezugriffe auf nummer:", tag.lesezugriffe)
print("Anzahl Schreibzugriffe auf nummer:", tag.schreibgriffe)