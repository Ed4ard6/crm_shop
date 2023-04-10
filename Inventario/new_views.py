import tkinter as tk
from tkinter import ttk
from conexion_2 import conexion, cursor


class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.treeview = ttk.Treeview(self.master, columns=("ID", "Producto", "Categoría", "Precio compra", "Cantidad", "Precio venta", "Estado"))
        self.treeview.heading("#0", text="ID")
        self.treeview.heading("#1", text="Producto")
        self.treeview.heading("#2", text="Categoría")
        self.treeview.heading("#3", text="Precio compra")
        self.treeview.heading("#4", text="Cantidad")
        self.treeview.heading("#5", text="Precio venta")
        self.treeview.heading("#6", text="Estado")
        self.treeview.pack()

        # Obtener los datos de la tabla
        query = "SELECT * FROM producto"
        cursor.execute(query)
        datos = cursor.fetchall()

        for row in datos:
            self.treeview.insert("", "end", text=row[0], values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

if __name__ == '__main__':
    root = tk.Tk()
    ventana_principal = VentanaPrincipal(root)
    root.mainloop()

