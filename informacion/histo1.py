import pandas as pd
import matplotlib.pyplot as plt
#Consiste en un CSV que contiene datos de un estudio realizado en la zona de Boston, 
#donde se analizan diferentes variables, como son el índice de crimen, el número de habitaciones,
#el porcentaje de habitantes de clase baje y el valor medio de las casas de esa zona. 
datos = pd.read_csv("casasboston.csv")
datos = datos[["RM","CRIM", "MEDV", "TOWN", "CHAS", "INDUS", "LSTAT"]]
df = datos[["RM","CRIM", "MEDV", "TOWN", "CHAS"]]
 
df = datos.rename(columns={
	"TOWN":"CIUDAD",
	"CRIM":"INDICE_CRIMEN",	
	"INDUS":"PCT_ZONA_INDUSTRIAL",
	"CHAS":"RIO_CHARLES",
	"RM":"N_HABITACIONES_MEDIO",
	"MEDV":"VALOR_MEDIANO",
	"LSTAT":"PCT_CLASE_BAJA"
})
 
print (df.sample(5))

#En el siguiente ejemplo deseamos ver la distribución de la cantidad media de habitaciones en el estudio realizado.
#df.N_HABITACIONES_MEDIO.plot.hist()
#plt.show()

#Otro ejemplo sería si deseamos ver la distribución del índice de crimen. Podemos utilizar bins para especificar la cantidad de grupos en los que deseamos distribuir los casos, y xlim para centrarnos en algunos grupos en específico.
#Python
#df.INDICE_CRIMEN.plot.hist(bins=100, xlim=(0,20))
#plt.show()
#1
#2
	
#df.INDICE_CRIMEN.plot.hist(bins=100, xlim=(0,20))
#plt.show()

#Gráfico de dispersión

#El gráfico de dispersión o scatter, sirve para representar la relación entre dos variables. Por ejemplo, si quisiésemos ver la relación entre índice de crimen y el valor mediano de las casas. En otras palabras, ¿el índice de crimen afecta el valor medio de las casas?
#df.plot.scatter(x="INDICE_CRIMEN", y="VALOR_MEDIANO", alpha=0.2)
#plt.show()
#1
#2
#El gráfico nos deja ver que a menor índice de crimen el valor mediano aumenta, por lo que pudiésemos concluir que ambos valores están correlacionados.

#Gráfico de barras

#Un gráfico de barras es útil para comparar una variable entre distintos grupos o categorías. Por ejemplo, si quisiéramos observar el valor medio de cada ciudad.

#Tenemos el valor medio de zonas dentro de una ciudad, así que la única forma de obtener el dato de la media de toda la ciudad, sería realizando una operación de agrupación. (Para más información sobre agrupación en Pandas consulta: Filtrado y uso de query con Pandas en Python).	
#El siguiente código agrupa por ciudad, y toma la media del valor_mediano. Después grafica las 10 primeras ciudades.
#Python
valor_por_ciudad = df.groupby("CIUDAD")["VALOR_MEDIANO"].mean()
valor_por_ciudad.head(10).plot.barh()
plt.show()
