# Log-Einträge werden zeilenweise das Format "Name;Geschlecht;Sportart;Leistung"
from collections import OrderedDict



# Bei Sportarten, die das Wort "Lauf" (in beliebiger Schreibweise) enthalten, sind die angegebenen Leistungen dann
# besser, wenn sie kleiner sind als andere. Bei allen anderen Sportarten sind höhere Werte besser.

class Teilnehmer:
    """
    Erstellen Sie eine Klasse Teilnehmer, die im Konstruktor einen Namen und ein Geschlecht übergeben bekommt und diese
    Informationen intern speichert. Objekte dieser Klasse sollen in Mengen und als Schlüssel von Dictionaries verwendbar
    sein. Zwei Objekte dieser Klasse sind genau dann gleich, wenn der Name gleich ist.
    """

    def __init__(self, name, geschlecht):
        self.name = name
        self.mwd = geschlecht

    def __eq__(self, other: 'Teilnehmer'):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name


class Sprotfest:
    """
    Erstellen Sie eine Klasse Sportfest. Dem Konstruktor werden beim Anlegen keine Daten übergeben (aber ggf. werden
    zunächst leere Datenstrukturen angelegt)! Die internen Datenstrukturen der Klasse sind selbst geeignet zu wählen.
    Es gibt viele Möglichkeiten, alle haben Vor- und Nachteile. Überlegen Sie anhand der geforderten Funktionalität,
    welche Implementierung Sie für geeignet halten!
    """

    def __init__(self):
        self.ergebnisse = {}
        self.alleversuche = []

    def neuer_datensatz(self, datensatz):
        """
        :param Datensatz der Form "Name;Geschlecht;Sportart;Leistung":
        :return:
        """
        try:
            name, geschlecht, sportart, leistung = datensatz.strip().split(';')
            float(leistung)
            if geschlecht.lower() not in ['m', 'w', 'd']:
                raise ValueError
        except ValueError:
            print(f'Fehler bei dem Datensatz: {datensatz}')
            return

        teilnehmer = Teilnehmer(name, geschlecht)

        if teilnehmer not in self.ergebnisse:
            self.ergebnisse[teilnehmer] = {}

        self.ergebnisse[teilnehmer][sportart] = float(leistung)
        self.alleversuche.append((teilnehmer, sportart, float(leistung)))

    def sportarten(self):
        sportarten_set = set()

        for teilnehmer in self.ergebnisse:
            for sportart in self.ergebnisse[teilnehmer]:
                sportarten_set.add(sportart)
        return sportarten_set

    def anzahl_sportarten(self):
        return len(self.sportarten())

    def liste_teilnehmer(self):
        teilnehmer_set = set()
        for teilnehmer in self.ergebnisse:
            teilnehmer_set.add(teilnehmer)
        return sorted(list(teilnehmer_set), key=lambda x: x.name)

    def anzahl_teilnehmer(self):
        return len(self.liste_teilnehmer())

    def teilnehmer_pro_sportart(self):
        sportarten_dict = {}

        for teilnehmer, disziplin in self.ergebnisse.items():
            for sportart in disziplin:
                if sportart not in sportarten_dict:
                    sportarten_dict[sportart] = 1
                sportarten_dict[sportart] += 1
        return sorted(sportarten_dict.items(), key=lambda x: x[1], reverse=True)

    def top10_pro_disziplin_und_geschlecht(self):
        top10 = {}
        for teilnehmer, disziplin in self.ergebnisse.items():
            for sportart, leistung in disziplin.items():
                key = sportart, teilnehmer.mwd
                if key not in top10:
                    top10[key] = []
                top10[key].append((teilnehmer, leistung))

        for key in top10:
            sportart, _ = key
            reverse = not ('lauf' in sportart.lower())
            top10[key] = sorted(top10[key], key=lambda x: x[1], reverse=reverse)[:10]

        top10_sorted = OrderedDict()
        for key in sorted(top10):
            top10_sorted[key] = top10[key]

        return top10_sorted

    def beste_10_versuche_pro_disziplin_und_geschlecht(self):
        top10 ={}

        for teilnehmer, sportart, leistung in self.alleversuche:
            key = (sportart, teilnehmer.mwd)
            if key not in top10:
                top10[key] = []
            top10[key].append((teilnehmer, leistung))

            # Sortieren & kürzen auf 10 pro Gruppe
        sorted_top10 = {}
        for key in sorted(top10):  # alphabetisch nach (Sportart, Geschlecht)
            sportart, _ = key
            reverse = not ('lauf' in sportart.lower())
            eintraege = sorted(top10[key], key=lambda x: x[1], reverse=reverse)[:10]
            sorted_top10[key] = eintraege

        return sorted_top10

    def teilnehmer_urkunden(self):
        urkunde = {}
        # print(self.ergebnisse.items())
        # dict_items([(Egon, {'100-m-Lauf': 24.12, 'Pendellauf': 27.2, 'Becherwerfen': 0.0, 'Kugelstoßen': 1181.0, '60-m-Lauf': 11.19, '110-m-Hürdenlauf': 26.17, 'Steinwurf': 473.0, 'Hochsprung': 164.0})])
        for teilnehmer, sportart, leistung in self.alleversuche:
            if teilnehmer not in urkunde:
                urkunde[teilnehmer] = {}

            if sportart not in urkunde[teilnehmer]:
                urkunde[teilnehmer][sportart] = []
            urkunde[teilnehmer][sportart].append(leistung)


        for teilnehmer in urkunde:
            for sportart in urkunde[teilnehmer]:
                urkunde[teilnehmer][sportart].sort()
                if 'lauf' in sportart:
                    urkunde[teilnehmer][sportart].sort()
                else:
                    urkunde[teilnehmer][sportart].sort(reverse=True)

                print(urkunde[teilnehmer][sportart][0])

        return urkunde
            # print(person, ergebnis, ergebnisse[ergebnis])






with open('sportfest.log', 'r', encoding='utf-8') as f:
    daten = f.read().splitlines()

sportfest = Sprotfest()
for datensatz in daten:
    sportfest.neuer_datensatz(datensatz)

# print(f'{"eine Liste aller Sportarten":_^50}')
# print(sportfest.sportarten())
#
# print(f'{"die Anzahl der Sportarten":_^50}')
# print(sportfest.anzahl_sportarten())
#
# print(f'{"eine Liste aller Teilnehmer":_^50}')
# print(sportfest.liste_teilnehmer())
#
# print(f'{"die Anzahl aller Teilnehmer":_^50}')
# print(sportfest.anzahl_teilnehmer())
#
# print(f'{"die Anzahl aller Teilnehmer pro Sportart":_^50}')
# print(*sportfest.teilnehmer_pro_sportart())
#
# print(f'{"TOP 10 Teilnehmer pro Sportart und Geschlecht":_^100}')
# top10 = sportfest.top10_pro_disziplin_und_geschlecht()
# for (sportart, geschlecht), eintraege in top10.items():
#     print(f"\n{sportart} ({geschlecht}):")
#     for platz, (teilnehmer, leistung) in enumerate(eintraege, start=1):
#         print(f"  {platz:2d}. {teilnehmer.name:<10} – {leistung}")

# print(sportfest.beste_10_versuche_pro_disziplin_und_geschlecht())

urkunden = sportfest.teilnehmer_urkunden()
for teilnehmer, disziplinen in urkunden.items():
    print(f"{teilnehmer.name}:")
    for sportart, werte in disziplinen.items():
        print(f"  {sportart}: {werte[0]}")