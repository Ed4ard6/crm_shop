import tkinter as tk
from funciones import actualizar_productos, limpiar_campos, agregar_producto
from conexion_2 import conexion, cursor





def abrir_ventana_emergente():
    print("abrir_ventana_emergente....")
    ventana_emergente = tk.Toplevel(ventana_principal)
    ventana_emergente.geometry("900x500")

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








def habilitar_insert():
    # Fcuncion para Habilitar los formularios de agregar productos
    """ entry_nombre.configure(state=tk.NORMAL)
    entry_categoria.configure(state=tk.NORMAL)
    entry_cantidad.configure(state=tk.NORMAL)
    entry_precio.configure(state=tk.NORMAL)

    label_nombre.configure(state=tk.NORMAL)
    label_categoria.configure(state=tk.NORMAL)
    label_cantidad.configure(state=tk.NORMAL)
    label_precio.configure(state=tk.NORMAL)

    button_agregar.configure(state=tk.NORMAL)
    button_cancelar.configure(state=tk.NORMAL) """

    #habilita los botones de nuevo, Actualizar, Eliminar
    # button_nuevo.configure(state=tk.DISABLED)
    # button_actualizar.configure(state=tk.DISABLED)
    # button_eliminar.configure(state=tk.DISABLED)

#def desabilitar_insert():
    # Fcuncion para desabilidar los formularios de agregar productos

   



# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Inventario number 2")


# Crear los widgets de la GUI


#para los margin untilizamos pad y el eje ya sea x o, =seguido del numero de pixeles, y para los pading utilizamos los ipad
#para alinear utilizamos side=tk.left       ejemplo entry_name.pack(side=tk.left)

button_eliminar = tk.Button(ventana_principal, text="Eliminar", command="")
button_eliminar = tk.Button(ventana_principal, text="Facturas", command="")
button_nuevo = tk.Button(ventana_principal, text="Nuevo", command=habilitar_insert)
button_actualizar = tk.Button(ventana_principal, text="Actualizar", command="")
lista_productos = tk.Listbox(ventana_principal, height=10, width=150)

boton_ventana_emergente = tk.Button(ventana_principal, text="Nuevo_producto", command=abrir_ventana_emergente)


# Ubicar los widgets en la ventana_principal

button_nuevo.grid(row=6, column=0)
button_actualizar.grid(row=6, column=1)
button_eliminar.grid(row=6, column=2)#, columnspan=2-- Esto es para dejar uin esacio para ubicar mejor los botones
boton_ventana_emergente.grid(row=7, column=0)
lista_productos.grid(row=8, column=0, columnspan=3)


#desabilita el formulario de insercion al inicio de la aplicacion


# Actualizar la lista de productos al inicio de la aplicación
actualizar_productos(lista_productos)

# Ejecutar la aplicación
ventana_principal.mainloop()