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
