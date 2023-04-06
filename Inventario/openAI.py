import mysql.connector

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

# Insertar un nuevo producto en el inventario
nombre = input("Ingrese el nombre del producto: ")
tipo = input("Ingrese el tipo del producto: ")
cantidad = int(input("Ingrese la cantidad de productos: "))
precio_compra = float(input("Ingrese el precio de compra del producto: "))
precio_venta = precio_compra * 1.2
datos = (nombre, tipo, cantidad, precio_compra)
consulta = "INSERT INTO inventario (nombre, tipo, cantidad, precio_compra) VALUES (%s, %s, %s, %s)"
cursor.execute(consulta, datos)
conexion.commit()

# Mostrar los productos del inventario
cursor.execute("SELECT * FROM inventario")
resultados = cursor.fetchall()
print("Productos en el inventario:")
for producto in resultados:
    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Tipo: {producto[2]}, Cantidad: {producto[3]}, Precio de compra: {producto[4]:.2f}, Precio de venta: {precio_venta:.2f}")

# Cerrar la conexión
conexion.close()
