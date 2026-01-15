# Leistungsnachweis Programmierung – RegEx (Advanced)
**Thema: Newsticker – erweiterte HTML-Analyse mit Python**

Datei im Projektordner: **`ADV_NEWSTICKER.html`**

In dieser Aufgabenstellung analysieren Sie einen komplexeren Newsticker.  
Neben regulären Ausdrücken werden **Gruppierung, Filterung, optionale Elemente und Nachverarbeitung** erwartet.

> Hinweis: In der Datei befinden sich absichtlich fehlerhafte Datensätze.  
> Diese dürfen durch korrekt formulierte RegEx **nicht** erfasst werden.

---

## Aufgabe 1 (2 Punkte) – Einlesen & Grundprüfung

- Lesen Sie die Datei vollständig ein.
- Geben Sie die Länge des Textes aus.
- Prüfen Sie, ob mindestens ein `<article>`-Element vorhanden ist.

---

## Aufgabe 2 (8 Punkte – AFB I) – Gültige Newseinträge zählen

Ein gültiger Eintrag besitzt:
- `<article class="ticker__item">`
- Attribut `data-id` mit:
  - führendem `n`
  - genau **8 Ziffern**
- gültiges ISO-`datetime` im `<time>`-Element

**Aufgaben:**
1. Schreiben Sie eine RegEx, die **nur gültige Datensätze** erkennt.
2. Zählen Sie die gültigen Datensätze.

**Erwartung:** Es werden **240 gültige Datensätze** erwartet.

---

## Aufgabe 3 (10 Punkte – AFB II) – Mehrere Gruppen extrahieren

Erfassen Sie pro gültigem Datensatz:
- ID
- ISO-Datetime
- Kategorie
- Titel

**Zusatz:**
- Kategorien besitzen zusätzlich eine CSS-Klasse `tag--<kategorie>`.
- Verwenden Sie **benannte Gruppen** (`?P<name>`).

Geben Sie die ersten 5 Treffer strukturiert aus.

---

## Aufgabe 4 (10 Punkte – AFB II) – Optionale Elemente & Filter

Manche Einträge enthalten zusätzlich:
```html
<span class="ticker__urgent">EILMELDUNG</span>
```

**Aufgaben:**
1. Erweitern Sie Ihre RegEx so, dass das Element optional erkannt wird.
2. Zählen Sie, wie viele Einträge eine EILMELDUNG besitzen.
3. Filtern Sie alle EILMELDUNGEN der Kategorie **Sicherheit**.

---

## Aufgabe 5 (10 Punkte – AFB III) – Query-Parameter analysieren

Links haben folgendes Format:
```
/news/<slug>?src=ticker&prio=0|1
```

**Aufgaben:**
1. Erfassen Sie den kompletten Link.
2. Extrahieren Sie aus der URL:
   - `slug`
   - `prio`
3. Prüfen Sie:
   - `prio=1` ⇒ EILMELDUNG muss vorhanden sein
4. Geben Sie alle fehlerhaften Datensätze aus (ID + Titel).

---

## Aufgabe 6 (5 Punkte – AFB III) – Objektmodell & Sortierung

Implementieren Sie eine Klasse `AdvancedTickerEntry` mit:
- id
- datetime
- category
- title
- urgent (bool)
- priority (int)

**Aufgaben:**
1. Erzeugen Sie Objekte aus allen gültigen Datensätzen.
2. Sortieren Sie:
   - zuerst nach `urgent` (True zuerst)
   - dann nach Datum (neueste zuerst)
3. Geben Sie die Top 10 Einträge aus.

---

**Gesamtpunktzahl: 45 Punkte**
