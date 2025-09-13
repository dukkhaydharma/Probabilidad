
#*Probabilidad y estadistica*

#* **Unidad

### *Practica 2. Máximo, minino, Rango y dispersión de datos.*

### Docente: Dr. Jose Gabriel Rodriguez Rivas*

### ALumno：Leos Lazcano Cristian Mauricio
import seaborn as sns
import random
import matplotlib.pyplot as plt
from statistics import *

fabrica1 = []
for i in range(100):
    numero_aleatorio = round( random.uniform(50, 100), 2 )
    fabrica1.append(numero_aleatorio)
   

maximo1 = max(fabrica1)
minimo1 = min(fabrica1)
rango1 = maximo1 - minimo1
media1 = mean(fabrica1)
mediana1 = median(fabrica1)
moda1 = mode(fabrica1)

print ( "Estadística descriptiva de la Fábrica #1 \n", "Media =", media1, "\n Mediana =", mediana1, "\n Moda =", moda1, "\n Maximo = ", maximo1, "\n Minimo =",minimo1, "\n Rango =", rango1)
print()









fabrica2 = []
for i in range(100):
    numero_aleatorio = round( random.uniform(50, 100), 2 )
    fabrica2.append(numero_aleatorio)

maximo2= max(fabrica2)
minimo2 = min(fabrica2)
rango2 = maximo2 - minimo2
media2 = mean(fabrica2)
mediana2 = median(fabrica2)
moda2 = mode(fabrica2)
    
print ( "Estadística descriptiva de la Fábrica #2 \n", "Media =", media2, "\n Mediana =", mediana2, "\n Moda =", moda2, "\n Maximo = ", maximo2, "\n Minimo =",minimo2, "\n Rango =", rango2)
print()
desviacion_estandar_fabrica1 = stdev(fabrica1)
print("Desviación estándar de la fábrica 1: ",desviacion_estandar_fabrica1)

desviacion_estandar_fabrica2 = stdev(fabrica2)
print("Desviación estándar de la fábrica 2: ",desviacion_estandar_fabrica2)

plt.figure(figsize= (8,6))
plt.hist(fabrica2, bins=10, alpha=0.2, color='b', edgecolor = "black")
plt.axvline(media2, color='b', linestyle='dashed', linewidth=2, label=f'Media={mediana2:.2f}')
plt.axvline(mediana2, color='r', linestyle='dashed', linewidth=2, label=f'Mediana={mediana2:.2f}')
plt.axvline(moda2, color='y', linestyle='dashed', linewidth=2, label=f'Moda={moda2:.2f}')

plt.axvline(media2 - desviacion_estandar_fabrica2, color='black', linestyle='dashed', linewidth=2, label=f'Desv. Estándar ={desviacion_estandar_fabrica2:.2f}')
plt.axvline(media2 + desviacion_estandar_fabrica2, color='black', linestyle='dashed', linewidth=2)

plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title("Producción diaria de la fábrica #2")
plt.legend
plt.show()




plt.figure(figsize= (8,6))
plt.hist(fabrica1, bins=10, alpha=0.2, color='b', edgecolor = "black")
plt.axvline(media1, color='b', linestyle='dashed', linewidth=2, label=f'Media={mediana1:.2f}')
plt.axvline(mediana1, color='r', linestyle='dashed', linewidth=2, label=f'Mediana={mediana1:.2f}')
plt.axvline(moda1, color='y', linestyle='dashed', linewidth=2, label=f'Moda={moda1:.2f}')

plt.axvline(media1 - desviacion_estandar_fabrica1, color='black', linestyle='dashed', linewidth=2, label=f'Desv. Estándar ={desviacion_estandar_fabrica2:.2f}')
plt.axvline(media1 + desviacion_estandar_fabrica1, color='black', linestyle='dashed', linewidth=2)

plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title("Producción diaria de la fábrica #1")
plt.legend
plt.show()


sns.histplot(x = fabrica1, kde = True, kde_kws = {'bw_adjust': 0.5}, bins=10)
sns.histplot(x = fabrica2, kde = True, kde_kws = {'bw_adjust': 0.5}, bins=10)