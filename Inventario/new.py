import tkinter as tk
from tkinter import *
from funciones import validacion_cantidad_productos, actualizar_productos_facturas, actualizar_productos, limpiar_campos, agregar_producto, crear_factura, agregar_detalles_factura, limpiar_formulario_detalles_fatura, activar_factura
from conexion_2 import conexion, cursor
import pandas as pd
from grafico_productos import producto_mas_vendido
from grafico_ventas import ventas_por_mes
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from decimal import Decimal 





def deshabilitar_botones():
    for boton in botones.values():
        boton.configure(state="disabled")

def habilitar_botones():

    button_nuevo.configure(state="normal")
    button_facturas.configure(state="normal")
    # for boton in botones.values():
    #     boton.configure(state="normal")


def ventana_nuevo():
    deshabilitar_botones()
    print("ventana_nuevo....")
    ventana_emergente = tk.Toplevel(ventana_principal)
    ventana_emergente.title("Registrar nuevo producto")
    ventana_emergente.geometry("300x250")
    
    label_nombre = tk.Label(ventana_emergente, text="Nombre_p:")#bg= color de fondo     fg= color de letra
    entry_nombre = tk.Entry(ventana_emergente)
    label_categoria = tk.Label(ventana_emergente, text="Categoria:")
    entry_categoria = tk.Entry(ventana_emergente)
    label_cantidad = tk.Label(ventana_emergente, text="Cantidad:")
    entry_cantidad = tk.Entry(ventana_emergente)
    label_precio = tk.Label(ventana_emergente, text="Precio de compra:")
    entry_precio = tk.Entry(ventana_emergente)
    button_agregar = tk.Button(ventana_emergente, text="Guardar", command = lambda :[agregar_producto(entry_nombre, entry_categoria, entry_cantidad, entry_precio), limpiar_campos(entry_nombre, entry_categoria, entry_cantidad, entry_precio)])
    boton_regresar = tk.Button(ventana_emergente, text="Finalizar", command= lambda: close_modal_new_product(ventana_emergente))
    
    entry_nombre.focus_set()
    #Establecemos la posicion de cada componente de la ventana
    label_nombre.grid(row=0, column=0)
    entry_nombre.grid(row=0, column=1)
    label_categoria.grid(row=1, column=0)
    entry_categoria.grid(row=1, column=1)
    label_cantidad.grid(row=2, column=0)
    entry_cantidad.grid(row=2, column=1)
    label_precio.grid(row=3, column=0)
    entry_precio.grid(row=3, column=1)
    button_agregar.grid(row=6, column=0)
    boton_regresar.grid(row=6, column=1)




def listado_productos_agregar():
    # Obtener los datos de la tabla
    query = "SELECT nombre_producto FROM producto WHERE estado = 'Disponible'"
    cursor.execute(query)
    datos = cursor.fetchall()

    var_seleccion = StringVar()

    lista_de_productos = OptionMenu(ventana_facturas, var_seleccion, datos[0], *datos[1:])
    # lista_de_productos.pack()
    lista_de_productos.grid(row=0, column=1)


def lista_detalles_en_facturas():
    print("mostrando detalles de factura.....")

def ventana_facturas():
    deshabilitar_botones()
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

    boton_finalizar = tk.Button(ventana_facturas, text="Finalizar", command= lambda: [boton_finalizar_factura(ventana_facturas), actualizar_productos(tabla_productos)])
    boton_finalizar.grid(row=6, column=1)
    actualizar_productos_facturas(detalles_de_factura)
    
    


def close_modal_new_product(ventana_emergente : tk.Toplevel):
    ventana_emergente.destroy()
    actualizar_productos(tabla_productos)
    habilitar_botones()

def boton_finalizar_factura(ventana_emergente : tk.Toplevel):
    ventana_emergente.destroy()
    actualizar_productos(tabla_productos)
    habilitar_botones()
    activar_factura()

def eliminar_producto():
    seleccionado = tabla_productos.selection() # Obtener el producto seleccionado de la tabla
    if seleccionado:
        nombre_producto = tabla_productos.item(seleccionado)['values'][1] 
    mensaje = f"Deseas eliminar el producto {nombre_producto} "
    respuesta = messagebox.askyesno("Eliminar producto", mensaje)
    if respuesta:
        print("respuesta si")
        print('registro eliminado...')
        if seleccionado:
            id_producto = tabla_productos.item(seleccionado)['values'][0] # Obtener el ID del producto a eliminar
            # Eliminar el producto de la base de datos
            cursor.execute("UPDATE producto SET estado='Eliminado' WHERE id=%s", (id_producto,))
            conexion.commit()
            # Actualizar la tabla de productos
            actualizar_productos(tabla_productos)
    else:
        print("respuesta no")
        return

def obtener_producto_por_id(id_producto):
    # Realizar consulta en la base de datos para obtener el producto con el ID proporcionado
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM producto WHERE id = %s", (id_producto,))
    producto = cursor.fetchone()  # Obtener el resultado de la consulta como una tupla
    cursor.close()  # Cerrar el cursor

    # Si se encontró un resultado, retornar los datos del producto en el formato adecuado
    if producto:
        # Desempaquetar los valores del resultado de la consulta en variables individuales
        id_producto, nombre_producto, categoria_producto, precio_compra, cantidad, precio_venta, estado = producto
        # Retornar los datos del producto en forma de tupla o en el formato adecuado
        return (id_producto, nombre_producto, categoria_producto, precio_compra, cantidad, precio_venta, estado)
    else:
        return None  # Si no se encontró un resultado, retornar None o algún valor indicativo de que no se encontró el producto




def modificar_producto():
    seleccionado = tabla_productos.selection() # Obtener el producto seleccionado de la tabla
    if seleccionado:
        id_producto = tabla_productos.item(seleccionado)['values'][0] # Obtener el valor de la primera columna (ID)
        # Abrir la ventana de modificación del producto
        producto = obtener_producto_por_id(id_producto) # Obtener el producto de la base de datos por ID
        ventana_modificar(producto)

def ventana_modificar(producto):
    # Crear una nueva ventana
    ventana_actualizar_producto = tk.Toplevel(ventana_principal)
    ventana_actualizar_producto.title("Modificar Producto")

    # Crear los widgets del formulario de modificación
    label_nombre = tk.Label(ventana_actualizar_producto, text="Nombre del Producto")
    entry_nombre = tk.Entry(ventana_actualizar_producto)
    entry_nombre.insert(tk.END, producto[1]) # Mostrar el nombre del producto en el campo de entrada
    label_categoria = tk.Label(ventana_actualizar_producto, text="Categoría del Producto")
    entry_categoria = tk.Entry(ventana_actualizar_producto)
    entry_categoria.insert(tk.END, producto[2]) # Mostrar la categoría del producto en el campo de entrada
    label_precio_compra = tk.Label(ventana_actualizar_producto, text="Precio de Compra")
    entry_precio_compra = tk.Entry(ventana_actualizar_producto)
    entry_precio_compra.insert(tk.END, producto[3]) # Mostrar el precio de compra del producto en el campo de entrada
    label_cantidad = tk.Label(ventana_actualizar_producto, text="Cantidad")
    entry_cantidad = tk.Entry(ventana_actualizar_producto)
    entry_cantidad.insert(tk.END, producto[4]) # Mostrar la cantidad del producto en el campo de entrada
    label_estado = tk.Label(ventana_actualizar_producto, text="Estado")
    entry_estado = tk.Entry(ventana_actualizar_producto)
    entry_estado.insert(tk.END, producto[6]) # Mostrar el estado del producto en el campo de entrada


    # Crear el botón de guardar
    button_guardar = tk.Button(ventana_actualizar_producto, text="Guardar", command=lambda: guardar_modificaciones(ventana_actualizar_producto ,producto[0], entry_nombre.get(), entry_categoria.get(), entry_precio_compra.get(), entry_cantidad.get(), entry_estado.get()))

    # Ubicar los widgets en la ventana_actualizar_producto
    label_nombre.grid(row=0, column=0, padx=10, pady=5)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)
    label_categoria.grid(row=1, column=0, padx=10, pady=5)
    entry_categoria.grid(row=1, column=1, padx=10, pady=5)
    label_precio_compra.grid(row=2, column=0, padx=10, pady=5)
    entry_precio_compra.grid(row=2, column=1, padx=10, pady=5)
    label_cantidad.grid(row=3, column=0, padx=10, pady=5)
    entry_cantidad.grid(row=3, column=1, padx=10, pady=5)
    label_estado.grid(row=5, column=0, padx=10, pady=5)
    entry_estado.grid(row=5, column=1, padx=10, pady=5)
    button_guardar.grid(row=6, column=0, columnspan=2, padx=10, pady=5)


def guardar_modificaciones(ventana_actualizar_producto, id_producto, nombre_producto, categoria_producto, precio_compra, cantidad, estado):
    precio_compra = Decimal(precio_compra)
    precio_venta = precio_compra * Decimal(1.2)
    # Actualizar los datos del producto en la base de datos
    update = f"UPDATE producto SET nombre_producto = '{nombre_producto}', cate_produc ={categoria_producto}, precio_compra = {precio_compra}, cantidad = {cantidad}, precio_venta = {precio_venta}, estado = '{estado}' WHERE id = {id_producto}"
    cursor.execute(update)
    conexion.commit()

    # Mostrar mensaje de éxito
    messagebox.showinfo("Éxito", "Producto actualizado exitosamente.")

    # Cerrar la ventana_actualizar_producto de modificación
    ventana_actualizar_producto.destroy()

    # Actualizar la tabla de productos en la ventana principal
    actualizar_productos(tabla_productos)

def seleccion_producto(event, botones):
    print("Función seleccion_producto() ejecutada") # Agregar esta línea de prueba
    seleccionado = tabla_productos.selection()
    if seleccionado:
        botones["actualizar"].configure(state=tk.NORMAL)
        botones["eliminar"].configure(state=tk.NORMAL)
    else:
        botones["actualizar"].configure(state=tk.DISABLED)
        botones["eliminar"].configure(state=tk.DISABLED)


def cerrar_aplicacion():
    print("cerrando ventana principal....")
    conexion.close()
    ventana_principal.destroy()


# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Inventario number 2")


# Crear los widgets de la GUI
botones = {
    "eliminar": tk.Button(ventana_principal, text="Eliminar", command=eliminar_producto, state=tk.DISABLED),
    "facturas": tk.Button(ventana_principal, text="Facturas", command=ventana_facturas),
    "nuevo": tk.Button(ventana_principal, text="Nuevo", command=ventana_nuevo),
    "Reporte": tk.Button(ventana_principal, text="Reporte", command= lambda : ventas_por_mes()),
    "actualizar": tk.Button(ventana_principal, text="Actualizar", command=modificar_producto, state=tk.DISABLED)
}
tabla_productos = ttk.Treeview(ventana_principal)
tabla_productos['columns'] = ("ID", "Producto", "Categoría", "Precio Compra", "Cantidad", "Precio Venta", "Estado") # Definir las columnas

# Definir encabezados de columna
tabla_productos.heading("#0", text="", anchor="w")
tabla_productos.heading("ID", text="ID", anchor="w")
tabla_productos.heading("Producto", text="Producto", anchor="w")
tabla_productos.heading("Categoría", text="Categoría", anchor="w")
tabla_productos.heading("Precio Compra", text="Precio Compra", anchor="w")
tabla_productos.heading("Cantidad", text="Cantidad", anchor="w")
tabla_productos.heading("Precio Venta", text="Precio Venta", anchor="w")
tabla_productos.heading("Estado", text="Estado", anchor="w")

# Definir el ancho de las columnas
tabla_productos.column("#0", width=0, stretch=tk.NO)
tabla_productos.column("ID", width=50, anchor="w")
tabla_productos.column("Producto", width=200, anchor="w")
tabla_productos.column("Categoría", width=150, anchor="w")
tabla_productos.column("Precio Compra", width=100, anchor="w")
tabla_productos.column("Cantidad", width=100, anchor="w")
tabla_productos.column("Precio Venta", width=100, anchor="w")
tabla_productos.column("Estado", width=100, anchor="w")


button_nuevo = botones["nuevo"]
button_actualizar = botones["actualizar"]
button_facturas = botones["facturas"]
button_eliminar = botones["eliminar"]
botton_reporte = botones["Reporte"]

# Ubicar los widgets en la ventana_principal
button_nuevo.grid(row=6, column=0)
button_facturas.grid(row=6, column=1)
button_actualizar.grid(row=6, column=2)
button_eliminar.grid(row=6, column=3)
botton_reporte.grid(row=6, column=4)
tabla_productos.grid(row=8, column=0, columnspan=5, sticky="nsew") # Ubicar el Treeview en la ventana

tabla_productos.bind("<<TreeviewSelect>>", lambda event: seleccion_producto(event, botones))  # Modificar el evento a <<TreeviewSelect>>

# Actualizar la lista de productos al inicio de la aplicación
actualizar_productos(tabla_productos)
seleccion_producto(None, botones)  # Llamar a la función seleccion_producto() con None como argumento



# Agregar el protocolo para cerrar la aplicación al hacer clic en la X
ventana_principal.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)

# Ejecutar la aplicación
ventana_principal.mainloop()