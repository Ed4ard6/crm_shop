from conexion_2 import conexion, cursor
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def producto_mas_vendido(ventana_principal):
    query = "SELECT producto.id, producto.nombre_producto AS producto, SUM(det_factura.cantidad) AS cantidad_vendida FROM det_factura JOIN producto ON det_factura.id_producto = producto.id GROUP BY producto.nombre_producto ORDER BY cantidad_vendida DESC LIMIT 10;"
    cursor.execute(query)
    # Obtener los datos de la tabla y almacenarlos en un DataFrame
    df = pd.DataFrame(cursor.fetchall(), columns=["id", "producto", "cantidad_vendida"])

    # Crear el gráfico
    fig, ax = plt.subplots()
    p = sns.barplot(data=df, x='producto', y='cantidad_vendida')

    # Agregar títulos y etiquetas de los ejes
    plt.title('Los 10 productos mas vendidos')
    plt.ylabel('Cantidad vendida')

    # Añadir etiquetas a las barras
    for index, row in df.iterrows():
        ax.text(index, row.cantidad_vendida, row.producto, ha='center', rotation='vertical')

    # Ajustar los márgenes
    fig.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95)
    plt.tight_layout()

    # Mostrar la figura en una ventana
    grafico_top_10 = tk.Tk()
    grafico_top_10.state('zoomed')  # Maximizar la ventana al iniciar
    grafico_top_10.wm_title("Gráfico de productos")

    def cerrar_ventana():
        grafico_top_10.destroy()
        plt.close(fig)
        ventana_principal.state("zoomed")

    grafico_top_10.protocol("WM_DELETE_WINDOW", cerrar_ventana)

    canvas = FigureCanvasTkAgg(fig, master=grafico_top_10)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Ocultar los nombres de los productos en el eje x
    ax.set_xticklabels([])

    ventana_principal.withdraw()# Ocultar ventana principal

    # Mostrar la ventana
    grafico_top_10.mainloop()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conexion.close()

