import tkinter as tk

fenster = tk.Tk()
fenster.geometry('750x500')
fenster.title("FitnessCenter")

# Hintergrund
bg_img = tk.PhotoImage(file='src/bg1.png').subsample(2, 2)
background = tk.Label(fenster, image=bg_img)
background.place(x=0, y=0, relwidth=1, relheight=1)
background.lower()


# Gleiche Höhe: gleiche ROW!
name = tk.Entry(fenster, width=20, font=('Arial', 18))
name.grid(row=1, column=0, padx=(400,8), pady=200)

btn = tk.Button(fenster, text='Login')
btn.grid(row=1, column=1, padx=0, pady=8)

fenster.mainloop()