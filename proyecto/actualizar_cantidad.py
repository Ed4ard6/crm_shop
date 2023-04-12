from conexion_2 import conexion, cursor

def actualizar_cantidades():
    # Obtener los datos de los productos vendidos y su cantidad desde la tabla det_factura
    cursor.execute("SELECT id , cantidad FROM det_factura WHERE id_factura = %s", (id_factura,))
    productos_vendidos = cursor.fetchall()
    
    for producto in productos_vendidos:
        id_producto = producto[0]
        cantidad_vendida = producto[1]
        
        # Buscar el registro correspondiente en la tabla productos
        cursor.execute("SELECT cantidad FROM productos WHERE id = %s", (id_producto,))
        cantidad_actual = cursor.fetchone()[0]
        
        # Restar la cantidad vendida de la cantidad disponible
        nueva_cantidad = cantidad_actual - cantidad_vendida
        
        # Actualizar la cantidad disponible en la tabla productos
        cursor.execute("UPDATE productos SET cantidad = %s WHERE id = %s", (nueva_cantidad, id_producto))
        
    # Guardar los cambios en la base de datos
    conexion.commit()
