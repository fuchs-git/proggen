import time
import multiprocessing as mp

def ist_primzahl(x: int) -> bool:
    # die Funktion ist nicht sehr schlau, sondern absichtlich langsam!!!
    if x <= 1: return False
    for i in range(2, x):
        if x % i == 0: return False
    return True

if __name__ == '__main__':
    grenze = 50_000  # 1Kern@2.4GHz etwa 5-10sec,   4Kerne@2.4GHz etwa 3-5sec
    grenze = 100_000  # 1Kern@2.4GHz etwa 30-40sec,   4Kerne@2.4GHz etwa 10-15sec
    grenze = 150_000  # 1Kern@2.4GHz etwa 65-85sec,   4Kerne@2.4GHz etwa 20-30sec
    grenze = 200_000  # 1Kern@2.4GHz etwa 130-150sec,   4Kerne@2.4GHz etwa 40-50sec
    runs = (1, 2, 4, 8, 16, 32, None)  # Anzahl der Prozesse, die wir vorgeben
    print(f"Rechner hat {mp.cpu_count()} CPU-Kerne") # Kerne im Rechner

    for anzahl_prozesse in runs:  # etwa 40-50 MiB RAM pro Prozess
        match anzahl_prozesse:
            case 1:
                ausgabe = "kein MP (1P):"
            case None:  # bei "None" nutzt der Pool so viele Prozesse, wie es Kerne gibt
                if mp.cpu_count() in runs: continue  # nicht nochmal, falls wir das eh schon machen
                ausgabe = " 1P pro Kern:"
            case _:
                ausgabe = f"{anzahl_prozesse:3} Prozesse:"
        print(f"{ausgabe} Anzahl aller Primzahlen kleiner {grenze:_}: ", end="")

        # im OS die Prozesse beobachten! ! !
        # Windows: Taskmanager, Details, Sortieren nach CPU
        # Betriebssysteme: top
        start = time.time()
        with mp.Pool(anzahl_prozesse) as pool:  # with sorgt dafür, dass der Pool am Ende wieder aufgeräumt wird
            if anzahl_prozesse == 1:  # kein MP
                prim_oder_nicht = list(map(ist_primzahl, range(grenze)))  # standard-map
            else:  # MP
                prim_oder_nicht = list(pool.map(ist_primzahl, range(grenze)))  # mp-map
            zeit = time.time() - start
        print(f"{prim_oder_nicht.count(True)} {zeit:6.2f}sec")


def cpu_count():
    return None