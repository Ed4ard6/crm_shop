                                            ###############################################
                                            ###############################################
                                            ###           INTEGRANTES DIPLOMADO         ###
                                            ###     Norbey Esledier Quiceno Martinez    ###
                                            ###         Elkin Smith Guzman Rojas        ###
                                            ###############################################
                                            ###############################################


# — — — — — — — — — — — — - Backend Layer, Figure Canvas Layer: Encompases area in which figures are drawn — — — — — — — — — — — — -
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanva

#— — — — — — — — — — — — -Desde la capa de Artista, importando la Figura de Artista: La capa de artista sabe cómo usar un renderizador para dibujar un objeto----------------------
from matplotlib.figure import Figure
fig=Figure()
#canvas=Figure.Canvas(fig) #-----pasando el objeto de la capa del artista a la capa del fondo (Figure Canvas)

#— — — — — — — — — — — — -Usando numpy para crear variables aleatorias----------------------
import numpy as np
x=np.random.rand(100)

#— — — — — — — — — — — — -Trazando un histograma---------------------
ax=fig.add_subplot(111)
ax.hist(x,100)
ax.set_title('Normal Distribution')
fig.savefig('matplotlib_histogram.png')


# Podemos ver que para trazar un histograma de números aleatorios usando una combinación de fondo y capa de artista, necesitamos trabajar en múltiples líneas del fragmento de código. Para reducir este esfuerzo, Matplotlib introdujo la capa de guión llamada Pyplot.

"matplotlib.pyplot" #es una colección de funciones de estilo de comando que hacen que matplotlib funcione como MATLAB. Cada función pyplot realiza algunos cambios en una figura, por ejemplo, crea una figura, crea un área de trazado en una figura, traza algunas líneas en un área de trazado, decora el trazado con etiquetas, etc. En matplotlib.pyplot se conservan varios estados a través de las llamadas de función de manera que se mantiene un registro de cosas como la figura actual y el área de trazado, y las funciones de trazado se dirigen a los ejes actuales.


import matplotlib.pyplot as plt
#— — — — — — — — — — — — -Using numpy to create random variables----------------------
import numpy as np
x=np.random.rand(100)
plt.hist(x,100) #-----100 refers to the number of bins
plt.title("Normal distribution Graph")
plt.xlabel("Random numbers generated")
plt.ylabel("Density")
plt.show()

#La misma salida puede ser generada directamente a través de pyplot usando menos líneas de código.