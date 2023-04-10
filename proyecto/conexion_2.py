import mysql.connector

# Conectar a la base de datos
conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="inventario"
)

cursor = conexion.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS `inventario` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;")
cursor.execute("USE `inventario`;")
