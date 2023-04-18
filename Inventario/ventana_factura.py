import tkinter as tk
from tkinter import *
from funciones_venta_factura import validacion_cantidad_productos, actualizar_productos_facturas, activar_factura, ultima_factura, cancelar_factura, crear_factura
from conexion_2 import conexion, cursor
from tkinter import messagebox
from tkinter import ttk



def boton_finalizar_factura(ventana_facturas: tk.Toplevel, ventana_principal):
    id_factura = ultima_factura()
    consulta = f"SELECT * FROM det_factura WHERE id_factura = {id_factura};"
    cursor.execute(consulta)
    resultado = cursor.fetchone()
    cursor.fetchall()  # Consumir todos los resultados antes de ejecutar otra consulta
    # conexion.close()

    if resultado is not None: # Si el resultado no es None
        activar_factura()
        cerrar_ventana_factura(ventana_facturas)
        messagebox.showinfo("Registro exitoso", "Factura registrada correctamente")
        abrir_ventana_principal(ventana_principal)
        return
    
    mensaje = "Para poder finalizar la factura debe tener al menos un producto agregado. ¿Desea cancelar la factura?"
    respuesta = messagebox.askyesno("Error al finalizar", mensaje)
    if respuesta:
        cancelar_factura()
        cerrar_ventana_factura(ventana_facturas)
        abrir_ventana_principal(ventana_principal)
        return

def cerrar_ventana_factura(ventana_facturas):
    ventana_facturas.destroy()


def abrir_ventana_principal(ventana_principal):
    # ventana_principal.deiconify()  # Mostrar ventana principal
    ventana_principal.state("zoomed")

def ventana_facturas(ventana_principal):
    # listado_productos_agregar()
    #Obtener los datos de la tabla producto
    query = "SELECT nombre_producto, id FROM producto"
    cursor.execute(query)
    datos = cursor.fetchall()
    diccionario = dict((nombre, id) for nombre, id in datos)
    var_seleccion = StringVar()

    ventana_facturas = tk.Toplevel(ventana_principal)
    ventana_facturas.title("Registrar Factura")
    ventana_facturas.state("zoomed")# Abre la ventana maximizada

    crear_factura()

    lista_de_productos = OptionMenu(ventana_facturas, var_seleccion, *diccionario.keys())
    label_producto = tk.Label(ventana_facturas, text="Producto:", width=100)
    label_cantidad = tk.Label(ventana_facturas, text="Cantidad:", width=100)
    entry_cantidad = tk.Entry(ventana_facturas, width=12)
    label_relleno1 = tk.Label(ventana_facturas, text="")
    label_relleno2 = tk.Label(ventana_facturas, text="", width=70)
    label_relleno3 = tk.Label(ventana_facturas, text="")

    tabla_detalles = ttk.Treeview(ventana_facturas)
    tabla_detalles['columns'] = ("Producto", "Cantidad", "Precio", "Total") # Definir las columnas
    
    # Definir encabezados de columna
    tabla_detalles.heading("#0", text="", anchor="w")
    tabla_detalles.heading("Producto", text="Producto", anchor="w")
    tabla_detalles.heading("Precio", text="Precio", anchor="w")
    tabla_detalles.heading("Cantidad", text="Cantidad", anchor="w")
    tabla_detalles.heading("Total", text="Total", anchor="w")

    # Definir el ancho de las columnas
    tabla_detalles.column("#0", width=0, stretch=tk.NO)
    tabla_detalles.column("Producto", width=200, anchor="w")
    tabla_detalles.column("Precio", width=150, anchor="w")
    tabla_detalles.column("Cantidad", width=100, anchor="w")
    tabla_detalles.column("Total", width=100, anchor="w")
    
    tabla_detalles.grid(row=8, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)
    ventana_facturas.grid_rowconfigure(8, weight=1)
    ventana_facturas.grid_columnconfigure(0, weight=1)
    
    # Crear una etiqueta para mostrar el total a pagar
    label_total = tk.Label(ventana_facturas, text="Total a pagar: $0", justify="left")  # Cambiar el valor de sticky a "anchor" con valor "w"
    label_total.grid(row=5, column=0, columnspan=4, sticky="e")
    label_total.configure(bg='black', fg='white', font=('Helvetica', 12, 'bold'))

    button_agregar = tk.Button(ventana_facturas, text="Agregar", width=120, bg="#1465bb", height=1, font=15, command=lambda: validacion_cantidad_productos(var_seleccion, entry_cantidad, diccionario, tabla_detalles, label_total))

    #Establecemos la posicion de cada componente de la ventana
    label_producto.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    lista_de_productos.grid(row=0, column=1, pady=10, sticky="w")
    # label_relleno1.grid(row=0, column=2, padx=300, pady=10, sticky="e")
    label_cantidad.grid(row=1, column=0, sticky="w")
    entry_cantidad.grid(row=1, column=1, sticky="w")
    label_relleno2.grid(row=1, column=2, sticky="e")
    # Configurar la tabla_detalles para que ocupe 4 columnas en la cuadrícula
    tabla_detalles.grid(row=4, column=0, columnspan=4, sticky="nsew")  # Agregar sticky="nsew" para que se expanda en todas las direcciones

    # Configurar la redimensión de filas y columnas en la ventana
    ventana_facturas.grid_rowconfigure(4, weight=1)  # Permitir que la fila 4 se redimensione verticalmente
    ventana_facturas.grid_columnconfigure(0, weight=1)
    lista_de_productos.focus_set()

    button_agregar.grid(row=6, column=0)
    boton_finalizar = tk.Button(ventana_facturas, text="Finalizar", width=70, height=1, bg="#009929", font=15,  command= lambda: [boton_finalizar_factura(ventana_facturas, ventana_principal)])
    boton_finalizar.grid(row=6, column=2)
    # label_relleno2.grid(row=6, column=3)

    ventana_principal.withdraw()# Ocultar ventana principal
    ventana_facturas.protocol("WM_DELETE_WINDOW", lambda: [abrir_ventana_principal(ventana_principal), cerrar_ventana_factura(ventana_facturas)])

    actualizar_productos_facturas(tabla_detalles, label_total)
