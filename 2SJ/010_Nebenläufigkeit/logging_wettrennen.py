import threading, time, logging

def eine_funktion(name):
    logging.info(f"Thread {name} startet.")
    time.sleep(3)
    logging.info(f"Thread {name} ist fertig.")


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s", level=logging.INFO)

    logging.info("Hauptprogramm erzeugt und startet 10 Threads.")
    for i in range(10):
        threading.Thread(target=eine_funktion, args=(i,)).start()

    logging.info("Hauptprogramm ist fertig.")