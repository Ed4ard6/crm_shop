import tkinter as tk
from tkinter import *
from funciones import validacion_cantidad_productos, actualizar_productos_facturas, actualizar_productos, limpiar_campos, agregar_producto, crear_factura, agregar_detalles_factura, limpiar_formulario_detalles_fatura, activar_factura
from conexion_2 import conexion, cursor

def boton_finalizar_factura(ventana_emergente : tk.Toplevel):
    ventana_emergente.destroy()
    activar_factura()


def ventana_facturas(ventana_principal):
    # listado_productos_agregar()
    #Obtener los datos de la tabla producto
    query = "SELECT nombre_producto, id FROM producto"
    cursor.execute(query)
    datos = cursor.fetchall()
    diccionario = dict((nombre, id) for nombre, id in datos)
    var_seleccion = StringVar()

    ventana_facturas = tk.Toplevel(ventana_principal)
    ventana_facturas.title("Registrar Factura")
    ventana_facturas.geometry("500x250")
    #crear_factura()

    lista_de_productos = OptionMenu(ventana_facturas, var_seleccion, *diccionario.keys())
    label_producto = tk.Label(ventana_facturas, text="Producto:")
    label_cantidad = tk.Label(ventana_facturas, text="Cantidad:")
    entry_cantidad = tk.Entry(ventana_facturas)

    detalles_de_factura = tk.Listbox(ventana_facturas, height=10, width=120)
    
    detalles_de_factura.grid(row=4, column=0, columnspan=4)
    
    button_agregar = tk.Button(ventana_facturas, text="Agregar", command=lambda: validacion_cantidad_productos(var_seleccion, entry_cantidad, diccionario, detalles_de_factura))

    #Establecemos la posicion de cada componente de la ventana
    label_producto.grid(row=0, column=0)
    lista_de_productos.grid(row=0, column=1)
    label_cantidad.grid(row=1, column=0)
    entry_cantidad.grid(row=1, column=1)
    lista_de_productos.focus_set()

    button_agregar.grid(row=6, column=0)

    boton_finalizar = tk.Button(ventana_facturas, text="Finalizar", command= lambda: [boton_finalizar_factura(ventana_facturas)])
    boton_finalizar.grid(row=6, column=1)
    actualizar_productos_facturas(detalles_de_factura)
