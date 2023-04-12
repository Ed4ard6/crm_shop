import tkinter as tk
from tkinter import *
import mysql.connector

# Conectar a la base de datos
conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="inventario"
)

cursor = conexion.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS `inventario` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;")
cursor.execute("USE `inventario`;")

def agregar_detalles_factura(var_seleccion, entry_cantidad, diccionario):
    id_factura = ultima_factura()
    nombre_producto = var_seleccion.get()
    id_producto = diccionario[nombre_producto]
    cantidad = entry_cantidad.get()
    precio_venta = precio_producto(id_producto)
    total = precio_venta * int(cantidad)
    print(f'El precio de venta es: {precio_venta}---- Se agregaron {cantidad} unidades de {nombre_producto} (ID: {id_producto}) y el total es {total}')
    datos = ( id_factura, id_producto, cantidad, precio_venta, total)
    insert = "INSERT INTO det_factura (id_factura, id_producto, cantidad, precio_venta, total) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert, datos)
    conexion.commit()


def ventana_facturas():
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
    
    button_agregar = tk.Button(ventana_facturas, text="Agregar", command=lambda: [agregar_detalles_factura(var_seleccion, entry_cantidad, diccionario), limpiar_formulario_detalles_fatura(var_seleccion, entry_cantidad), actualizar_productos_facturas(detalles_de_factura)])

    #Establecemos la posicion de cada componente de la ventana
    label_producto.grid(row=0, column=0)
    lista_de_productos.grid(row=0, column=1)
    label_cantidad.grid(row=1, column=0)
    entry_cantidad.grid(row=1, column=1)
    lista_de_productos.focus_set()

    button_agregar.grid(row=6, column=0)

    boton_finalizar = tk.Button(ventana_facturas, text="Finalizar", command= lambda: boton_finalizar_factura(ventana_facturas))
    boton_finalizar.grid(row=6, column=1)
    actualizar_productos_facturas(detalles_de_factura)

def boton_finalizar_factura(ventana_emergente : tk.Toplevel):
    ventana_emergente.destroy()
    actualizar_productos(lista_productos)
    habilitar_botones()
    activar_factura()

def actualizar_productos_facturas(detalles_de_factura ):
    id_factura = ultima_factura()
    print(f"actualizando lista de facturas de la factura numero { id_factura} ....")
    query = f"SELECT det_factura.id_factura, producto.nombre_producto, det_factura.cantidad, producto.precio_venta, det_factura.total FROM det_factura JOIN producto ON det_factura.id_producto = producto.id WHERE det_factura.id_factura = {id_factura};"
    cursor.execute(query)
    resultados = cursor.fetchall()
    detalles_de_factura.delete(0, tk.END)
    for producto in resultados:
        detalles_de_factura.insert(tk.END, f"Factura: {producto[0]} -- Producto: {producto[1]} -- Cantidad: {producto[2]} -- Precio: {producto[3]} -- Total: {producto[4]}")
  