import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import datetime
from conexion_2 import conexion, cursor

def ventas_por_mes_pastel():
    # Realizar la consulta a la base de datos
    query = "SELECT DATE_FORMAT(fecha, '%M %Y') AS mes, SUM(total) AS total_venta FROM facturas GROUP BY mes ORDER BY fecha;"
    cursor.execute(query)

    # Obtener los datos de la tabla y almacenarlos en un DataFrame
    df = pd.DataFrame(cursor.fetchall(), columns=["mes", "total_venta"])

    # Crear el gráfico de pastel
    fig, ax = plt.subplots()
    ax.pie(df['total_venta'], labels=df['mes'], autopct='%1.1f%%', startangle=90) # Usar el total de ventas como datos y el mes como etiquetas

    # Agregar título
    plt.title('Porcentaje de ventas por mes')

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
