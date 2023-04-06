import mysql.connector
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="invetario_python"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT nombre, cantidad FROM inventario")

result = mycursor.fetchall()

# Crear listas con nombres de productos y cantidades
nombres_productos = []
cantidades = []
for row in result:
    nombres_productos.append(row[0])
    cantidades.append(row[1])

# Crear gráfico de barras 2D
plt.bar(nombres_productos, cantidades, width=0.5)
plt.xticks(rotation=90)
plt.xlabel('Producto')
plt.ylabel('Cantidad')
plt.title('Stock of products')
plt.show()
