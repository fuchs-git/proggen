# Programmierung – RegEx  
**Thema: Online-Outdoor-Shop (HTML-Auswertung mit Python)**


---

## Aufgabe 1 (1 Punkt) – Einlesen der Datei prüfen

Die Datei `SHOP.html` enthält den HTML-Quelltext einer Produktübersichtsseite.

- Lesen Sie die Datei vollständig ein.
- Zeilenumbrüche sind inhaltlich ohne Bedeutung.
- Geben Sie die Länge des eingelesenen Textes aus.

Hinweis:
```python
print(len(text))
```

---

## Aufgabe 2 (9 Punkte – AFB I) – Identifizieren eines Produkts

Jeder Produktdatensatz beginnt mit einem `<div>`-Element, das eine eindeutige Produkt-ID enthält.

**Eigenschaften der ID:**
- Attribut: `data-ref-id`
- Optional ein Kleinbuchstabe
- Danach genau 8 Ziffern

Beispiele:
```html
<div data-ref-id="80437234">
<div data-ref-id="s99299039">
```

**Aufgaben:**
1. Entwickeln Sie einen regulären Ausdruck, der den Beginn eines gültigen Produkts erkennt.
2. Verwenden Sie `re.findall()` oder eine geeignete Alternative.
3. Zählen Sie ausschließlich die gültigen Produkte.
4. Geben Sie die Anzahl der gefundenen Produkte aus.

Hinweis:  
Ein Datensatz besitzt absichtlich eine ungültige ID und darf nicht gezählt werden.

---

## Aufgabe 3 (9 Punkte – AFB I) – Identifizierung des Produktnamens

Jeder Produktdatensatz enthält einen Produktnamen.

**Merkmale:**
- Befindet sich in einem `<span>`-Element mit der Klasse  
  `notranslate plp-price-module__product-name`
- Besteht nur aus:
  - Großbuchstaben
  - Leerzeichen
  - Schrägstrichen `/`
  - Umlauten wie Ä, Ö, Å

Beispiel:
```html
<span class="notranslate plp-price-module__product-name">
NORDVIND / TÄLT
</span>
```

**Aufgaben:**
1. Erweitern Sie den regulären Ausdruck aus Aufgabe 2.
2. Erfassen Sie zusätzlich den Produktnamen.
3. Verwenden Sie Gruppen, um auf ID und Produktname zuzugreifen.
4. Geben Sie ID und Produktname zeilenweise aus.

Hinweis:  
Ein Produkt besitzt einen ungültigen Namen und scheidet aus.

---

## Aufgabe 4 (11 Punkte – AFB II) – Beschreibung und Ausmaß

Jedes Produkt enthält eine Beschreibung mit integrierter Größenangabe.

**Aufbau:**
```html
<span class="plp-price-module__description">
Beschreibung, Ausmaß cm
</span>
```

**Beispiele für gültige Ausmaße:**
```
79x176 cm
250x60x236 cm
211/161x236 cm
110-127x57x181 cm
```

**Regeln:**
- Das Ausmaß endet immer mit ` cm`
- Dimensionen sind mit `x` getrennt
- In der ersten Dimension sind `/` und `-` erlaubt
- Beschreibung und Maß sind durch `, ` getrennt

**Aufgaben:**
1. Erweitern Sie den regulären Ausdruck erneut.
2. Erfassen Sie:
   - die Beschreibung (ohne Maß)
   - das Ausmaß (ohne `cm`)
3. Legen Sie beide Angaben in getrennten Gruppen ab.
4. Geben Sie ID, Name, Beschreibung und Ausmaß aus.

Hinweis:  
Ein Produkt enthält ein fehlerhaftes Maßformat und darf nicht berücksichtigt werden.

---

## Aufgabe 5 (9 Punkte – AFB II) – Identifizierung des Preises

Der Preis eines Produkts folgt immer der Beschreibung.

**Aufbau:**
```html
<span class="plp-price__sr-text">Preis 123.45€</span>
```

**Regeln:**
- Ganze Euro
- Punkt als Dezimaltrennzeichen
- Genau zwei Nachkommastellen
- Euro-Symbol `€`

**Aufgaben:**
1. Erweitern Sie den regulären Ausdruck um den Preis.
2. Erfassen Sie den Preis ohne Euro-Zeichen in einer Gruppe.
3. Wandeln Sie den Preis in `float` um.
4. Summieren Sie alle gültigen Preise.
5. Geben Sie die Gesamtsumme aus.

Hinweis:  
Ein Produkt enthält einen ungültigen Preis (Komma statt Punkt) und scheidet aus.

---

## Aufgabe 6 (4 Punkte – AFB III) – Produkte als Objekte

Es existiert eine Klasse `Produkt` mit Attributen für:
- ID
- Name
- Beschreibung
- Ausmaß
- Preis

**Aufgaben:**
1. Erzeugen Sie aus jedem vollständigen Treffer eine Objektinstanz.
2. Speichern Sie alle Objekte in einer Liste.
3. Sortieren Sie die Liste nach dem Preis.
4. Geben Sie alle Produkte sortiert aus.

---

**Gesamtpunktzahl: 43 Punkte**
