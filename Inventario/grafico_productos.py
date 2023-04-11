from conexion_2 import conexion, cursor
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure


def producto_mas_vendido():

    query = "SELECT producto.id, producto.nombre_producto AS producto, SUM(det_factura.cantidad) AS cantidad_vendida FROM det_factura JOIN producto ON det_factura.id_producto = producto.id GROUP BY producto.nombre_producto ORDER BY cantidad_vendida DESC LIMIT 10;"

    cursor.execute(query)
    # Obtener los datos de la tabla y almacenarlos en un DataFrame
    df = pd.DataFrame(cursor.fetchall(), columns=["id", "producto", "cantidad_vendida"])

    # Crear el gráfico
    fig, ax = plt.subplots()
    sns.barplot(data=df, x='producto', y='cantidad_vendida')

    # Agregar títulos y etiquetas de los ejes
    plt.title('Los 10 productos mas vendidos')
    #plt.xlabel('Producto')
    plt.ylabel('Cantidad vendida')
    
    # Ajustar los márgenes
    fig.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95)
    plt.tight_layout()
    # Mostrar la figura en una ventana
    root = tk.Tk()
    root.state('zoomed')
    root.wm_title("Gráfico de productos")

    def cerrar_ventana():
        print("Cerrando reportes .....")
        # cursor.close()
        # conexion.close()
        root.destroy()#root.quit() con esta ce cierran todas las ventanas aun que no deberia
        plt.close(fig)


    root.protocol("WM_DELETE_WINDOW", cerrar_ventana)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Mostrar la ventana
    root.mainloop()


    # Cerrar la conexión a la base de datos
    cursor.close()
    conexion.close()

   