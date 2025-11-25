import tkinter as tk
import os
import math

CHARACTERS = [
    {
        "Name": "Geralt of Rivia",
        "Species": "Witcher",
        "Gender": "Male",
        "Age_Group": "Adult",
        "Origin_or_Region": "Kaer Morhen / Rivia",
        "Affiliation": "Wolf School",
        "Role_or_Occupation": "Monster slayer",
        "Notable_Traits": "stoic, moral code",
        "Abilities_or_Skills": "Signs, swordsmanship",
        "First_Appearance": "The Last Wish",
        "Strength": 85, "Health": 90, "Mana": 40, "Level": 70,
        "Image": "bilder/1.png",  # PNG/GIF wird von tk.PhotoImage unterstützt
    },
    # weitere Charaktere hier ...
]

class WitcherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Witcher Charaktere")
        self.geometry("980x560")

        self._img_cache = None  # wichtig: Referenz halten

        # Layout
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Left: Listbox
        left = tk.Frame(self, padx=8, pady=8)
        left.grid(row=0, column=0, sticky="ns")

        tk.Label(left, text="Charaktere").pack(anchor="w")

        self.listbox = tk.Listbox(left, height=25, width=28)
        self.listbox.pack(fill="y")
        for c in CHARACTERS:
            self.listbox.insert("end", c["Name"])
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        # Right: Details
        right = tk.Frame(self, padx=8, pady=8)
        right.grid(row=0, column=1, sticky="nsew")
        right.columnconfigure(0, weight=1)
        right.rowconfigure(1, weight=1)

        # Image area
        self.image_label = tk.Label(right, anchor="nw", justify="left")
        self.image_label.grid(row=0, column=0, sticky="nw")

        # Stats + text
        self.text = tk.Text(right, height=22, wrap="word")
        self.text.grid(row=1, column=0, sticky="nsew", pady=(8, 0))
        self.text.configure(state="disabled")

        # Preselect first
        if CHARACTERS:
            self.listbox.selection_set(0)
            self.show_character(CHARACTERS[0])

    def on_select(self, _evt=None):
        sel = self.listbox.curselection()
        if not sel:
            return
        self.show_character(CHARACTERS[sel[0]])

    def _load_photoimage_fit(self, path, max_w=420, max_h=420):
        """
        Lädt ein PNG/GIF ohne PIL und passt es mit integer subsample an.
        Falls Bild kleiner ist, bleibt es unverändert.
        """
        img = tk.PhotoImage(file=path)
        w, h = img.width(), img.height()

        if w <= max_w and h <= max_h:
            return img

        # integer factor berechnen (nur subsample möglich)
        factor = max(w / max_w, h / max_h)
        factor_int = max(1, math.ceil(factor))

        # subsample reduziert um ganzzahligen Faktor
        img_small = img.subsample(factor_int, factor_int)
        return img_small

    def show_character(self, c):
        # update image
        path = c.get("Image")
        if path and os.path.exists(path):
            try:
                self._img_cache = self._load_photoimage_fit(path)
                self.image_label.configure(image=self._img_cache, text="")
            except tk.TclError:
                self._img_cache = None
                self.image_label.configure(image="", text="(Bildformat nicht unterstützt)")
        else:
            self._img_cache = None
            self.image_label.configure(image="", text="(kein Bild)")

        # update text
        lines = [
            f"Name: {c['Name']}",
            f"Spezies: {c['Species']}",
            f"Geschlecht: {c['Gender']}",
            f"Alter: {c['Age_Group']}",
            f"Herkunft: {c['Origin_or_Region']}",
            f"Fraktion: {c['Affiliation']}",
            f"Rolle: {c['Role_or_Occupation']}",
            f"Traits: {c['Notable_Traits']}",
            f"Skills: {c['Abilities_or_Skills']}",
            f"Erster Auftritt: {c['First_Appearance']}",
            "",
            f"Stärke: {c['Strength']}/100",
            f"Leben:  {c['Health']}/100",
            f"Mana:   {c['Mana']}/100",
            f"Level:  {c['Level']}/100",
        ]

        self.text.configure(state="normal")
        self.text.delete("1.0", "end")
        self.text.insert("1.0", "\n".join(lines))
        self.text.configure(state="disabled")


if __name__ == "__main__":
    WitcherApp().mainloop()
