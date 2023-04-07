import tkinter as tk
from conexion_2 import conexion, cursor


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
        lista_productos.insert(tk.END, f"ID: {producto[0]}, Nombre_producto: {producto[1]} -- cate_produc: {producto[2]} -- precio_compra: {producto[3]:.2f} -- cantidad: {producto[4]} -- precio_venta: {producto[5]} -- estado: {producto[6]}")
