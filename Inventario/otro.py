import tkinter as tk

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        
        self.btn_formulario = tk.Button(self, text="Abrir formulario", command=self.abrir_formulario)
        self.btn_formulario.pack(pady=10)
        
    def abrir_formulario(self):
        self.btn_formulario.pack_forget() # Elimina el botón de la ventana principal
        self.formulario = Formulario(self)
        
class Formulario(tk.Toplevel):
    def __init__(self, ventana_principal):
        super().__init__()
        self.title("Formulario")
        
        self.ventana_principal = ventana_principal
        
        # Aquí iría el diseño del formulario
        
        self.btn_regresar = tk.Button(self, text="Regresar a la ventana principal", command=self.regresar_ventana_principal)
        self.btn_regresar.pack(pady=10)
        
    def regresar_ventana_principal(self):
        self.destroy() # Cierra la ventana del formulario
        self.ventana_principal.btn_formulario.pack() # Vuelve a mostrar el botón en la ventana principal

if __name__ == '__main__':
    ventana_principal = VentanaPrincipal()
    ventana_principal.mainloop()
