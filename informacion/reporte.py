import mysql.connector
from tkinter import *
from tkinter import ttk

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="invetario_python"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM inventario")

result = mycursor.fetchall()

# Crear ventana principal
root = Tk()
root.geometry("1000x400")

# Crear Treeview widget
tree = ttk.Treeview(root, columns=("id", "nombre", "tipo", "cantidad", "precio_compra"))

# Agregar encabezados de columna
tree.heading("#0", text="id")
tree.heading("#1", text="Nombre")
tree.heading("#2", text="Tipo")
tree.heading("#3", text="Cantidad")  # Alinear al centro
tree.heading("#4", text="Precio de compra")  # Alinear al centro


# Agregar datos a Treeview
for row in result:
    tree.insert("", END, text=row[0], values=(row[0], row[1], row[2], row[3], row[4]))

# Centrar contenido en columnas
    tree.tag_configure('centered', anchor='center')
    for col in tree["columns"]:
        tree.column(col, anchor="center")

# Empaquetar Treeview
tree.pack()

# Ejecutar la ventana principal
root.mainloop()
