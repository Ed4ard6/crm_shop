from conexion_2 import conexion, cursor
from funciones import ultima_factura, agregar_productos 
from tkinter import *

root = Tk()

# Obtener el valor de la última factura
ultima_factura_id = ultima_factura()
id_producto = agregar_productos()
# Imprimir el valor de la última factura
print("El valor de la última factura es:", ultima_factura_id)
print("el id del producto es: ", id_producto)


app.mainloop()

