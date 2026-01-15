# Kurzarbeit Programmierung – RegEx  
**Thema: Newsticker (HTML-Auswertung mit Python)**

In dieser Übung werten Sie mit Python und regulären Ausdrücken eine HTML-Datei eines fiktiven Newstickers aus.

Datei im Projektordner: **`NEWSTICKER.html`**

> Hinweis: In der Datei sind absichtlich **2 fehlerhafte Datensätze** enthalten (z. B. ungültige ID oder falsches datetime-Format).  
> Korrekte RegEx-Lösungen sollen diese Datensätze automatisch **nicht** erfassen.

---

## Aufgabe 1 (1 Punkt) – Datei einlesen

- Lesen Sie die Datei `NEWSTICKER.html` vollständig ein.
- Geben Sie die Länge des eingelesenen Textes aus.

Beispiel:
```python
print(len(text))
```

---

## Aufgabe 2 (8 Punkte – AFB I) – Datensätze über die ID zählen

Jeder Newsticker-Eintrag ist ein `<article>`-Element und enthält eine ID im Attribut `data-id`.

**Regel für eine gültige ID:**
- Optional **ein Kleinbuchstabe**
- Danach **genau 8 Ziffern**

Beispiele:
```html
<article class="ticker__item" data-id="90000001">
<article class="ticker__item" data-id="n90000002">
```

**Aufgaben:**
1. Schreiben Sie eine RegEx, die die ID aus `data-id="..."` erfasst.
2. Nutzen Sie `re.findall()` (oder eine geeignete Alternative), um alle gültigen IDs zu finden.
3. Geben Sie die Anzahl der gefundenen Datensätze aus.

**Erwartung:** Es werden **208 Datensätze** erwartet.

---

## Aufgabe 3 (10 Punkte – AFB I) – ID, Zeitstempel und Titel extrahieren

Jeder Eintrag enthält zusätzlich:
- einen Zeitstempel im `<time>`-Element mit ISO-`datetime`-Attribut
- einen Titel in `<span class="ticker__title">...</span>`

Beispiele:
```html
<time class="ticker__time" datetime="2026-01-15T18:30:00+01:00">15.01.2026 18:30</time>
<span class="ticker__title">Phishing-Welle trifft Mittelstand</span>
```

**Aufgaben:**
1. Erweitern Sie Ihre RegEx so, dass Sie pro Datensatz erfassen:
   - ID (aus `data-id`)
   - ISO-Zeitstempel (aus dem `datetime`-Attribut)
   - Titeltext
2. Geben Sie die ersten 5 Treffer aus (z. B. als Tabelle oder in einer Zeile pro Treffer).

**Erwartung:** Es werden **208 vollständige Treffer** erwartet.

---

## Aufgabe 4 (10 Punkte – AFB II) – Kategorie filtern

Jeder Datensatz besitzt eine Kategorie:
```html
<span class="ticker__tag">Sicherheit</span>
```

**Aufgaben:**
1. Erfassen Sie zusätzlich zur Aufgabe 3 auch die Kategorie (Tag).
2. Filtern Sie alle Treffer, deren Kategorie exakt **`Sicherheit`** ist.
3. Geben Sie die Anzahl dieser Treffer aus.

**Erwartung:** Es werden **52 Datensätze** der Kategorie **Sicherheit** erwartet.

---

## Aufgabe 5 (10 Punkte – AFB II) – Link extrahieren und prüfen

Jeder Datensatz enthält einen Link:
```html
<a class="ticker__link" href="/news/technik-0001">Mehr</a>
```

**Aufgaben:**
1. Erfassen Sie zusätzlich den Link (Wert im `href`-Attribut).
2. Geben Sie eine Liste (oder die ersten 10) der extrahierten Links aus.
3. Prüfen Sie, ob alle Links mit `/news/` beginnen (z. B. per `startswith`).  
   Geben Sie aus, wie viele Links diese Bedingung erfüllen.

**Erwartung:** Es werden **208 Links** erwartet, die mit `/news/` beginnen.

---

## Aufgabe 6 (4 Punkte – AFB III) – Objekte und Sortierung

Implementieren Sie eine Klasse `TickerEintrag` mit Attributen:
- `id`
- `datetime_iso`
- `kategorie`
- `titel`
- `link`

**Aufgaben:**
1. Erzeugen Sie aus jedem vollständigen Treffer ein Objekt.
2. Speichern Sie alle Objekte in einer Liste.
3. Sortieren Sie die Liste nach `datetime_iso` (aufsteigend).
4. Geben Sie die ersten 10 Einträge sortiert aus.

---

**Gesamtpunktzahl: 43 Punkte**
