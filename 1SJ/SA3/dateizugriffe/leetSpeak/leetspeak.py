import tkinter as tk
import pyperclip



def leet_conv(text):
    klartext = 'A,a,E,e,F,f,G,g,I,i,L,l,O,o,S,s,T,t,Y,y,Z,z'.split(',')
    leet = '4,4,3,3,Ph,ph,6,9,!,!,1,1,0,0,5,5,7,7,°/,°/,2,2'.split(',')
    leet_speak = ''
    text = text.replace('!!','!1')
    for index, char in enumerate(text):
        try:
            if char in klartext:
                leet_speak += leet[klartext.index(char)]
            else: leet_speak += char
        except IndexError:
            pass
    return leet_speak

def btn():
    wert = eingabe.get()
    lbl_ausgabe.configure(text=leet_conv(wert))
    pyperclip.copy(leet_conv(wert))




fenster = tk.Tk()
fenster.title("L33tSp3ak-Generator")
fenster.geometry('500x400')
tk.Label(text='Text der übersetzt werden soll:').pack(padx=25, pady=5)
eingabe = tk.Entry(width=200)
eingabe.pack(padx=25, pady=25)
tk.Button(text="1337 7h!5", command=btn).pack(padx=25, pady=5)
lbl_ausgabe = tk.Label(text='C0nv3rt3t T3xt')
lbl_ausgabe.pack()


fenster.mainloop()



