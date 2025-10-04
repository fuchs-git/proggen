## Aufgaben

Nutzer in passwd suchen

Erstellen Sie eine Abfrage, die alle nicht anmeldeberechtigten Nutzer in _/etc/passwd_ anzeigt!

```bash
grep 'nologin' /etc/passwd
```

Ändern Sie die Abfrage so ab, dass nur die anmeldeberechtigten Nutzer angezeigt werden!

```bash
grep 'sh$' /etc/passwd
```

Nutzer zählen

Erstellen Sie eine Abfrage, die zunächst nach dem angemeldeten Nutzer (whoami) in _/etc/passwd_ sucht!
```bash
w
```

Erstellen Sie eine weitere Abfrage, die nun im gesamten Verzeichnis `/etc/` sucht!
```bash
???
```

Gruppen rausschreiben

Erstellen Sie eine Abfrage, die aus _/etc/group_ die Gruppen rausschreibt, die vermeintliche Systemgruppen sind (_system_ ist Teil des Namens)! Speichern Sie diese Zeilen in eine Datei _systemgruppen.log_!

Gruppen rausschreiben

Erstellen Sie eine Abfrage, die aus _/etc/group_ die Gruppen rausschreibt, die vermeintliche Systemgruppen sind (_system_ ist Teil des Namens)! Speichern Sie diese Zeilen in eine Datei _systemgruppen.log_!
```bash
cat /etc/group | cut -d: -f1 | grep 'system' > systemgruppen.log 
```

Gruppen mit Regex rausschreiben
```bash
grep 'system' /etc/group
```

Erstellen Sie eine Abfrage, die aus _/etc/group_ nur die Gruppen rausschreibt, deren Id dreistellig ist und mit einer 1 beginnt! Speichern Sie diese Zeilen in eine Datei _gruppen100.log_!
```bash
grep '^[^:]*:[^:]*:1[0-9][0-9]:' /etc/group > gruppen100.log
```


Zahlen sortieren

Betrachten Sie folgende Beispiele:

```
echo -e"111
12
5
23
1" sort
111
12
23
5

--> sort -d 
```

Warum sortiert der Befehl, die Zahlen vermeitlich falsch?

Korrigieren Sie den Befehl so, dass er die Zahlen in numerischer Ordnung richtig sortiert!