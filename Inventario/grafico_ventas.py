import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import datetime
from conexion_2 import conexion, cursor
import matplotlib.ticker as ticker

def ventas_por_mes():

    # Realizar la consulta a la base de datos
    query = "SELECT DATE_FORMAT(fecha, '%M %Y') AS mes, SUM(total) AS total_venta FROM facturas GROUP BY mes ORDER BY fecha;"
    cursor.execute(query)

    # Obtener los datos de la tabla y almacenarlos en un DataFrame
    df = pd.DataFrame(cursor.fetchall(), columns=["mes", "total_venta"])

    # Crear el gráfico
    fig, ax = plt.subplots()
    sns.barplot(data=df, x='mes', y='total_venta')

    # Agregar títulos y etiquetas de los ejes
    plt.title('Total de ventas por mes')
    plt.xlabel('Mes')
    plt.ylabel('Total de ventas')

    # Personalizar formato del eje y
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))

    # Ajustar los márgenes
    fig.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95)

    # Ajustar el tamaño del gráfico para evitar que las etiquetas se corten
    plt.tight_layout()

    # Mostrar la figura en una ventana
    root = tk.Tk()
    root.state('zoomed')
    root.wm_title("Gráfico de ventas por mes")

    def cerrar_ventana():
        print("Cerrando reportes .....")
        root.destroy()
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
