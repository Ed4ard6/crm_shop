import tkinter as tk

class VentanaSecundaria:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana = tk.Toplevel(ventana_principal.root)
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.boton_cerrar = tk.Button(self.ventana, text="Cerrar", command=self.cerrar_ventana)
        self.boton_cerrar.pack()
        self.ventana.grab_set()
        self.ventana.wait_window()
        self.ventana_principal.habilitar_botones() 

    def cerrar_ventana(self):
        self.ventana.grab_release()
        self.ventana.destroy()

class VentanaPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.boton_abrir = tk.Button(self.root, text="Abrir ventana", command=self.abrir_ventana)
        self.boton_abrir.pack()
        self.boton_guardar = tk.Button(self.root, text="Guardar", command= lambda : self.boton_guarda())
        self.boton_guardar.pack()
        self.boton2 = tk.Button(self.root, text="Cancelar", command= lambda :  self.boton_cancela())
        self.boton2.pack()

    def boton_guarda(self):
        print("Guardando informacion........")

    def boton_cancela(self):
        print("Cancelando proceso...........")

    def abrir_ventana(self):
        self.deshabilitar_botones()
        self.ventana_secundaria = VentanaSecundaria(self)

    def habilitar_botones(self):
        self.boton_guardar.config(state=tk.NORMAL)
        self.boton2.config(state=tk.NORMAL)

def actualizar_productos(lista_productos):
    cursor.execute("SELECT * FROM producto")
    resultados = cursor.fetchall()
    lista_productos.delete(0, tk.END)
    for producto in resultados:
        precio_venta = producto[4] * 1.2
        lista_productos.insert(tk.END, f"ID: {producto[0]}, Producto: {producto[1]} -- Categoria: {producto[2]} -- precio_compra: {producto[3]:.2f} -- cantidad: {producto[4]} -- precio_venta: {producto[5]} -- estado: {producto[6]}")


def deshabilitar_botones():
    for boton in botones.values():
        boton.configure(state="disabled")

def habilitar_botones():
    for boton in botones.values():
        boton.configure(state="normal")


def ventana_facturas():
    deshabilitar_botones()
    # lista_productos()
    #Obtener los datos de la tabla producto
    query = "SELECT nombre_producto, id FROM producto"
    cursor.execute(query)
    datos = cursor.fetchall()
    diccionario = dict((nombre, id) for nombre, id in datos)
    var_seleccion = StringVar()

    ventana_emergente = tk.Toplevel(ventana_principal)
    ventana_emergente.title("Registrar Factura")
    ventana_emergente.geometry("300x350")
    #crear_factura()

    lista_de_productos = OptionMenu(ventana_emergente, var_seleccion, *diccionario.keys())
    label_producto = tk.Label(ventana_emergente, text="Producto:")
    label_cantidad = tk.Label(ventana_emergente, text="Cantidad:")
    entry_cantidad = tk.Entry(ventana_emergente)
    
    button_agregar = tk.Button(ventana_emergente, text="Guardar", command=lambda: [agregar_detalles_factura(var_seleccion, entry_cantidad, diccionario), limpiar_formulario_detalles_fatura(var_seleccion, entry_cantidad)])


    #Establecemos la posicion de cada componente de la ventana
    label_producto.grid(row=0, column=0)
    lista_de_productos.grid(row=0, column=1)
    label_cantidad.grid(row=1, column=0)
    entry_cantidad.grid(row=1, column=1)
    
    button_agregar.grid(row=6, column=0)

    boton_regresar = tk.Button(ventana_emergente, text="Finalizar", command= lambda: close_modal_new_product(ventana_emergente))
    boton_regresar.grid(row=6, column=1)


def close_modal_new_product(ventana_emergente : tk.Toplevel):
    ventana_emergente.destroy()
    actualizar_productos(lista_productos)
    habilitar_botones()

def limpiar_formulario_detalles_fatura(var_seleccion, entry_cantidad):
    var_seleccion.set("")  # limpia la opción seleccionada en la lista de productos
    entry_cantidad.delete(0, tk.END)  # limpia el campo de entrada de cantidad


# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Inventario number 2")


app.mainloop()

