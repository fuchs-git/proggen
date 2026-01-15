# RegEx-CTF: „Operation Logstorm“  
**Thema: Incident Response in einer fiktiven militärischen IT-Übungsumgebung**

Sie erhalten mehrere Logdateien aus einer simulierten Umgebung. Es besteht der Verdacht, dass ein Angreifer Zugriff erlangt und Daten exfiltriert hat.  
Ihre Aufgabe ist es, **nur mit Python + regulären Ausdrücken** Hinweise zu finden und die Ereigniskette zu rekonstruieren.

> Die Daten sind synthetische Trainingsdaten (CTF/Übung), kein Realbezug.

---

## Dateien

- `ctf_auth.log` – SSH- und sudo-Ereignisse (Authentifizierung / Privilegien)
- `ctf_web.log` – Webserver Access Log (API-Aufrufe / Downloads)
- `ctf_vpn.log` – VPN Ereignisse inkl. Traffic-Indikatoren

---

## Ziel

1. Identifizieren Sie **Angreifer-IP**, **betroffenen User** und **betroffenen Host**.
2. Finden Sie den Zeitpunkt des **ersten erfolgreichen Zugriffs**.
3. Belegen Sie eine **Privilegienerweiterung**.
4. Finden Sie Hinweise auf **Datenexport** und rekonstruieren Sie das **Flag**.

---

# Aufgaben

## Aufgabe 1 – „Warm-up“: Zeilen zählen (3 Punkte)

1. Lesen Sie jede Datei ein und zählen Sie die Zeilen.
2. Geben Sie die Anzahl Zeilen pro Datei aus.

**Erwartung (nur Kontrolle):**  
- `ctf_auth.log` hat **> 5.000** Zeilen  
- `ctf_web.log` hat **> 6.000** Zeilen  
- `ctf_vpn.log` hat **> 3.000** Zeilen

---

## Aufgabe 2 – SSH-Bruteforce erkennen (10 Punkte)

In `ctf_auth.log` gibt es Hinweise auf massenhafte Fehlversuche.

1. Schreiben Sie eine RegEx für `Failed password`-Zeilen und extrahieren Sie:
   - `user`
   - `src` (IP)
   - `host`
2. Filtern Sie alle Zeilen, bei denen `src` **nicht RFC1918** ist (also kein `10.*`, `172.16-31.*`, `192.168.*`).
3. Ermitteln Sie die IP mit den meisten Fehlversuchen.

**Erwartung:** Für die Angreifer-IP werden **137 Fehlversuche** gefunden.

---

## Aufgabe 3 – Erster erfolgreicher Zugriff (10 Punkte)

1. Schreiben Sie eine RegEx für erfolgreiche SSH-Logins (`Accepted password` oder `Accepted publickey`).
2. Filtern Sie auf die zuvor ermittelte Angreifer-IP.
3. Bestimmen Sie den **ersten** erfolgreichen Login (Zeitpunkt, Host, User).

**Erwartung:** Für die Angreifer-IP gibt es **genau 1** `Accepted password`-Treffer.

---

## Aufgabe 4 – Privilegienerweiterung (sudo) (8 Punkte)

1. Schreiben Sie eine RegEx für `sudo:`-Zeilen und extrahieren Sie:
   - ausführenden User
   - Ziel-User (`USER=`)
   - Command (`COMMAND=`)
   - Host
2. Prüfen Sie, ob der kompromittierte User Aktionen als **root** ausführt.

**Erwartung:** Es gibt **genau 1** sudo-Event, das als `USER=root` ausgeführt wird.

---

## Aufgabe 5 – Datenexport im Weblog (10 Punkte)

In `ctf_web.log` gibt es verdächtige API-Aufrufe.

1. Schreiben Sie eine RegEx für Requests, die auf `/api/export` gehen.
2. Extrahieren Sie:
   - IP
   - Methode
   - Pfad
   - Statuscode
   - Response-Größe
   - optional den Zusatz `X-Note="..."` (wenn vorhanden)
3. Filtern Sie auf die Angreifer-IP.

**Erwartung:** Es gibt **genau 3** Treffer auf `/api/export` von der Angreifer-IP.

---

## Aufgabe 6 – Flag rekonstruieren (9 Punkte)

Das Flag ist in Fragmenten im Feld `X-Note="..."` versteckt.

1. Extrahieren Sie alle `X-Note="..."`-Fragmente der `/api/export`-Requests (Angreifer-IP).
2. Sortieren Sie die Fragmente zeitlich (Reihenfolge im Log / Timestamp im Request).
3. Fügen Sie die Fragmente zusammen → **Flag**.

**Erwartung:** Das rekonstruierte Flag lautet:
- **`FLAG{REGEX_HUNTER_2026}`**

---

## Aufgabe 7 – VPN-Korrelation (Bonus 6 Punkte)

In `ctf_vpn.log` gibt es eine Tunnel-Session und Traffic-Spikes.

1. Extrahieren Sie für die Angreifer-IP:
   - `event`
   - `bytes_in`
   - `bytes_out`
   - `user`
2. Zeigen Sie, dass es im Zeitraum rund um den ersten erfolgreichen Login zu auffälligen Transfers kommt.
3. Optional: Finden Sie den Eintrag `event=TUNNEL_UP` für die Angreifer-IP.

---

## Abgabeformat

- Python-Datei (`.py`) oder Jupyter Notebook (`.ipynb`)
- Kurzer Bericht (Text oder Markdown) mit:
  - Angreifer-IP
  - kompromittierter User
  - kompromittierter Host
  - Zeitpunkt erster Erfolg
  - sudo-Beleg (Command)
  - rekonstruierte Flag

---

## Hinweise (RegEx)

- Nutzen Sie `re.MULTILINE` (bei `^`/`$`) und ggf. `re.DOTALL` nur, wenn nötig.
- Verwenden Sie **Gruppen** und gerne **benannte Gruppen** (`(?P<name>...)`).
- Achten Sie auf greedy vs. non-greedy (`.*` vs `.*?`).

