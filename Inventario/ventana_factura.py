import tkinter as tk
from tkinter import *
from funciones import validacion_cantidad_productos, actualizar_productos_facturas, activar_factura, ultima_factura, cancelar_factura, crear_factura
from conexion_2 import conexion, cursor
from tkinter import messagebox
from tkinter import ttk



def boton_finalizar_factura(ventana_emergente: tk.Toplevel):
    id_factura = ultima_factura()
    consulta = f"SELECT * FROM det_factura WHERE id_factura = {id_factura};"
    cursor.execute(consulta)
    resultado = cursor.fetchone()
    cursor.fetchall()  # Consumir todos los resultados antes de ejecutar otra consulta
    # conexion.close()

    if resultado is not None: # Si el resultado no es None
        activar_factura()
        ventana_emergente.destroy()
        return
    
    mensaje = "Para poder finalizar la factura debe tener al menos un producto agregado. ¿Desea cancelar la factura?"
    respuesta = messagebox.askyesno("Error al finalizar", mensaje)
    if respuesta:
        print("respuesta sí")
        cancelar_factura()
        return
    
    print("respuesta no")
    ventana_facturas(ventana_emergente)


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
    # ventana_facturas.state('zoomed')  # Abre la ventana maximizada

    # crear_factura()

    lista_de_productos = OptionMenu(ventana_facturas, var_seleccion, *diccionario.keys())
    label_producto = tk.Label(ventana_facturas, text="Producto:")
    label_cantidad = tk.Label(ventana_facturas, text="Cantidad:")
    entry_cantidad = tk.Entry(ventana_facturas)

    tabla_detalles = ttk.Treeview(ventana_facturas)
    tabla_detalles['columns'] = ("Producto", "Cantidad", "Precio", "Total") # Definir las columnas
    
    # Definir encabezados de columna
    tabla_detalles.heading("#0", text="", anchor="w")
    tabla_detalles.heading("Producto", text="Producto", anchor="w")
    tabla_detalles.heading("Precio", text="Precio", anchor="w")
    tabla_detalles.heading("Cantidad", text="Cantidad", anchor="w")
    tabla_detalles.heading("Total", text="Total", anchor="w")

    # Definir el ancho de las columnas
    tabla_detalles.column("#0", width=0, stretch=tk.NO)
    tabla_detalles.column("Producto", width=200, anchor="w")
    tabla_detalles.column("Precio", width=150, anchor="w")
    tabla_detalles.column("Cantidad", width=100, anchor="w")
    tabla_detalles.column("Total", width=100, anchor="w")
    
    tabla_detalles.grid(row=4, column=0, columnspan=4)
    
    # Crear una etiqueta para mostrar el total a pagar
    label_total = tk.Label(ventana_facturas, text="Total a pagar: $0.00")
    label_total.grid(row=5, column=0, columnspan=2)

    button_agregar = tk.Button(ventana_facturas, text="Agregar", command=lambda: validacion_cantidad_productos(var_seleccion, entry_cantidad, diccionario, tabla_detalles))

    #Establecemos la posicion de cada componente de la ventana
    label_producto.grid(row=0, column=0)
    lista_de_productos.grid(row=0, column=1)
    label_cantidad.grid(row=1, column=0)
    entry_cantidad.grid(row=1, column=1)
    lista_de_productos.focus_set()

    button_agregar.grid(row=6, column=0)
    boton_finalizar = tk.Button(ventana_facturas, text="Finalizar", command= lambda: [boton_finalizar_factura(ventana_facturas)])
    boton_finalizar.grid(row=6, column=1)
    actualizar_productos_facturas(tabla_detalles, label_total)
