import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import datetime
from conexion_2 import conexion, cursor

def ventas_por_mes(ventana_principal):
    # Realizar la consulta a la base de datos
    query = "SELECT DATE_FORMAT(fecha, '%M %Y') AS mes, SUM(total) AS total_venta FROM facturas GROUP BY mes ORDER BY fecha;"
    cursor.execute(query)

    # Obtener los datos de la tabla y almacenarlos en un DataFrame
    df = pd.DataFrame(cursor.fetchall(), columns=["mes", "total_venta"])

    # Crear el gráfico de barras horizontales
    fig, ax = plt.subplots()
    bars = ax.barh(df['mes'], df['total_venta'])

    # Agregar títulos y etiquetas de los ejes
    plt.title('Total de ventas por mes')
    plt.ylabel('Mes')

    # Personalizar formato del eje x
    ax.xaxis.set_major_formatter('${x:,.0f}')

    # Colocar los valores del total de cada mes en el eje x
    ax.set_xticks(df['total_venta'])
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')

    # Ajustar los márgenes
    fig.subplots_adjust(left=0.25, bottom=0.05, right=0.95, top=0.95)

    # Ajustar el tamaño del gráfico para evitar que las etiquetas se corten
    plt.tight_layout()

    # Mostrar la figura en una ventana
    ventas_mes = tk.Tk()
    ventas_mes.state('zoomed')
    ventas_mes.wm_title("Gráfico de ventas por mes")

    def cerrar_ventana():
        ventas_mes.destroy()
        plt.close(fig)
        ventana_principal.state("zoomed")

    ventas_mes.protocol("WM_DELETE_WINDOW", cerrar_ventana)

    canvas = FigureCanvasTkAgg(fig, master=ventas_mes)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    ventana_principal.withdraw()# Ocultar ventana principal

    # Mostrar la ventana
    ventas_mes.mainloop()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conexion.close()
