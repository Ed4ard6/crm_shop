import tkinter as tk
from conexion_2 import conexion, cursor
import datetime

def limpiar_formulario_detalles_fatura(var_seleccion, entry_cantidad):
    var_seleccion.set("")  # limpia la opción seleccionada en la lista de productos
    entry_cantidad.delete(0, tk.END)  # limpia el campo de entrada de cantidad

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

def precio_producto(id_producto):
    dato = id_producto
    consulta = f"SELECT precio_venta FROM producto WHERE id = {dato}"
    cursor.execute(consulta)
    precio_de_venta = cursor.fetchone()
    if precio_de_venta is not None:
        return precio_de_venta[0]

    
agregar_detalles_factura
#creamos la factura
def crear_factura():
    #Aqui sabemos las fecha de hoy para guardarlo en la factura
    fecha_hoy = datetime.date.today()
    estado = "Sin finalizar"
    total = 0
    datos = (fecha_hoy, estado, total)
    insert= "INSERT INTO facturas (fecha, estado, total) VALUES (%s, %s, %s)"
    cursor.execute(insert, datos)
    conexion.commit()

def total_factura():
    id = ultima_factura()
    datos =(id,)
    consulta= "SELECT SUM(total) FROM det_factura WHERE id_factura = %s"
    cursor.execute(consulta, datos)
    total_factura = cursor.fetchone()
    # conexion.close()
    if total_factura is not None:
        return total_factura[0]
    conexion.commit()

def activar_factura():
    id_factura = ultima_factura()
    estado = "Activa"
    total = total_factura()
    datos = (estado, total, id_factura)
    update = "UPDATE facturas SET estado = %s, total = %s WHERE id = %s;"
    cursor.execute(update, datos)
    conexion.commit()
    print("Factura Actualizada")



def ultima_factura():
    consulta= "SELECT id FROM facturas ORDER by id DESC LIMIT 1"
    cursor.execute(consulta)
    resultado = cursor.fetchone()
    # conexion.close()
    if resultado is not None:
        return resultado[0]
    conexion.commit()

def agregar_producto(entry_nombre : tk.Entry, entry_categoria : tk.Entry,entry_cantidad : tk.Entry, entry_precio : tk.Entry):

    nombre_producto = entry_nombre.get()
    cate_produc = entry_categoria.get()
    cantidad = int(entry_cantidad.get())
    precio_compra = float(entry_precio.get())
    estado = "Disponible"
    precio_venta = precio_compra * 1.2  
    datos = (nombre_producto, cate_produc, precio_compra, cantidad, precio_venta, estado)
    consulta = "INSERT INTO producto (nombre_producto, cate_produc, precio_compra, cantidad, 	precio_venta, estado) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(consulta, datos)
    conexion.commit()
    limpiar_campos()
    actualizar_productos()


def limpiar_campos(entry_nombre : tk.Entry, entry_categoria : tk.Entry,entry_cantidad : tk.Entry, entry_precio : tk.Entry, 
                   label_categoria : tk.Label,label_nombre : tk.Label,label_cantidad : tk.Label ,label_precio : tk.Label, 
                   button_agregar: tk.Button, button_cancelar: tk.Button, button_nuevo: tk.Button, button_actualizar: tk.Button, 
                   button_eliminar: tk.Button):
    
    entry_nombre.configure(state=tk.DISABLED)
    entry_categoria.configure(state=tk.DISABLED)
    entry_cantidad.configure(state=tk.DISABLED)
    entry_precio.configure(state=tk.DISABLED)

    label_nombre.configure(state=tk.DISABLED)
    label_categoria.configure(state=tk.DISABLED)
    label_cantidad.configure(state=tk.DISABLED)
    label_precio.configure(state=tk.DISABLED)

    button_agregar.configure(state=tk.DISABLED)
    button_cancelar.configure(state=tk.DISABLED)

    # habilita los botones de nuevo, Actualizar, Eliminar
    button_nuevo.configure(state=tk.NORMAL)
    button_actualizar.configure(state=tk.NORMAL)
    button_eliminar.configure(state=tk.NORMAL)

def actualizar_productos(lista_productos):
    cursor.execute("SELECT * FROM producto")
    resultados = cursor.fetchall()
    lista_productos.delete(0, tk.END)
    for producto in resultados:
        precio_venta = producto[4] * 1.2
        lista_productos.insert(tk.END, f"ID: {producto[0]}, Producto: {producto[1]} -- Categoria: {producto[2]} -- precio_compra: {producto[3]:.2f} -- cantidad: {producto[4]} -- precio_venta: {producto[5]} -- estado: {producto[6]}")
