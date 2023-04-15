import tkinter as tk

app = tk.TK()

app.geometry("600x300")

app.configure(background="black")
tk.Wm.wm_title(app, "Hola Crack")

tk.Button(app, text="Karol",font=("courier", 14),bg="#00a8e8",fg="white").pack(fill=tk.BOTH, expand=True)


app.mainloop()

