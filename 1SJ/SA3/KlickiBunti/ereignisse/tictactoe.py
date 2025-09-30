import tkinter as tk

def wechsel():
    global spieler
    spieler = "O" if spieler == 'X' else 'X'

spieler = 'X'

fenster = tk.Tk()
fenster.geometry()

frame = tk.Frame(fenster)
frame.pack()

buttons = []

# --------- Spielfeld ---------
for i in range(3):
    zeilen_frame = tk.Frame(frame)
    zeilen_frame.pack()
    for j in range(3):
        index = i * 3 + j
        btn = tk.Button(zeilen_frame, text=f"{i,j}", width=15, height=8)
        btn.pack(side='left')
        buttons.append(btn)



wechsel()
print(spieler)
wechsel()
print(spieler)
wechsel()
print(spieler)

fenster.mainloop()