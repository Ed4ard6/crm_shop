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
