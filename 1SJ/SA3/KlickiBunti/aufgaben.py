import tkinter as tk

# a.
# a = tk.Tk()
# a.geometry("100x50")
# tk.Label(text='Hallo', bg='yellow').pack(pady=10)
# tk.Label(text="welt", bg="green").pack(pady=10, padx=10, fill=tk.X)

#
# # b.
# b = tk.Tk()
# b.geometry("100x50")

# tk.Label(text="hallo", bg='yellow').pack(side=tk.LEFT, padx=10, pady=10, expand=True)
# tk.Label(text="Welt", bg='green').pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

fenster = tk.Tk()
fenster.geometry("500x400")
# fenster.title("Proggen")
# tk.Frame(fenster, height=60, width=60, bg="yellow").pack(side=tk.LEFT, padx=10, pady=10)
# tk.Frame(fenster, height=60, width=60, bg="green").pack(side=tk.LEFT,fill=tk.BOTH, expand=tk.TRUE, padx=10, pady=10)
#
# tk.Frame(fenster, height=60, width=60, bg="yellow").pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE, padx=10, pady=10)
# tk.Frame(fenster, height=60, width=60, bg="green").pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE, padx=10, pady=10)
#-----------------------------------------------------------------------------------------------------------------------
# frame_top = tk.Frame(fenster)
# frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)
#
# tk.Frame(frame_top, bg="yellow", width=90, height=90).pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
# tk.Frame(frame_top, bg="green", width=90, height=90).pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
#
#
# frame_bottom = tk.Frame(fenster)
# frame_bottom.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)
#
# tk.Frame(frame_bottom, bg="red", width=90, height=90).pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
# tk.Frame(frame_bottom, bg="blue", width=90, height=90).pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
#-----------------------------------------------------------------------------------------------------------------------
frame_top = tk.Frame(fenster)
frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

tk.Label(frame_top, text="Hallo", bg="yellow", width=90, height=90).pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
tk.Label(frame_top, bg="green", width=90, height=90).pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)


frame_bottom = tk.Frame(fenster)
frame_bottom.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

tk.Frame(frame_bottom, bg="red", width=90, height=90).pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
tk.Frame(frame_bottom, bg="blue", width=90, height=90).pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

tk.mainloop()


