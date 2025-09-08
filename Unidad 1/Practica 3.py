#**Probabilidad y estadística**
## **Unidad 1**
###Practica 3. Tabla de frecuencias y regla de Sturges
### Docente: Dr. José Gabriel Rodríguez Rivas
### Alumno: Leos Lazcano Cristian Mauricio


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
