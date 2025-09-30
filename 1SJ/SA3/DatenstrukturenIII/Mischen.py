# Schreiben Sie eine Funktion dict_merger, die eine beliebige Anzahl von Dictionaries übergeben bekommt und ein
# einziges Dictionary zurückliefert. Dabei sollen alle Schlüssel aus allen übergebenen Dictionaries im zurückgelieferten
# Dictionary enthalten sein. Als Wert soll jeder Schlüssel eine Liste aller Werte haben, die dieser Schlüssel in den
# verschiedenen Dictionaries hat. Kommt ein Schlüssel nicht in allen Dictionaries vor, ist im Rückgabewert die Liste
# für diesen Schlüssel entsprechend kürzer.

def dict_merger(*kwargs):
    merged = {}
    for d in kwargs:
        for key in d:
            if key not in merged:
                merged[key] = []
            merged[key].append(d[key])
    return merged

print(dict_merger())

d1 = {1: "eins", 2: "zwei", 3: "drei", 17: "siebzehn", 5:"fünf"}
print(dict_merger(d1))

d1 = {1: "eins", 2: "zwei", 3: "drei", 17: "siebzehn", 5:"fünf"}
d2 = {1: "one", 2: "two", 3: "three", 4:"four", 5:"five", 6:"six"}
d3 = {1: "один", 2: "два", 19: "девятнадцать", 3: "три", 4: "четыре"}
print(dict_merger(d1, d2, d3))