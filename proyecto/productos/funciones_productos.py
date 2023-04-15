from conexion_2 import conexion, cursor


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
        cursor.execute("UPDATE producto SET estado='Eliminado' WHERE id=%s", (id_producto,))
        conexion.commit()
        # Actualizar la lista de productos
        actualizar_productos(lista_productos)


