import mysql.connector
import tkinter as tk

# Conectar a la base de datos
conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="invetario_python"
)

# Crear la tabla si no existe
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS inventario (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), tipo VARCHAR(255), cantidad INT, precio_compra FLOAT)")

# Función para insertar un nuevo producto en el inventario
def agregar_producto():
    nombre = entry_nombre.get()
    tipo = entry_tipo.get()
    cantidad = int(entry_cantidad.get())
    precio_compra = float(entry_precio.get())
    datos = (nombre, tipo, cantidad, precio_compra)
    consulta = "INSERT INTO inventario (nombre, tipo, cantidad, precio_compra) VALUES (%s, %s, %s, %s)"
    cursor.execute(consulta, datos)
    conexion.commit()
    #actualizar_productos()

# Función para actualizar un producto del inventario
def actualizar_producto():
    id_producto = int(entry_id.get())
    nombre = entry_nombre.get()
    tipo = entry_tipo.get()
    cantidad = int(entry_cantidad.get())
    precio_compra = float(entry_precio.get())
    datos = (nombre, tipo, cantidad, precio_compra, id_producto)
    consulta = "UPDATE inventario SET nombre=%s, tipo=%s, cantidad=%s, precio_compra=%s WHERE id=%s"
    cursor.execute(consulta, datos)
    conexion.commit()
    #actualizar_productos()

# Función para eliminar un producto del inventario
def eliminar_producto():
    id_producto = int(entry_id.get())
    consulta = "DELETE FROM inventario WHERE id=%s"
    cursor.execute(consulta, (id_producto,))
    conexion.commit()
   # actualizar_productos()

# Función para actualizar la lista de productos en la GUI
""" def actualizar_productos():
    cursor.execute("SELECT * FROM inventario")
    resultados = cursor.fetchall()
    lista_productos.delete(0, tk.END)
    for producto in resultados:
        precio_venta = producto[4] * 1.2
        lista_productos.insert(tk.END, f"ID: {producto[0]}, Nombre: {producto[1]}, Tipo: {producto[2]}, Cantidad: {producto[3]}, Precio de compra: {producto[4]:.2f}, Precio de venta: {precio_venta:.2f}")
 """
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inventario de miscelánea")

# Crear los widgets de la GUI
label_id = tk.Label(ventana, text="ID:")
entry_id = tk.Entry(ventana)
label_nombre = tk.Label(ventana, text="Nombre:")
entry_nombre = tk.Entry(ventana)
label_tipo = tk.Label(ventana, text="Tipo:")
entry_tipo = tk.Entry(ventana)
label_cantidad = tk.Label(ventana, text="Cantidad:")
entry_cantidad = tk.Entry(ventana)
label_precio = tk.Label(ventana, text="Precio de compra:")
entry_precio = tk.Entry(ventana)
button_agregar = tk.Button(ventana, text="Agregar", command=agregar_producto)
button_actualizar = tk.Button(ventana, text="Actualizar", command=actualizar_producto)
