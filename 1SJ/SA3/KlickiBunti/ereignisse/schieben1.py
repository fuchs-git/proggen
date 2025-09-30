import tkinter as tk
from tkinter import Label

# fenster = tk.Tk()
# fenster.geometry('200x200')
# x = tk.IntVar()
#
# widget = tk.Scale(variable=x, from_=15, to=100, orient=tk.HORIZONTAL).pack()
# tk.Button(command=lambda: print(x.get()), width=10, text='Press').pack()
#
# fenster.mainloop()

# Schieben 2 --------------------------------------------------------------------------------------
# fenster = tk.Tk()
# fenster.geometry('200x200')
# x = tk.DoubleVar()
#
# widget = tk.Scale(variable=x, from_=1, to=10, orient=tk.HORIZONTAL, resolution=0.1).pack()
# tk.Button(command=lambda: print(x.get()), width=10, text='Press').pack()
#
# fenster.mainloop()


# Schieben 3 --------------------------------------------------------------------------------------
# fenster = tk.Tk()
# fenster.geometry('200x200')
# x = tk.DoubleVar()
#
# widget = tk.Scale(variable=x, from_=1, to=10, orient=tk.HORIZONTAL, resolution=0.1).pack()
# lbl = tk.Label(textvariable=x).pack()
#
# fenster.mainloop()

# Schieben 4 --------------------------------------------------------------------------------------
# fenster = tk.Tk()
# fenster.geometry('200x200')
#
# x = tk.DoubleVar()
# tk.Scale(from_=1, to=10, orient=tk.HORIZONTAL, resolution=0.1, command=lambda y: x.set(y)).pack()
# tk.Label(textvariable=x).pack()
#
# fenster.mainloop()


# Ja oder Nein 1 --------------------------------------------------------------------------------------

# fenster = tk.Tk()
# fenster.geometry('200x200')
#
# x1 = tk.IntVar()
# x2 = tk.BooleanVar()
#
# check1 = tk.Checkbutton(variable=x1, text='Option 1')
# check1.pack()
#
# check2 = tk.Checkbutton(variable=x2, text='Option 2')
# check2.pack()
#
# tk.Button(command=lambda: print(x1.get(), x2.get()), width=10, text='Ausgabe').pack()
#
# fenster.mainloop()

# Ja oder Nein 2 --------------------------------------------------------------------------------------
# fenster = tk.Tk()
# fenster.geometry('200x200')
#
# x1 = tk.IntVar()
# x2 = tk.BooleanVar()
#
# check1 = tk.Checkbutton(variable=x1, text='Option 1')
# check1.pack()
#
# check2 = tk.Checkbutton(variable=x2, text='Option 2')
# check2.pack()
#
# tk.Label(textvariable=x1).pack()
# tk.Label(textvariable=x2).pack()
#
# fenster.mainloop()


# Eins von vielen 1 --------------------------------------------------------------------------------------
# fenster = tk.Tk()
# fenster.geometry('200x200')
#
# x = tk.IntVar()
#
# tk.Radiobutton(variable=x, text='Option 1', value=1).pack()
# tk.Radiobutton(variable=x, text='Option 2', value=2).pack()
# tk.Radiobutton(variable=x, text='Option 3', value=3).pack()
# tk.Button(text='Button', command=lambda: print(x.get())).pack()
#
# fenster.mainloop()

# Eins von vielen 2 --------------------------------------------------------------------------------------
# fenster = tk.Tk()
# fenster.geometry('200x200')
#
# x = tk.IntVar()
#
# tk.Radiobutton(variable=x, text='Option 1', value=1).pack()
# tk.Radiobutton(variable=x, text='Option 2', value=2).pack()
# tk.Radiobutton(variable=x, text='Option 3', value=3).pack()
# tk.Label(textvariable=x).pack()
#
# fenster.mainloop()

# Eins von vielen 3 --------------------------------------------------------------------------------------
# zutaten = "Eier Tomaten Käse".split()
#
# fenster = tk.Tk()
# fenster.geometry('200x200')
#
# auswahl = tk.StringVar()
# lbl1 = tk.Label(textvariable=auswahl)
# lbl1.pack()
#
# x = tk.IntVar()
#
# auswahl.set(zutaten[0])
# [tk.Radiobutton(variable=auswahl, text=zutaten[i], value=i, anchor=tk.W).pack(fill=tk.X) for i in range(len(zutaten))]
#
# fenster.mainloop()

# # Eins oder viele von vielen 1 --------------------------------------------------------------------------------------
# einkaufen = "Eier Tomaten Käse Brot Bonbons".split()
#
# fenster = tk.Tk()
# fenster.geometry('200x300')
#
# lb = tk.Listbox()
# lb.pack()
#
# # [lb.insert(i,x) for i,x in enumerate(einkaufen)]
# lb.insert(0, *einkaufen)
#
# tk.Button(text='Button', command=lambda: print(lb.curselection())).pack()
# tk.Button(text='Honig', command=lambda: lb.insert(4, 'Honig')).pack()
#
# tk.Button(text=u'\u2b06', command=lambda:lb.see(0)).pack()
# tk.Button(text=u'\u2193', command=lambda:lb.see("end")).pack()
#
# fenster.mainloop()


# Eins oder viele von vielen 2 --------------------------------------------------------------------------------------
einkaufen = "Eier Tomaten Käse Brot Bonbons".split()

fenster = tk.Tk()
fenster.geometry('200x300')

lb = tk.Listbox(selectmode=tk.MULTIPLE)
lb.pack()

# [lb.insert(i,x) for i,x in enumerate(einkaufen)]
lb.insert(0, *einkaufen)

tk.Button(text='Button', command=lambda: print(lb.curselection())).pack()
tk.Button(text='Honig', command=lambda: lb.insert(4, 'Honig')).pack()

tk.Button(text=u'\u2b06', command=lambda:lb.see(0)).pack()
tk.Button(text=u'\u2193', command=lambda:lb.see('end')).pack()

fenster.mainloop()
