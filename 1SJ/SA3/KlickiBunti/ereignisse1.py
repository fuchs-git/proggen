import tkinter as tk

def hallo(nummer=None):
    print(f"Hallo {nummer if nummer else ''}".strip())

# Button
fenster1 = tk.Tk()
fenster1.title("Ein Button")
tk.Button(fenster1, text="Sag Hallo", command=lambda: hallo(), padx=20, pady=10).pack(padx=20, pady=20)
fenster1.mainloop()

# Buttons
fenster2 = tk.Tk()
fenster2.title("Fünf Buttons")
[tk.Button(fenster2, text=f"Button {i}", command=lambda x=i: hallo(x), padx=20, pady=5).pack(pady=5) for i in range(1, 6)]
fenster2.mainloop()

# mehr Buttons
fenster3 = tk.Tk()
fenster3.title("15 Buttons")
frame = tk.Frame(fenster3)
frame.pack(padx=20, pady=20)

for i in range(5):
    for j in range(3):
        nummer = i * 3 + j + 1
        button = tk.Button(frame, text=f"Button {nummer}", command=lambda x=nummer: hallo(x), padx=10, pady=5)
        button.grid(row=i, column=j, padx=5, pady=5)

#[[tk.Button(frame, text=f"Button {i*3+j+1}", command=lambda x=i*3+j+1: hallo(x), padx=10, pady=5).grid(row=i, column=j, padx=5, pady=5) for j in range(3)] for i in range(5)]

fenster3.mainloop()