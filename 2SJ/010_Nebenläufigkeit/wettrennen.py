import threading, time

def eine_funktion(name):
    print(f"Thread {name} startet.\n", end='')
    time.sleep(3)
    print(f"Thread {name} ist fertig.\n", end='')

if __name__ == "__main__":
    print("Hauptprogramm erzeugt und startet 10 Threads.")
    for i in range(10):
        threading.Thread(target=eine_funktion, args=(i,)).start()

    print("Hauptprogramm ist fertig.")