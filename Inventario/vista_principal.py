import tkinter as tk
from tkinter import *
from conexion_2 import conexion, cursor

# Función de controlador de eventos para el evento Enter (hover)
def on_enter(event):
    event.widget.config(bg="blue")

# Función de controlador de eventos para el evento Leave (fuera del hover)
def on_leave(event):
    event.widget.config(bg="SystemButtonFace")

# Funciones de ejemplo para las opciones del submenú
def opcion1():
    print("Se seleccionó la Opción 1")

def opcion2():
    print("Se seleccionó la Opción 2")

def opcion3():
    print("Se seleccionó la Opción 3")

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Inventario number 2")

# Maximizar la ventana al inicio
ventana_principal.state("zoomed")

# Crear los widgets de la GUI
botones = {
    "facturas": tk.Button(ventana_principal, text="Facturas", command="ventana_facturas", width=10, height=2, cursor="hand2"),
    "inventario": tk.Button(ventana_principal, text="Inventario", command="ventana_nuevo", width=10, height=2, cursor="hand2"),
    "Reporte": tk.Menubutton(ventana_principal, text="Reporte", width=10, height=2, cursor="hand2")
}

button_nuevo = botones["inventario"]
button_facturas = botones["facturas"]
botton_reporte = botones["Reporte"]

# Crear el submenú
menu_reporte = tk.Menu(botton_reporte, tearoff=False)
botton_reporte.config(menu=menu_reporte)

# Agregar las opciones del submenú y vincularlas a las funciones
menu_reporte.add_command(label="Opción 1", command=opcion1)
menu_reporte.add_command(label="Opción 2", command=opcion2)
menu_reporte.add_command(label="Opción 3", command=opcion3)

# Vincular eventos Enter y Leave a las funciones de controlador de eventos
button_nuevo.bind("<Enter>", on_enter)
button_nuevo.bind("<Leave>", on_leave)
button_facturas.bind("<Enter>", on_enter)
button_facturas.bind("<Leave>", on_leave)
botton_reporte.bind("<Enter>", on_enter)
botton_reporte.bind("<Leave>", on_leave)

# Ubicar los widgets en la ventana_principal
button_nuevo.grid(row=6, column=0)
button_facturas.grid(row=6, column=1)
botton_reporte.grid(row=6, column=2)

# Ejecutar la aplicación
ventana_principal.mainloop()
