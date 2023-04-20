import tkinter as tk
from tkinter import messagebox
from conexion_2 import conexion, cursor
import datetime

def validacion_cantidad_productos(var_seleccion, entry_cantidad, diccionario, tabla_detalles, label_total):
    cantidad = entry_cantidad.get()  # Obtener la cantidad ingresada en el entry
    if len(cantidad) == 0 or int(cantidad) == 0:  # Modificar la condición para incluir si la cantidad es igual a cero
        messagebox.showerror("Error", "Tiene que establecer una cantidad válida del producto a agregar")
        entry_cantidad.focus_set()
    else:
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
        if cantidad_producto_en_factura != 0:
            mensaje = f"El producto {nombre_producto} ya está registrado en esta factura con cantidad {cantidad_producto_en_factura}. ¿Desea agregarlo nuevamente?"
            respuesta = messagebox.askyesno("Producto ya registrado", mensaje)
            if respuesta: 
                cantidad_ingresada += cantidad_producto_en_factura
                actualizar_cantidad(cantidad_ingresada, id_producto)
                limpiar_formulario_detalles_fatura(var_seleccion, entry_cantidad)
                actualizar_productos_facturas(tabla_detalles, label_total) 
                entry_cantidad.focus_set()
            else:
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
                    actualizar_productos_facturas(tabla_detalles, label_total) 
                else:
                    messagebox.showerror("Error", f"Para {nombre_producto} solo tenemos {cantidad_disponible} unidades disponibles")
                    entry_cantidad.focus_set()
            else:
                messagebox.showerror("Error", f"No tenemos disponibilidad para {nombre_producto} ")
                entry_cantidad.focus_set()

def actualizar_productos_facturas(tabla_detalles, label_total):
    id_factura = ultima_factura()
    query = f"SELECT producto.nombre_producto, det_factura.cantidad, producto.precio_venta, det_factura.total FROM det_factura JOIN producto ON det_factura.id_producto = producto.id WHERE det_factura.id_factura = {id_factura};"
    cursor.execute(query)
    resultados = cursor.fetchall()
    tabla_detalles.delete(*tabla_detalles.get_children())
    total_pagar = 0  # Inicializar la suma total en 0
    for producto in resultados:
        precio_producto = producto[2]  # Obtener el precio del producto
        total_producto = producto[3]  # Obtener el total del producto
        total_pagar += total_producto  # Sumar el total del producto al total a pagar
        precio_producto_formatted = '{:,}'.format(precio_producto)  # Formatear el precio del producto con separadores de miles
        total_producto_formatted = '{:,}'.format(total_producto)  # Formatear el total del producto con separadores de miles
        tabla_detalles.insert("", tk.END, values=(producto[0], producto[1], precio_producto_formatted, total_producto_formatted))  # Insertar el producto en la tabla con el precio y total formateados
    total_pagar_formatted = '{:,}'.format(total_pagar)  # Formatear el total a pagar con separadores de miles
    label_total.config(text=f"Total a pagar: ${total_pagar_formatted}")  # Actualizar el texto de la etiqueta con el total a pagar formateado

def activar_factura():
    id_factura = ultima_factura()
    estado = "Activa"
    total = total_factura()
    datos = (estado, total, id_factura)
    update = "UPDATE facturas SET estado = %s, total = %s WHERE id = %s;"
    cursor.execute(update, datos)
    conexion.commit()
    actualizar_cantidad_disponible(id_factura)

def ultima_factura():
    consulta= "SELECT id FROM facturas ORDER by id DESC LIMIT 1"
    cursor.execute(consulta)
    resultado = cursor.fetchone()
    # conexion.close()
    if resultado is not None:
        return resultado[0]

def cancelar_factura():
    id_factura = ultima_factura()
    estado = "Cancelada"
    datos = (estado, id_factura)
    update = "UPDATE facturas SET estado = %s WHERE id = %s;"
    cursor.execute(update, datos)
    conexion.commit()
    actualizar_cantidad_disponible(id_factura)

def crear_factura():
    #Aqui sabemos las fecha de hoy para guardarlo en la factura
    fecha_hoy = datetime.date.today()
    estado = "Sin finalizar"
    total = 0
    datos = (fecha_hoy, estado, total)
    insert= "INSERT INTO facturas (fecha, estado, total) VALUES (%s, %s, %s)"
    cursor.execute(insert, datos)
    conexion.commit()

def actualizar_cantidad(cantidad_ingresada, id_producto):
    id_factura = ultima_factura()
    precio_venta = precio_producto(id_producto)
    total = precio_venta * cantidad_ingresada
    query = f"UPDATE det_factura SET cantidad = {cantidad_ingresada}, total = {total} WHERE id_producto = {id_producto} AND id_factura = {id_factura};"
    cursor.execute(query)
    conexion.commit()

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
    datos = ( id_factura, id_producto, cantidad, precio_venta, total)
    insert = "INSERT INTO det_factura (id_factura, id_producto, cantidad, precio_venta, total) VALUES (%s, %s, %s, %s, %s)"
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

        # Verificar si la cantidad disponible es igual a 0 y actualizar el estado del producto
        query = f"SELECT cantidad FROM producto WHERE id = {id_producto};"
        cursor.execute(query)
        cantidad_disponible = cursor.fetchone()[0]
        if cantidad_disponible == 0:
            query = f"UPDATE producto SET estado = 'Agotado' WHERE id = {id_producto};"
            cursor.execute(query)

    conexion.commit()

def precio_producto(id_producto):
    dato = id_producto
    consulta = f"SELECT precio_venta FROM producto WHERE id = {dato}"
    cursor.execute(consulta)
    precio_de_venta = cursor.fetchone()
    if precio_de_venta is not None:
        return precio_de_venta[0]