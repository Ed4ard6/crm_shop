import tkinter as tk
from conexcion import cursor, conexion
# Función para insertar un nuevo producto en el inventario
def agregar_producto():
    nombre = entry_nombre.get()
    tipo = entry_tipo.get()
    cantidad = int(entry_cantidad.get())
    precio_compra = float(entry_precio.get())
    precio_venta = precio_compra * 1.2  
    datos = (nombre, tipo, cantidad, precio_compra)
    consulta = "INSERT INTO inventario (nombre, tipo, cantidad, precio_compra) VALUES (%s, %s, %s, %s)"
    cursor.execute(consulta, datos)
    conexion.commit()
    actualizar_productos()


def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_tipo.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    new_disable()

  


def new_enable():
    # Mostrar los widgets de entrada después de eliminar un producto
    entry_nombre.configure(state=tk.NORMAL)
    entry_tipo.configure(state=tk.NORMAL)
    entry_cantidad.configure(state=tk.NORMAL)
    entry_precio.configure(state=tk.NORMAL)


    label_nombre.configure(state=tk.NORMAL)
    label_tipo.configure(state=tk.NORMAL)
    label_cantidad.configure(state=tk.NORMAL)
    label_precio.configure(state=tk.NORMAL)
    button_agregar.configure(state=tk.NORMAL)
    button_cancelar.configure(state=tk.NORMAL)

    button_nuevo.configure(state=tk.DISABLED)
    button_actualizar.configure(state=tk.DISABLED)
    button_eliminar.configure(state=tk.DISABLED)

    
def new_disable():
    # Ocultar los widgets de entrada después de guardar un producto
    entry_nombre.configure(state=tk.DISABLED)
    entry_tipo.configure(state=tk.DISABLED)
    entry_cantidad.configure(state=tk.DISABLED)
    entry_precio.configure(state=tk.DISABLED)

    label_nombre.configure(state=tk.DISABLED)
    label_tipo.configure(state=tk.DISABLED)
    label_cantidad.configure(state=tk.DISABLED)
    label_precio.configure(state=tk.DISABLED)

    button_agregar.configure(state=tk.DISABLED)
    button_cancelar.configure(state=tk.DISABLED)

    #habilita los botones de nuevo, Actualizar, Eliminar
    button_nuevo.configure(state=tk.NORMAL)
    button_actualizar.configure(state=tk.NORMAL)
    button_eliminar.configure(state=tk.NORMAL)


def eliminar_producto():
    print('registro eliminado...')
     # Obtener el índice del elemento seleccionado en la lista de productos
    seleccionado = lista_productos.curselection()
    if seleccionado:
        indice = seleccionado[0]
        # Obtener el ID del producto a eliminar
        producto = lista_productos.get(indice)
        id_producto = producto.split(',')[0][4:]
        # Eliminar el producto de la base de datos
        cursor.execute("DELETE FROM inventario WHERE id=%s", (id_producto,))
        conexion.commit()
        # Actualizar la lista de productos
        actualizar_productos()

# Función para actualizar la lista de productos en la GUI
def actualizar_productos():
    cursor.execute("SELECT * FROM inventario")
    resultados = cursor.fetchall()
    lista_productos.delete(0, tk.END)
    for producto in resultados:
        precio_venta = producto[4] * 1.2
        lista_productos.insert(tk.END, f"ID: {producto[0]}, Nombre: {producto[1]} -- Tipo: {producto[2]} -- Cantidad: {producto[3]} -- Precio de compra: {producto[4]:.2f} -- Precio de venta: {precio_venta:.2f}")

def mostrar_formulario_emergente():
    
    formulario_emergente = tk.Toplevel()
    # Agrega los widgets del formulario emergente aquí
    boton_regresar = tk.Button(formulario_emergente, text="Regresar", command=formulario_emergente.destroy)
    boton_regresar.pack()
    formulario_emergente.grab_set()
    formulario_emergente.wait_window()
    ventana_principal.deiconify()  # Esto volverá a mostrar la ventana principal cuando se cierre el formulario emergente


# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Inventario Eduardo")

# Crear los widgets de la GUI
label_nombre = tk.Label(ventana_principal, text="Nombre:")
entry_nombre = tk.Entry(ventana_principal)
label_tipo = tk.Label(ventana_principal, text="Tipo:")
entry_tipo = tk.Entry(ventana_principal)
label_cantidad = tk.Label(ventana_principal, text="Cantidad:")
entry_cantidad = tk.Entry(ventana_principal)
label_precio = tk.Label(ventana_principal, text="Precio de compra:")
entry_precio = tk.Entry(ventana_principal)
button_agregar = tk.Button(ventana_principal, text="Guardar", command=agregar_producto)
button_cancelar = tk.Button(ventana_principal, text="Cancelar", command=limpiar_campos)
button_eliminar = tk.Button(ventana_principal, text="Eliminar", command=eliminar_producto)
button_eliminar = tk.Button(ventana_principal, text="Facturas", command=eliminar_producto)
button_nuevo = tk.Button(ventana_principal, text="Nuevo", command=new_enable)
button_actualizar = tk.Button(ventana_principal, text="Actualizar", command=eliminar_producto)
lista_productos = tk.Listbox(ventana_principal, height=10, width=100)

# Ubicar los widgets en la ventana_principal
label_nombre.grid(row=0, column=0)
entry_nombre.grid(row=0, column=1)
label_tipo.grid(row=1, column=0)
entry_tipo.grid(row=1, column=1)
label_cantidad.grid(row=2, column=0)
entry_cantidad.grid(row=2, column=1)
label_precio.grid(row=3, column=0)
entry_precio.grid(row=3, column=1)
button_agregar.grid(row=4, column=0, columnspan=2)
button_cancelar.grid(row=4, column=1, columnspan=3)
button_nuevo.grid(row=5, column=0)
button_actualizar.grid(row=5, column=1)
button_eliminar.grid(row=5, column=2)#, columnspan=2-- Esto es para dejar uin esacio para ubicar mejor los botones
lista_productos.grid(row=6, column=0, columnspan=3)

new_disable()



# Actualizar la lista de productos al inicio de la aplicación
actualizar_productos()

# Ejecutar la aplicación
ventana_principal.mainloop()
