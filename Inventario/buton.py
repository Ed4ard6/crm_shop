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
    # datos = ( id_factura, id_producto, cantidad, precio_venta, total)
    # insert = "INSERT INTO det_factura (id_factura, id_producto, cantidad, precio_venta, total) VALUES (%s, %s, %s, %s, %s)"
    # cursor.execute(insert, datos)
    # conexion.commit()

def precio_producto(id_producto):
    dato = id_producto
    consulta = f"SELECT precio_venta FROM producto WHERE id = {dato}"
    cursor.execute(consulta)
    precio_de_venta = cursor.fetchone()
    if precio_de_venta is not None:
        return precio_de_venta[0]


def ultima_factura():
    consulta= "SELECT id FROM facturas ORDER by id DESC LIMIT 1"
    cursor.execute(consulta)
    resultado = cursor.fetchone()
    # conexion.close()
    if resultado is not None:
        return resultado[0]
    conexion.commit()

def actualizar_productos(lista_productos):
    cursor.execute("SELECT * FROM producto")
    resultados = cursor.fetchall()
    lista_productos.delete(0, tk.END)
    for producto in resultados:
        precio_venta = producto[4] * 1.2
        lista_productos.insert(tk.END, f"ID: {producto[0]}, Producto: {producto[1]} -- Categoria: {producto[2]} -- precio_compra: {producto[3]:.2f} -- cantidad: {producto[4]} -- precio_venta: {producto[5]} -- estado: {producto[6]}")


def deshabilitar_botones():
    for boton in botones.values():
        boton.configure(state="disabled")

def habilitar_botones():
    for boton in botones.values():
        boton.configure(state="normal")


def ventana_facturas():
    deshabilitar_botones()
    # lista_productos()
    #Obtener los datos de la tabla producto
    query = "SELECT nombre_producto, id FROM producto"
    cursor.execute(query)
    datos = cursor.fetchall()
    diccionario = dict((nombre, id) for nombre, id in datos)
    var_seleccion = StringVar()

    ventana_emergente = tk.Toplevel(ventana_principal)
    ventana_emergente.title("Registrar Factura")
    ventana_emergente.geometry("300x350")
    #crear_factura()

    lista_de_productos = OptionMenu(ventana_emergente, var_seleccion, *diccionario.keys())
    label_producto = tk.Label(ventana_emergente, text="Producto:")
    label_cantidad = tk.Label(ventana_emergente, text="Cantidad:")
    entry_cantidad = tk.Entry(ventana_emergente)
    
    button_agregar = tk.Button(ventana_emergente, text="Guardar", command=lambda: [agregar_detalles_factura(var_seleccion, entry_cantidad, diccionario), limpiar_formulario_detalles_fatura(var_seleccion, entry_cantidad)])


    #Establecemos la posicion de cada componente de la ventana
    label_producto.grid(row=0, column=0)
    lista_de_productos.grid(row=0, column=1)
    label_cantidad.grid(row=1, column=0)
    entry_cantidad.grid(row=1, column=1)
    
    button_agregar.grid(row=6, column=0)

    boton_regresar = tk.Button(ventana_emergente, text="Finalizar", command= lambda: close_modal_new_product(ventana_emergente))
    boton_regresar.grid(row=6, column=1)


def close_modal_new_product(ventana_emergente : tk.Toplevel):
    ventana_emergente.destroy()
    actualizar_productos(lista_productos)
    habilitar_botones()

def limpiar_formulario_detalles_fatura(var_seleccion, entry_cantidad):
    var_seleccion.set("")  # limpia la opción seleccionada en la lista de productos
    entry_cantidad.delete(0, tk.END)  # limpia el campo de entrada de cantidad


# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Inventario number 2")


app.mainloop()


# Ejecutar la aplicación
ventana_principal.mainloop()