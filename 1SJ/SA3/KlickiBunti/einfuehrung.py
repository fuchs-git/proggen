import tkinter as tk

fenster = tk.Tk()
fenster.geometry("500x400")
fenster.title("Proggen")
tk.Label(master=fenster, text="Proggen",
                 bg="black", fg="white",
                 padx=400, pady=10).pack()

def sag_hallo():
    print("Hallo")

button = tk.Button(text="Ein Button, der 'Hallo' sagt", command=sag_hallo )
button.pack()

fenster.mainloop()
