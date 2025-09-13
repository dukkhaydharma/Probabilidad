#**Probabilidad y estadística**
## **Unidad 1**
###Practica 4. Tabla de frecuencias y regla de Sturges
### Docente: Dr. José Gabriel Rodríguez Rivas
### Alumno: Leos Lazcano Cristian Mauricio


import random
import matplotlib.pyplot as plt
from statistics import *

fabrica1 = []
for i in range(100):
    numero_aleatorio = round ( random.uniform(50, 100), 2 )
    fabrica1.append(numero_aleatorio)    

print(fabrica1)

fabrica2 = []
for i in range(100):
    numero_aleatorio = round ( random.uniform(40, 93), 2 )
    fabrica2.append(numero_aleatorio)

print(fabrica2)

plt.boxplot(fabrica1)
plt.ylabel('Producción en metros.')
plt.title('Producción de la fábrica 1')
plt.show()

plt.boxplot(fabrica2)
plt.ylabel('Producción en métros.')
plt.title('Producción de la fábrica 2')
plt.show()

fabrica1.append(150)
print(fabrica1)
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))
bplot1 = ax1.boxplot(fabrica1, vert = True, patch_artist = True)
ax1.set_title('Producción fábrica 1')

fabrica2.append(150)
print(fabrica2)
bplot2 = ax2.boxplot(fabrica2, vert = True, patch_artist = True)
ax1.set_title('Producción fábrica 2')

plt.show()

