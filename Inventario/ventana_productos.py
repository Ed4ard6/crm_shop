import tkinter as tk
from tkinter import *
from funciones_ventana_productos import limpiar_campos, agregar_producto,verificacion_de_estados_cantidad
from conexion_2 import conexion, cursor
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from decimal import Decimal 

def close_modal_new_product(ventana_emergente : tk.Toplevel, button_nuevo, tabla_productos):
    ventana_emergente.destroy()
    verificacion_de_estados_cantidad(tabla_productos)
    habilitar_botones(button_nuevo)

def deshabilitar_botones(button_nuevo):
    button_nuevo.configure(state="disabled")

def habilitar_botones(button_nuevo):

    button_nuevo.configure(state="normal")
    # for boton in botones.values():
    #     boton.configure(state="normal")

def ventana_nuevo(ventana_inventario, button_nuevo, tabla_productos):
    deshabilitar_botones(button_nuevo)
    ventana_emergente = tk.Toplevel(ventana_inventario)
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
    button_agregar = tk.Button(ventana_emergente, text="Guardar", command = lambda :[agregar_producto(ventana_emergente, entry_nombre, entry_categoria, entry_cantidad, entry_precio), limpiar_campos(entry_nombre, entry_categoria, entry_cantidad, entry_precio)])
    boton_regresar = tk.Button(ventana_emergente, text="Finalizar", command= lambda: close_modal_new_product(ventana_emergente, button_nuevo, tabla_productos))
    
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

def eliminar_producto(tabla_productos):
    seleccionado = tabla_productos.selection() # Obtener el producto seleccionado de la tabla
    if seleccionado:
        nombre_producto = tabla_productos.item(seleccionado)['values'][1] 
    mensaje = f"Deseas eliminar el producto {nombre_producto} "
    respuesta = messagebox.askyesno("Eliminar producto", mensaje)
    if respuesta:
        if seleccionado:
            id_producto = tabla_productos.item(seleccionado)['values'][0] # Obtener el ID del producto a eliminar
            # Eliminar el producto de la base de datos
            cursor.execute("UPDATE producto SET estado='Eliminado' WHERE id=%s", (id_producto,))
            conexion.commit()
            # Actualizar la tabla de productos
            verificacion_de_estados_cantidad(tabla_productos)
    else:
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




def modificar_producto(tabla_productos, ventana_inventario, button_nuevo ):
    seleccionado = tabla_productos.selection() # Obtener el producto seleccionado de la tabla
    if seleccionado:
        id_producto = tabla_productos.item(seleccionado)['values'][0] # Obtener el valor de la primera columna (ID)
        # Abrir la ventana de modificación del producto
        producto = obtener_producto_por_id(id_producto) # Obtener el producto de la base de datos por ID
        ventana_modificar(tabla_productos, producto, ventana_inventario, button_nuevo)

def ventana_modificar(tabla_productos, producto, ventana_inventario, button_nuevo):
    # Crear una nueva ventana
    ventana_actualizar_producto = tk.Toplevel(ventana_inventario)
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
    button_guardar = tk.Button(ventana_actualizar_producto, text="Guardar", command=lambda: guardar_modificaciones(ventana_inventario, ventana_actualizar_producto, tabla_productos, producto[0], entry_nombre.get(), entry_categoria.get(), entry_precio_compra.get(), entry_cantidad.get(), entry_estado.get(), cursor, button_nuevo))


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



def guardar_modificaciones(ventana_inventario, ventana_actualizar_producto, tabla_productos, id_producto, nombre_producto, categoria_producto, precio_compra, cantidad, estado, cursor, button_nuevo):
    precio_compra = Decimal(precio_compra)
    precio_venta = precio_compra * Decimal(1.2)
    # Actualizar los datos del producto en la base de datos
    update = "UPDATE producto SET nombre_producto = %s, cate_produc = %s, precio_compra = %s, cantidad = %s, precio_venta = %s, estado = %s WHERE id = %s"
    cursor.execute(update, (nombre_producto, categoria_producto, precio_compra, cantidad, precio_venta, estado, id_producto))
    conexion.commit()

    # Cerrar la ventana_actualizar_producto de modificación
    ventana_actualizar_producto.destroy()

    # Mostrar mensaje de éxito
    messagebox.showinfo("Éxito", "Producto actualizado exitosamente.")

    # Actualizar la tabla de productos
    verificacion_de_estados_cantidad(tabla_productos)
    ventana_inventario.focus_set()

def seleccion_producto(tabla_productos,event ,botones ):
    seleccionado = tabla_productos.selection()
    if seleccionado:
        botones["actualizar"].configure(state=tk.NORMAL)
        botones["eliminar"].configure(state=tk.NORMAL)
    else:
        botones["actualizar"].configure(state=tk.DISABLED)
        botones["eliminar"].configure(state=tk.DISABLED)


def cerrar_ventana_inventario(ventana_inventario):
    ventana_inventario.destroy()

    

def abrir_ventana_principal(ventana_principal):
    # ventana_principal.deiconify()  # Mostrar ventana principal
    ventana_principal.state("zoomed")


def productos(ventana_principal):
        # Crear la ventana principal
    ventana_inventario = tk.Tk()
    ventana_inventario.title("Inventario number 2")

    ventana_inventario.state("zoomed")# Abre la ventana maximizada

    # Crear los widgets de la GUI
    botones = {
        "eliminar": tk.Button(ventana_inventario, text="Eliminar", width=65, bg="#ff6c3e", command= lambda : eliminar_producto( tabla_productos), state=tk.DISABLED),
        "nuevo": tk.Button(ventana_inventario, text="Nuevo",bg="#5ccb5f" , command= lambda : ventana_nuevo(ventana_inventario, button_nuevo, tabla_productos)),
        "actualizar": tk.Button(ventana_inventario, text="Actualizar", width=65, bg="#ffff00", command=lambda: modificar_producto(tabla_productos, ventana_inventario, button_nuevo ), state=tk.DISABLED)
    }
    tabla_productos = ttk.Treeview(ventana_inventario)
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
    tabla_productos.column("Estado", width=50, anchor="w")


    button_nuevo = botones["nuevo"]
    button_actualizar = botones["actualizar"]
    button_eliminar = botones["eliminar"]

   # Ubicar los widgets en la ventana_inventario
    button_nuevo.grid(row=6, column=0, sticky="nsew", padx=5, pady=5)
    button_actualizar.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)
    button_eliminar.grid(row=6, column=2, sticky="nsew", padx=5, pady=5)
    tabla_productos.grid(row=8, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)
    ventana_inventario.grid_rowconfigure(8, weight=1)
    ventana_inventario.grid_columnconfigure(0, weight=1)


    tabla_productos.bind("<<TreeviewSelect>>", lambda event, tabla=tabla_productos, botones=botones: seleccion_producto(tabla, event, botones))  # Modificar el evento a <<TreeviewSelect>>

    # Actualizar la lista de productos al inicio de la aplicación
    verificacion_de_estados_cantidad(tabla_productos)
    seleccion_producto(tabla_productos ,None, botones)  # Llamar a la función seleccion_producto() con None como argumento

    ventana_principal.withdraw()# Ocultar ventana principal

    ventana_inventario.protocol("WM_DELETE_WINDOW", lambda: [abrir_ventana_principal(ventana_principal), cerrar_ventana_inventario(ventana_inventario)])

    # Ejecutar la aplicación
    ventana_inventario.mainloop()