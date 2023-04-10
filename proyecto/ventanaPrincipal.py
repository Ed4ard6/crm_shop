import tkinter as tk
from conexion_2 import conexion, cursor

class ventanaProductos:

    def __init__(self, ventana_principal):
        self.ventana_productos = tk.Toplevel(ventana_principal)
        self.ventana_productos.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_productos)
        self.ventana_principal = ventana_principal

        self.botones = {
            "nuevo": tk.Button(self.ventana_productos, text="Nuevo", command=self.abrir_ventana_nuevo_producto),
            "actualizar": tk.Button(self.ventana_productos, text="Actualizar", command=self.ventana_facturas),
            "eliminar": tk.Button(self.ventana_productos, text="Eliminar", command="")
        }

        self.button_nuevo = self.botones["nuevo"]
        self.button_actualizar = self.botones["actualizar"]
        self.button_eliminar = self.botones["eliminar"]

        self.button_nuevo.grid(row=0, column=0)
        self.button_actualizar.grid(row=0, column=1)
        self.button_eliminar.grid(row=0, column=2)

        self.lista_productos = tk.Listbox(self.ventana_productos, height=10, width=120)
        self.lista_productos.grid(row=1, column=0, columnspan=3)

        self.lista_productos.bind("<<ListboxSelect>>", self.seleccion_producto)

        # Actualizar la lista de productos al inicio de la aplicación
        self.actualizar_productos(self.lista_productos)

    def abrir_ventana_nuevo_producto(self):
        # Lógica para abrir la ventana de nuevo producto
        pass

    def ventana_facturas(self):
        # Lógica para abrir la ventana de facturas
        pass

    def seleccion_producto(self, event):
        # Lógica para manejar la selección de un producto en la lista
        pass

    def actualizar_productos(self):
        # Lógica para actualizar la lista de productos
        pass

    def cerrar_ventana_productos(self):
        self.ventana_productos.grab_release()
        self.ventana_productos.destroy()


class VentanaPrincipal:
    def __init__(self):
        # Crear la ventana principal
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Adonde quieres ir")

        self.botones = {
            "inventario": tk.Button(self.ventana_principal, text="Inventario", command= lambda : ventanaProductos(self.ventana_principal)),
            "facturas": tk.Button(self.ventana_principal, text="Facturas", command="ventana_facturas"),
            "reportes": tk.Button(self.ventana_principal, text="Reportes", command="")
        }
        self.button_inventario = self.botones["inventario"]
        self.button_facturas = self.botones["facturas"]
        self.button_reportes = self.botones["reportes"]
        self.button_inventario.pack()
        self.button_facturas.pack()
        self.button_reportes.pack()

    def run(self):
        self.ventana_principal.mainloop()


if __name__ == '__main__':
    ventana_principal = VentanaPrincipal()
    ventana_principal.run()
