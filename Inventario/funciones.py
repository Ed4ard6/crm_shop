import tkinter as tk
from tkinter import messagebox
from conexion_2 import conexion, cursor
import datetime

def validacion_cantidad_productos(var_seleccion, entry_cantidad, diccionario, detalles_de_factura):
    id_factura = ultima_factura()
    nombre_producto = var_seleccion.get()
    cantidad_ingresada = int(entry_cantidad.get())
    id_producto = diccionario[nombre_producto]
    consulta = f"SELECT cantidad FROM det_factura WHERE id_producto = {id_producto} AND id_factura = {id_factura}"
    cursor.execute(consulta)
    resultado = cursor.fetchone()
    cantidad_producto_en_factura = 0  # Asignar un valor predeterminado
    if resultado is not None:
        cantidad_producto_en_factura = resultado[0]  # Asignar el valor del resultado de la consulta
        print(f"el valor de la consulta es {cantidad_producto_en_factura}")
    if cantidad_producto_en_factura != 0:
        mensaje = f"El producto {nombre_producto} ya está registrado en esta factura con cantidad {cantidad_producto_en_factura}. ¿Desea agregarlo nuevamente?"
        respuesta = messagebox.askyesno("Producto ya registrado", mensaje)
        if respuesta:
            print("respuesta si")
            cantidad_ingresada += cantidad_producto_en_factura
            actualizar_cantidad(cantidad_ingresada, id_producto)
            limpiar_formulario_detalles_fatura(var_seleccion, entry_cantidad)
            actualizar_productos_facturas(detalles_de_factura) 
            entry_cantidad.focus_set()
        else:
            print("respuesta no")
            entry_cantidad.focus_set()
            return
    
    else:
        query = f"SELECT cantidad FROM producto WHERE id = {id_producto};"
        cursor.execute(query)
        cantidad_disponible = cursor.fetchone()[0]

        if cantidad_disponible != 0:
            if cantidad_disponible >= cantidad_ingresada: 
                agregar_detalles_factura(var_seleccion, entry_cantidad, diccionario)
                limpiar_formulario_detalles_fatura(var_seleccion, entry_cantidad)
                actualizar_productos_facturas(detalles_de_factura) 
            else:
                messagebox.showerror("Error", f"Para {nombre_producto} solo tenemos {cantidad_disponible} unidades disponibles")
                entry_cantidad.focus_set()
        else:
            messagebox.showerror("Error", f"No tenemos disponibilidad para {nombre_producto} ")
            entry_cantidad.focus_set()



def limpiar_formulario_detalles_fatura(var_seleccion, entry_cantidad):
    var_seleccion.set("")  # limpia la opción seleccionada en la lista de productos
    entry_cantidad.delete(0, tk.END)  # limpia el campo de entrada de cantidad
    
def actualizar_cantidad(cantidad_ingresada, id_producto):
    id_factura = ultima_factura()
    precio_venta = precio_producto(id_producto)
    total = precio_venta * cantidad_ingresada
    query = f"UPDATE det_factura SET cantidad = {cantidad_ingresada}, total = {total} WHERE id_producto = {id_producto} AND id_factura = {id_factura};"
    cursor.execute(query)
    print("supuestamente alctualize la cantidad")
    conexion.commit()

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

    
#agregar_detalles_factura#creo que esta de mas
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
    
# Aqui buscamos el total de la ultima factura registrada
def total_factura():
    id = ultima_factura()
    datos =(id,)
    consulta= "SELECT SUM(total) FROM det_factura WHERE id_factura = %s"
    cursor.execute(consulta, datos)
    total_factura = cursor.fetchone()
    # conexion.close()
    if total_factura is not None:
        return total_factura[0]
    
def actualizar_cantidad_disponible(id_factura):
    # Obtener los datos de la tabla det_factura correspondientes a la factura en cuestión
    query = f"SELECT id_producto, cantidad FROM det_factura WHERE id_factura = {id_factura};"
    cursor.execute(query)
    detalles_factura = cursor.fetchall()

    # Actualizar la cantidad disponible de cada producto en la tabla producto
    for detalle in detalles_factura:
        id_producto = detalle[0]
        cantidad_vendida = detalle[1]
        query = f"UPDATE producto SET cantidad = cantidad - {cantidad_vendida} WHERE id = {id_producto};"
        cursor.execute(query)
    
    conexion.commit()
    print("Cantidades actulaizadas")


def activar_factura():
    id_factura = ultima_factura()
    estado = "Activa"
    total = total_factura()
    datos = (estado, total, id_factura)
    update = "UPDATE facturas SET estado = %s, total = %s WHERE id = %s;"
    cursor.execute(update, datos)
    conexion.commit()
    print("Factura Activa")
    actualizar_cantidad_disponible(id_factura)




def ultima_factura():
    consulta= "SELECT id FROM facturas ORDER by id DESC LIMIT 1"
    cursor.execute(consulta)
    resultado = cursor.fetchone()
    # conexion.close()
    if resultado is not None:
        return resultado[0]


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
    messagebox.showinfo("Registro exitoso", "Producto registrado correctamente")


def limpiar_campos(entry_nombre, entry_categoria, entry_cantidad, entry_precio):
    entry_nombre.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_nombre.focus_set()  # Ubicar cursor en el primer campo de entrada

def actualizar_productos(tabla_productos):
    cursor.execute("SELECT * FROM producto")
    resultados = cursor.fetchall()
    tabla_productos.delete(*tabla_productos.get_children()) # Eliminar los elementos actuales del Treeview
    for producto in resultados:
        tabla_productos.insert("", tk.END, values=(producto[0], producto[1], producto[2], producto[3], producto[4], producto[5], producto[6]))

def actualizar_productos_facturas(detalles_de_factura ):
    id_factura = ultima_factura()
    print(f"actualizando lista de facturas de la factura numero { id_factura} ....")
    query = f"SELECT det_factura.id_factura, producto.nombre_producto, det_factura.cantidad, producto.precio_venta, det_factura.total FROM det_factura JOIN producto ON det_factura.id_producto = producto.id WHERE det_factura.id_factura = {id_factura};"
    cursor.execute(query)
    resultados = cursor.fetchall()
    detalles_de_factura.delete(0, tk.END)
    for producto in resultados:
        detalles_de_factura.insert(tk.END, f"Factura: {producto[0]} -- Producto: {producto[1]} -- Cantidad: {producto[2]} -- Precio: {producto[3]} -- Total: {producto[4]}")
  