import tkinter as tk


# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Inventario number 2")

class ventanaProductos:
    
    def __init__(self, ventana_productos):
        self.ventana_productos = ventana_productos
        self.ventana_productos = tk.Toplevel(ventana_productos.ventana_principal)
        self.ventana_productos.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_productos)
        self.boton_cerrar = tk.Button(self.ventana_productos, text="Cerrar", command=self.cerrar_ventana_productos)
        self.boton_cerrar.pack()
        self.ventana_productos.grab_set()
        self.ventana_productos.wait_window()
        self.ventana_productos_principal.habilitar_botones() 

    def cerrar_ventana_productos(self):
        self.ventana_productos.grab_release()
        self.ventana_productos.destroy()


    