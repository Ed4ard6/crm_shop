import tkinter as tk
from tkinter import *
from funciones import actualizar_productos, limpiar_campos, agregar_producto, crear_factura, agregar_detalles_factura, limpiar_formulario_detalles_fatura, activar_factura
from conexion_2 import conexion, cursor



def deshabilitar_botones():
    for boton in botones.values():
        boton.configure(state="disabled")

def habilitar_botones():
    for boton in botones.values():
        boton.configure(state="normal")


def ventana_nuevo():
    deshabilitar_botones()
    print("ventana_nuevo....")
    ventana_emergente = tk.Toplevel(ventana_principal)
    ventana_emergente.title("Registrar nuevo producto")
    ventana_emergente.geometry("300x350")

    label_nombre = tk.Label(ventana_emergente, text="Nombre_p:")#bg= color de fondo     fg= color de letra
    entry_nombre = tk.Entry(ventana_emergente)
    label_categoria = tk.Label(ventana_emergente, text="Categoria:")
    entry_categoria = tk.Entry(ventana_emergente)
    label_cantidad = tk.Label(ventana_emergente, text="Cantidad:")
    entry_cantidad = tk.Entry(ventana_emergente)
    label_precio = tk.Label(ventana_emergente, text="Precio de compra:")
    entry_precio = tk.Entry(ventana_emergente)
    button_agregar = tk.Button(ventana_emergente, text="Guardar", command = lambda :agregar_producto(entry_nombre, entry_categoria, entry_cantidad, entry_precio))
    boton_regresar = tk.Button(ventana_emergente, text="Finalizar", command= lambda: close_modal_new_product(ventana_emergente))
    
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

def lista_productos():
    # Obtener los datos de la tabla
    query = "SELECT nombre_producto FROM producto"
    cursor.execute(query)
    datos = cursor.fetchall()

    var_seleccion = StringVar()

    lista_de_productos = OptionMenu(ventana_facturas, var_seleccion, datos[0], *datos[1:])
    # lista_de_productos.pack()
    lista_de_productos.grid(row=0, column=1)

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
    crear_factura()

    lista_de_productos = OptionMenu(ventana_emergente, var_seleccion, *diccionario.keys())
    label_producto = tk.Label(ventana_emergente, text="Producto:")
    label_cantidad = tk.Label(ventana_emergente, text="Cantidad:")
    entry_cantidad = tk.Entry(ventana_emergente)
    
    button_agregar = tk.Button(ventana_emergente, text="Agregar", command=lambda: [agregar_detalles_factura(var_seleccion, entry_cantidad, diccionario), limpiar_formulario_detalles_fatura(var_seleccion, entry_cantidad)])

    #Establecemos la posicion de cada componente de la ventana
    label_producto.grid(row=0, column=0)
    lista_de_productos.grid(row=0, column=1)
    label_cantidad.grid(row=1, column=0)
    entry_cantidad.grid(row=1, column=1)
    
    button_agregar.grid(row=6, column=0)

    boton_finalizar = tk.Button(ventana_emergente, text="Finalizar", command= lambda: boton_finalizar_factura(ventana_emergente))
    boton_finalizar.grid(row=6, column=1)


def close_modal_new_product(ventana_emergente : tk.Toplevel):
    ventana_emergente.destroy()
    actualizar_productos(lista_productos)
    habilitar_botones()

def boton_finalizar_factura(ventana_emergente : tk.Toplevel):
    ventana_emergente.destroy()
    actualizar_productos(lista_productos)
    habilitar_botones()
    activar_factura()

def agregar_limpiar():
    agregar_producto()
    limpiar_campos()

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Inventario number 2")


# Crear los widgets de la GUI
botones = {
    "eliminar": tk.Button(ventana_principal, text="Eliminar", command=""),
    "facturas": tk.Button(ventana_principal, text="Facturas", command=ventana_facturas),
    "nuevo": tk.Button(ventana_principal, text="Nuevo", command=ventana_nuevo),
    "actualizar": tk.Button(ventana_principal, text="Actualizar", command="")
}

button_nuevo = botones["nuevo"]
button_actualizar = botones["actualizar"]
button_facturas = botones["facturas"]
button_eliminar = botones["eliminar"]
lista_productos = tk.Listbox(ventana_principal, height=10, width=120)

# Ubicar los widgets en la ventana_principal
button_nuevo.grid(row=6, column=0)
button_facturas.grid(row=6, column=1)
button_actualizar.grid(row=6, column=2)
button_eliminar.grid(row=6, column=3)#, columnspan=2-- Esto es para dejar uin esacio para ubicar mejor los botones
lista_productos.grid(row=8, column=0, columnspan=4)

# Actualizar la lista de productos al inicio de la aplicación
actualizar_productos(lista_productos)

# Ejecutar la aplicación
ventana_principal.mainloop()