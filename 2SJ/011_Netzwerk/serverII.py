import random
import socket

text = '''
Erfolg ist eine Reise, kein Ziel. – Arthur Robert Ashe jr.
Gib niemals auf zu versuchen, das zu tun, was du wirklich willst. – Ella Fitzgerald
Wenn es schwierig wird, gib nicht auf.
Gehe immer einen Schritt weiter.
Du bist stärker als du denkst.
Es ist nie zu spät, das zu werden, was du hättest sein können. - George Eliot
Nur wer Fehler macht, kann auch wachsen.
Wer positiv denkt, bekommt positive Ergebnisse.
Sei mutig und wage es, deine Träume zu leben.
Verwandle deine Träume in Ziele.
Sei der Kapitän deines Schicksals.
Konzentriere dich auf die Dinge, die du ändern kannst.
Du kannst alles erreichen, wenn du es wirklich willst.
Vertraue auf deinen Instinkt.
Investiere in deine Stärken und arbeite an deinen Schwächen.
Wenn du stolperst, stehe auf und gehe weiter.
Lass dich nicht von Rückschlägen entmutigen.
Eine negative Einstellung wird dich nie zu positiven Erfolgen bringen.
Je schwieriger der Weg, desto stolzer bist du auf das Ergebnis.
Glaube an dich selbst, egal was andere sagen.
Gib niemals auf, auch wenn es schwierig wird.
Vertraue auf deine Fähigkeiten und sei selbstbewusst.
Wenn es schwierig wird, denke daran, warum du angefangen hast.
Jeder Tag ist eine neue Chance, um erfolgreich zu sein.
Du bist der Einzige, der dich aufhalten kann.
Der Schlüssel zum Erfolg ist Durchhaltevermögen.
Sei stolz auf das, was du erreicht hast.
Die beste Art, etwas zu erreichen, ist es zu tun.
Die größte Motivation kommt aus dir selbst.
Ohne Ziel kommt auch keine Motivation.
Du kannst nur das in anderen entzünden, was in dir selbst brennt. – Augustinus von Hippo
Jeder kleine Schritt bringt dich näher an dein Ziel.
Wer nicht wagt, der nicht gewinnt. – Hans Sachs
Die größten Erfolge kommen aus den größten Herausforderungen.
In der Ruhe liegt die Kraft. - Konfuzius
Lass dich nicht von Rückschlägen entmutigen, sondern nutze sie als Treibstoff für deine Motivation. – Michael Jordan
Das Leben ist zu kurz, um es nicht mit voller Motivation zu leben.
Jeder neue Tag ist eine Chance, etwas Neues zu erreichen.
Es ist noch kein Meister vom Himmel gefallen. – Linus Paul
Nicht träumen, sondern machen.
Wenn du aufgibst, erfährst du nie, was daraus geworden wäre.
Jeder Fehler ist eine Chance, um zu lernen und besser zu werden.
Es ist nie zu spät, um anzufangen und etwas zu erreichen.
Jeder Tag ist ein Geschenk, nutze ihn sinnvoll.
Mache das Unmögliche möglich, indem du es einfach tust.
Wenn du aufhörst zu träumen, hörst du auf zu leben.
Das Leben ist eine Reise, genieße jeden Schritt auf dem Weg.
Es gibt keine Grenzen, außer denen, die du dir selbst setzt.
Du bist dein einziger Gegner.
Sei besser als die Person, die du gestern warst.
Fehler machen bedeutet keine Schwäche, sondern die Chance aus ihnen zu lernen.
Nur wer sich den Herausforderungen stellt, kann auch siegreich sein.
Durchhalten bedeutet, sich auf das Ziel zu fokussieren und nicht auf die Hindernisse.
Wenn du am Tiefpunkt bist, mach dich auf den Hochpunkt gefasst.
Nur wer durchhält, kann die Früchte seiner Arbeit ernten.
Wenn es einfach wäre, wäre es auch langweilig.
Nur wer durchhält, kann den Erfolg genießen und stolz auf sich sein.
Durchhalten bedeutet, auch in schwierigen Zeiten positiv zu bleiben.
Nur wer sein Ziel kennt, findet den Weg. - Laotse
Du bist nie zu alt, um dir ein neues Ziel zu setzen oder einen neuen Traum zu träumen. - C.S. Lewis
Wer immer tut, was er schon kann, bleibt immer das, was er schon ist. - Henry Ford
'''
liste = text.split("\n")

with socket.socket() as server_socket:
    server_socket.bind(('', 7710))
    server_socket.listen()

    while True:
        client, info = server_socket.accept()
        print(info, 'hat verbunden')

        print(client.recv(1000))

        client.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n<html><body>' + str(
            f'{info} <br><h1>Hello Jan!</h1><h2>{liste[random.randint(0, len(liste)-1)]}</h2>').encode(
            'utf-8') + b'</body></html>')
