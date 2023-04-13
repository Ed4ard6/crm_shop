import tkinter as tk
from tkinter import messagebox
from conexion_2 import conexion, cursor

def actualizar_productos(tabla_productos):
    cursor.execute("SELECT * FROM producto")
    resultados = cursor.fetchall()
    tabla_productos.delete(*tabla_productos.get_children()) # Eliminar los elementos actuales del Treeview
    for producto in resultados:
        tabla_productos.insert("", tk.END, values=(producto[0], producto[1], producto[2], producto[3], producto[4], producto[5], producto[6]))

def limpiar_campos(entry_nombre, entry_categoria, entry_cantidad, entry_precio):
    entry_nombre.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_nombre.focus_set()  # Ubicar cursor en el primer campo de entrada

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