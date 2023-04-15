import tkinter as tk
from tkinter import *
from ventana_factura import ventana_facturas
from grafico_productos import producto_mas_vendido
from grafico_ventas import ventas_por_mes
from grafico_ventas_pastel import ventas_por_mes_pastel
from ventana_productos import productos

# Función de controlador de eventos para el evento Enter (hover)
def on_enter(event):
    event.widget.config(bg="#96f321")

# Función de controlador de eventos para el evento Leave (fuera del hover)
def on_leave(event):
    event.widget.config(bg="SystemButtonFace")

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Inventario")

# Maximizar la ventana al inicio
ventana_principal.state("zoomed")

# Crear los widgets de la GUI
botones = {
    "facturas": tk.Button(ventana_principal, text="Facturas", command=lambda : ventana_facturas(ventana_principal), width=10, height=2, cursor="hand2"),
    "inventario": tk.Button(ventana_principal, text="Inventario", command=lambda : productos(), width=10, height=2, cursor="hand2"),
    "Reporte": tk.Menubutton(ventana_principal, text="Reporte", width=10, height=2, cursor="hand2")
}

button_nuevo = botones["inventario"]
button_facturas = botones["facturas"]
botton_reporte = botones["Reporte"]

# Configurar el tamaño de fuente en los botones
font_size = 10  # Tamaño de fuente deseado
button_nuevo.config(font=("Helvetica", font_size))
button_facturas.config(font=("Helvetica", font_size))
botton_reporte.config(font=("Helvetica", font_size))

# Crear el submenú
menu_reporte = tk.Menu(botton_reporte, tearoff=False)
botton_reporte.config(menu=menu_reporte)

# Agregar las opciones del submenú y vincularlas a las funciones
menu_reporte.add_command(label="producto mas vendido", command=producto_mas_vendido)
menu_reporte.add_command(label="ventas por mes", command=ventas_por_mes)
menu_reporte.add_command(label="ventas por mes pastel", command=ventas_por_mes_pastel)

# Vincular eventos Enter y Leave a las funciones de controlador de eventos
button_nuevo.bind("<Enter>", on_enter)
button_nuevo.bind("<Leave>", on_leave)
button_facturas.bind("<Enter>", on_enter)
button_facturas.bind("<Leave>", on_leave)
botton_reporte.bind("<Enter>", on_enter)
botton_reporte.bind("<Leave>", on_leave)

# Configurar la geometría de cuadrícula para centrar los botones
button_nuevo.grid(row=1, column=0, sticky='nsew')
button_facturas.grid(row=1, column=1, sticky='nsew')
botton_reporte.grid(row=1, column=2, sticky='nsew')

# Configurar las columnas y filas para que se expandan y llenen todo el espacio disponible
ventana_principal.columnconfigure(0, weight=1)
ventana_principal.columnconfigure(1, weight=1)
ventana_principal.columnconfigure(2, weight=1)
ventana_principal.rowconfigure(1, weight=1)
# Ejecutar la aplicación
ventana_principal.mainloop()
