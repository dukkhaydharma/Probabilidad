#**Probabilidad y estadística**
## **Unidad 1**
###Practica 3. Tabla de frecuencias y regla de Sturges
### Docente: Dr. José Gabriel Rodríguez Rivas
### Alumno: Leos Lazcano Cristian Mauricio

import matplotlib.pyplot as plt
import random
edades = []

for i in range(100):
    numero_aleatorio = random.randint( 18, 70)
    edades.append(numero_aleatorio)

print(edades)

import pandas as pd

df = pd.DataFrame(edades, columns=['Edad'])
df.head()

tabla_frecuencias = df['Edad'].value_counts().reset_index()
tabla_frecuencias.columns = ['Edad', 'Frecuencia']
tabla_frecuencias = tabla_frecuencias.sort_values(by='Edad')

print("Tabla de Distribución de Frecuencias: ")
tabla_frecuencias

##Frecuencia Relativa
tabla_frecuencias['Frec. Relativa'] = tabla_frecuencias['Frecuencia'] / 100
tabla_frecuencias

##Calcular la frecuencia porcentual
tabla_frecuencias['Frec. Porcentual'] = tabla_frecuencias['Frecuencia'] / 100 * 100
tabla_frecuencias

##Calcular frecuencia acumulada
tabla_frecuencias['Frec. Acumulada'] = tabla_frecuencias['Frecuencia'].cumsum()
tabla_frecuencias

import math 
print(edades)

df = pd.DataFrame({'Edad': edades})
df

n = len(edades)
k = int( 1 + math.log2(n))
print("Valor de n: ", n , "Número de intérvalos: ", k)

tabla_frecuencias = pd.cut( df['Edad'], bins=k, include_lowest=True).value_counts().reset_index()
tabla_frecuencias.columns = ['Clase', 'Frec.']
tabla_frecuencias

tabla_frecuencias = tabla_frecuencias.sort_values(by='Clase')
tabla_frecuencias

tabla_frecuencias['Frec. Rel.'] = tabla_frecuencias['Frec.'] / n
tabla_frecuencias['Frec. Porc.'] = tabla_frecuencias['Frec.'] / n * 100
tabla_frecuencias['Frec. Acum.'] = tabla_frecuencias['Frec.'].cumsum()
tabla_frecuencias['Frec. Rel. Acum.'] = tabla_frecuencias['Frec. Rel.'].cumsum()
tabla_frecuencias['Frec. Porc. Acum.'] = tabla_frecuencias['Frec. Porc.'].cumsum()

print(tabla_frecuencias)

plt.hist(edades, alpha = 0.5)
plt.title("Histograma de edades basado en la función de matplotlib con valores estándar")

plt.hist(df['Edad'], bins=k, alpha = 0.5)
plt.title('Histograma de edades basado en la regla dew Sturges')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')


