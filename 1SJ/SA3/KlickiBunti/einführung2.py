import tkinter as tk

fenster = tk.Tk()

def hallo():
    print("Hallo")

button_breite = 50
tk.Button(text='a', width=button_breite).pack()
tk.Button(text='bbbbbbbb', width=button_breite, background='green').pack()
tk.Button(text='exit', width=button_breite, command=fenster.destroy, font='arial').pack()
tk.Button(text='ddddd', width=button_breite, command=hallo).pack(side=tk.TOP)

fenster.mainloop()