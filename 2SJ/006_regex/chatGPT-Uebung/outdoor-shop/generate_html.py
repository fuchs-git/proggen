# generate_shop_html.py
# Erzeugt eine HTML-Datei mit 305 gueltigen Datensaetzen + 3 absichtlich falschen
# Ausgabe: SHOP.html

import random

random.seed(42)

PRODUCT_NAMES = [
    "NORDVIND / TÄLT",
    "FJÄLL / RYGGSÄCK",
    "KOK / SET",
    "STORM / PLANDE",
    "VÅR / MATTE",
    "AURORA / ZELT",
    "ÄVENTYR / KOCHER",
    "ÖRN / LAMPE",
    "SJÖ / FLASKA",
    "GLÖD / GRILL",
    "SKOG / SÄCK",
    "FROST / BOX",
    "KLAR / GLAS",
    "DRIVA / TARP",
    "VIND / JACKA",
    "SOL / PANEL",
    "IS / KÜHLBOX",
    "RÖK / KESSEL",
    "BÄR / MESSER",
    "ELD / OFEN",
]

DESCRIPTIONS = [
    "Zelt für 2 Personen, windstabil",
    "Rucksack 35L, wasserabweisend",
    "Outdoor-Kochset, leicht & robust",
    "Tarp mit Ösen",
    "Isomatte, kompakt",
    "Expeditionszelt, 4-Jahreszeiten",
    "Gaskocher, piezo",
    "Stirnlampe, 350 lm",
    "Trinkflasche, Edelstahl",
    "Faltgrill, hitzebeständig",
    "Drybag, verschließbar",
    "Kühlbox, isoliert",
    "Trinkglas, bruchsicher",
    "Tarp, reißfest",
    "Regenjacke, atmungsaktiv",
    "Solarpanel, faltbar",
    "Kühlbox, ultraleicht",
    "Teekessel, Camping",
    "Messer, rostfrei",
    "Mini-Ofen, Titanium",
]

def gen_measure() -> str:
    # 2D oder 3D; Ziffern, x; in der ersten Angabe optional / oder -
    kind = random.choice(["2d", "3d", "slash", "dash"])
    if kind == "2d":
        a = random.randint(10, 280)
        b = random.randint(10, 250)
        return f"{a}x{b} cm"
    if kind == "3d":
        a = random.randint(30, 350)
        b = random.randint(30, 120)
        c = random.randint(30, 260)
        return f"{a}x{b}x{c} cm"
    if kind == "slash":
        a1 = random.randint(100, 260)
        a2 = random.randint(50, 200)
        b = random.randint(30, 120)
        c = random.randint(30, 260)
        return f"{a1}/{a2}x{b}x{c} cm"
    # dash
    a1 = random.randint(80, 160)
    a2 = a1 + random.randint(10, 60)
    b = random.randint(30, 120)
    c = random.randint(30, 260)
    return f"{a1}-{a2}x{b}x{c} cm"

def gen_price() -> str:
    # Preis als EURO.CC
    euros = random.choice([9, 12, 14, 19, 24, 29, 34, 39, 44, 49, 59, 79, 89, 99, 129, 149, 199, 249, 333, 499, 799, 1070, 2020])
    cents = random.choice([0, 5, 9, 10, 25, 50, 90, 95, 99])
    return f"{euros}.{cents:02d}"

def gen_id(i: int) -> str:
    # optionaler Kleinbuchstabe + 8 Ziffern
    prefix = random.choice(["", "s"])
    base = 80000000 + i  # 8-stellig bleibt es bis i < 20000000
    return f"{prefix}{base:08d}"

def make_valid_item(i: int) -> str:
    pid = gen_id(i)
    name = random.choice(PRODUCT_NAMES)
    desc = random.choice(DESCRIPTIONS)
    size = gen_measure()
    price = gen_price()

    # absichtlich viele Zeilenumbrueche / Whitespaces
    return f"""
    <div data-ref-id="{pid}">
      <section class="teaser">
        <span class="notranslate plp-price-module__product-name">{name}</span>

        <div class="details">
          <span class="plp-price-module__description">{desc}, {size}</span>
        </div>

        <div class="price">
          <span class="plp-price__sr-text">Preis {price}€</span>
        </div>
      </section>
    </div>
    """

def make_invalid_items() -> str:
    # 1) Ungueltige ID (7 Ziffern)
    bad_id = """
    <div data-ref-id="s1234567">
      <span class="notranslate plp-price-module__product-name">FEHLER / ID</span>
      <span class="plp-price-module__description">Soll nicht gefunden werden, 10x10 cm</span>
      <span class="plp-price__sr-text">Preis 9.99€</span>
    </div>
    """

    # 2) Ungueltiges Maß (endet nicht mit " cm")
    bad_size = """
    <div data-ref-id="81234567">
      <span class="notranslate plp-price-module__product-name">FEHLER / MAS</span>
      <span class="plp-price-module__description">Falsches Maßformat, 100x50x30</span>
      <span class="plp-price__sr-text">Preis 12.34€</span>
    </div>
    """

    # 3) Ungueltiger Preis (Komma statt Punkt)
    bad_price = """
    <div data-ref-id="82345678">
      <span class="notranslate plp-price-module__product-name">FEHLER / PREIS</span>
      <span class="plp-price-module__description">Falsche Preisdarstellung, 30x20 cm</span>
      <span class="plp-price__sr-text">Preis 33,50€</span>
    </div>
    """

    return bad_id + "\n" + bad_size + "\n" + bad_price

def main() -> None:
    valid_count = 305  # 300+
    items = [make_valid_item(i) for i in range(valid_count)]

    # streue die 3 "falschen" irgendwo ein
    insert_pos = random.randint(20, valid_count - 20)
    items.insert(insert_pos, make_invalid_items())

    html = f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <title>Outdoor Shop – Katalog</title>
</head>
<body>
  <main>
    <h1>Outdoor Shop</h1>
    {''.join(items)}
  </main>
</body>
</html>
"""

    with open("SHOP.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Erzeugt: SHOP.html")
    print(f"Gueltige Datensaetze: {valid_count}")
    print("Zusaetzlich: 3 absichtlich falsche Datensaetze (ID/Mass/Preis)")

if __name__ == "__main__":
    main()
