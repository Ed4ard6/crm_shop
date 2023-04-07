import tkinter as tk
from funciones import actualizar_productos, limpiar_campos, agregar_producto
from conexion_2 import conexion, cursor



def deshabilitar_botones():
    for boton in botones.values():
        boton.configure(state="disabled")

def habilitar_botones():
    for boton in botones.values():
        boton.configure(state="normal")


def abrir_ventana_emergente():
    deshabilitar_botones()
    print("abrir_ventana_emergente....")
    ventana_emergente = tk.Toplevel(ventana_principal)
    # ventana_emergente.geometry("900x500")

    label_nombre = tk.Label(ventana_emergente, text="Nombre_p:")#bg= color de fondo     fg= color de letra
    entry_nombre = tk.Entry(ventana_emergente)
    label_categoria = tk.Label(ventana_emergente, text="Categoria:")
    entry_categoria = tk.Entry(ventana_emergente)
    label_cantidad = tk.Label(ventana_emergente, text="Cantidad:")
    entry_cantidad = tk.Entry(ventana_emergente)
    label_precio = tk.Label(ventana_emergente, text="Precio de compra:")
    entry_precio = tk.Entry(ventana_emergente)
    button_agregar = tk.Button(ventana_emergente, text="Guardar", command = lambda :agregar_producto(entry_nombre, entry_categoria, entry_cantidad, entry_precio))
    button_cancelar = tk.Button(ventana_emergente, text="Cancelar", command="")

    #Establecemos la posicion de cada componente de la ventana
    label_nombre.pack()
    entry_nombre.pack()
    label_categoria.pack()
    entry_categoria.pack()
    label_cantidad.pack()
    entry_cantidad.pack()
    label_precio.pack()
    entry_precio.pack()
    button_agregar.pack()
    button_cancelar.pack()

    boton_regresar = tk.Button(ventana_emergente, text="Regresar", command= lambda: close_modal_new_product(ventana_emergente))
    boton_regresar.pack()




def close_modal_new_product(ventana_emergente : tk.Toplevel):
    ventana_emergente.destroy()
    actualizar_productos(lista_productos)
    habilitar_botones()

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Inventario number 2")


# Crear los widgets de la GUI
botones = {
    "eliminar": tk.Button(ventana_principal, text="Eliminar", command=""),
    "facturas": tk.Button(ventana_principal, text="Facturas", command=""),
    "nuevo": tk.Button(ventana_principal, text="Nuevo", command=abrir_ventana_emergente),
    "actualizar": tk.Button(ventana_principal, text="Actualizar", command="")
}

button_nuevo = botones["nuevo"]
button_actualizar = botones["actualizar"]
button_eliminar = botones["eliminar"]
lista_productos = tk.Listbox(ventana_principal, height=10, width=100)

# Ubicar los widgets en la ventana_principal
button_nuevo.grid(row=6, column=0)
button_actualizar.grid(row=6, column=1)
button_eliminar.grid(row=6, column=2)#, columnspan=2-- Esto es para dejar uin esacio para ubicar mejor los botones
lista_productos.grid(row=8, column=0, columnspan=3)

# Actualizar la lista de productos al inicio de la aplicación
actualizar_productos(lista_productos)

# Ejecutar la aplicación
ventana_principal.mainloop()