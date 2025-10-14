import psycopg
import tkinter as tk

db_conn: psycopg.Connection  # type hint für PyCharm
# ---------------------------------------------------------------------------------------------------------------------
# Verbindung mit der DB aufbauen
# ---------------------------------------------------------------------------------------------------------------------

try:
    with psycopg.connect(dbname="prg_fitness",
                         user="postgres",
                         password="password",
                         host="localhost",
                         port="5432",
                         autocommit=True) as db_conn:
        # -------------------------------------------------------------------------------------------------------------
        # tk applikation
        # -------------------------------------------------------------------------------------------------------------
        with db_conn.cursor() as cursor:
            cursor.execute('''SELECT bild
                              FROM bilder
                              WHERE person = 2''')
            fenster = tk.Tk()
            bild = tk.PhotoImage(data=cursor.fetchone()[0])
            tk.Label(fenster, image=bild).pack()
            fenster.mainloop()


except psycopg.DatabaseError as e:
    print(e, type(e))
