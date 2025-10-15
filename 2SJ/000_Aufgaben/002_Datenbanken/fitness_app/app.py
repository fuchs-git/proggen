import tkinter as tk
from tkinter import filedialog, messagebox
import psycopg
import base64

DB = dict(
    dbname="prg_fitness_app",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

def save_person_to_db(name: str, age: int, image_path: str) -> int:
    """Speichert Person in person und Bild (als BYTEA) in bilder. Gibt person.id zurück."""
    with psycopg.connect(**DB, autocommit=False) as conn:
        try:
            with conn.cursor() as cur:
                # 1) Person
                cur.execute(
                    'INSERT INTO person (name, alter) VALUES (%s, %s) RETURNING id;',
                    (name, age)
                )
                person_id = cur.fetchone()[0]

                # 2) Bild als BYTEA (rohe Bytes)
                with open(image_path, 'rb') as f:
                    bild = f.read()
                    cur.execute('INSERT INTO bilder (person, bild) VALUES (%s,%b)', (person_id, bild))


            conn.commit()
            return person_id
        except Exception:
            conn.rollback()
            raise

fenster = tk.Tk()
fenster.geometry('750x500')
fenster.title("FitnessCenter")

# Hintergrund
bg_label = tk.Label(fenster)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()
_bg_ref = None

def set_background(path: str):
    global _bg_ref
    _bg_ref = tk.PhotoImage(file=path).subsample(2, 2)
    bg_label.config(image=_bg_ref)

def clear_content():
    for w in fenster.winfo_children():
        if w is bg_label:
            continue
        w.destroy()

# ---------- HOME (deine Ausrichtung unverändert) ----------
def show_home():
    clear_content()
    set_background('src/bg1.png')

    name = tk.Entry(fenster, width=20, font=('Arial', 18))
    name.grid(row=1, column=0, padx=(400, 8), pady=200)

    btn = tk.Button(fenster, text='Login')
    btn.grid(row=1, column=1, padx=0, pady=200)

    tk.Button(fenster, text='Registrieren', command=create_person)\
      .grid(row=2, column=0, columnspan=2, pady=(10, 0))

# ---------- REGISTRIEREN (ohne Pillow) ----------
PREVIEW_W, PREVIEW_H = 200, 140  # Zielbox in Pixeln

def create_person():
    clear_content()
    set_background('src/bg2.png')

    fenster.name_var = tk.StringVar()
    fenster.age_var  = tk.StringVar()
    fenster.selected_image_path = None
    fenster.preview_img_ref = None      # skaliertes Bild
    fenster.preview_img_orig = None     # Original-PhotoImage

    tk.Label(fenster, text='Person anlegen').grid(row=0, column=0, columnspan=3, pady=(20, 12))

    tk.Label(fenster, text='Name:').grid(row=1, column=0, sticky='e', padx=(20, 8), pady=4)
    tk.Entry(fenster, width=24, textvariable=fenster.name_var)\
        .grid(row=1, column=1, sticky='w', padx=(0, 20), pady=4)

    tk.Label(fenster, text='Alter:').grid(row=2, column=0, sticky='e', padx=(20, 8), pady=4)
    tk.Entry(fenster, width=24, textvariable=fenster.age_var)\
        .grid(row=2, column=1, sticky='w', padx=(0, 20), pady=4)

    tk.Label(fenster, text='Bild:').grid(row=3, column=0, sticky='e', padx=(20, 8), pady=4)
    tk.Button(fenster, text='Bild wählen…', command=pick_image_no_pillow)\
        .grid(row=3, column=1, sticky='w', padx=(0, 20), pady=4)

    # Vorschau-Box in Pixeln (grauer Rahmen, bleibt kompakt)
    preview_frame = tk.Frame(fenster, width=PREVIEW_W, height=PREVIEW_H, relief='groove', bd=1)
    preview_frame.grid(row=1, column=2, rowspan=3, padx=(0, 20), pady=4)
    preview_frame.grid_propagate(False)
    fenster.preview_label = tk.Label(preview_frame, text='(Vorschau)')
    fenster.preview_label.place(relx=0.5, rely=0.5, anchor='center')

    tk.Button(fenster, text='Zurück', command=show_home).grid(row=5, column=0, pady=(16, 0))
    tk.Button(fenster, text='Speichern', command=validate_form).grid(row=5, column=1, pady=(16, 0))

def pick_image_no_pillow():
    path = filedialog.askopenfilename(
        title="Bild auswählen",
        filetypes=[("Bilder (PNG/GIF/PPM/PGM)", "*.png *.gif *.ppm *.pgm")]
    )
    if not path:
        return
    fenster.selected_image_path = path

    try:
        # Original laden
        orig = tk.PhotoImage(file=path)
        fenster.preview_img_orig = orig  # Referenz halten

        ow, oh = orig.width(), orig.height()

        # Skalierungsfaktor (ganzzahlig) wählen, um in Box zu passen (nur Verkleinern)
        fx = max(1, ow // PREVIEW_W)
        fy = max(1, oh // PREVIEW_H)
        factor = max(1, min(fx, fy))  # größtmögl. Reduzierung, die noch reinpasst

        if factor > 1:
            scaled = orig.subsample(factor, factor)
        else:
            # Keine Verkleinerung nötig – Original anzeigen (kein echtes Upscaling ohne Pillow)
            scaled = orig

        fenster.preview_img_ref = scaled  # Referenz halten
        fenster.preview_label.config(image=scaled, text="")
    except Exception as e:
        messagebox.showerror("Fehler", f"Bild konnte nicht geladen werden:\n{e}")

def validate_form():
    name = fenster.name_var.get().strip()
    age_s = fenster.age_var.get().strip()
    img = fenster.selected_image_path

    # Plausibilitätsprüfungen
    if not name:
        messagebox.showwarning("Hinweis", "Bitte einen Namen eingeben.")
        return
    try:
        age = int(age_s)
        if age < 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Hinweis", "Bitte ein gültiges Alter (Ganzzahl ≥ 0) eingeben.")
        return
    if not img:
        messagebox.showwarning("Hinweis", "Bitte ein Bild auswählen (PNG/GIF/PPM/PGM).")
        return

    # DB-Save
    try:
        new_id = save_person_to_db(name, age, img)
        messagebox.showinfo("Gespeichert",
                            f"Person #{new_id} wurde angelegt.\n\nName: {name}\nAlter: {age}")
        show_home()  # zurück zur Startansicht (optional)
    except Exception as e:
        messagebox.showerror("Fehler beim Speichern", str(e))
# Start
show_home()
fenster.mainloop()

def debug_db(cur):
    cur.execute("SELECT current_database(), current_schema(), current_setting('search_path');")
    print(cur.fetchone())  # (db, schema, search_path)

    cur.execute("SELECT to_regclass('public.bilder');")
    print("public.bilder =", cur.fetchone()[0])  # None = Tabelle wird nicht gefunden

with psycopg.connect(**DB, autocommit=False) as conn:
    with conn.cursor() as cur:
        debug_db(cur)
        ...
