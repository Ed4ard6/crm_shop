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

# Crear gráfico de barras
plt.bar(nombres_productos, cantidades)
plt.xticks(rotation=90)
plt.xlabel('Producto')
plt.ylabel('Cantidad')
plt.title('Stock of products')

# Establecer formato de los números en el eje y
plt.yticks(range(0, max(cantidades)+1, 10), ["%.0f" % x for x in range(0, max(cantidades)+1, 10)])

plt.show()
