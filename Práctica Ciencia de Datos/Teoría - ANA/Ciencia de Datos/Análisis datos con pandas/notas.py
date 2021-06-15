import pandas as pd
personas =  pd.read_csv("/Users/frana/Documents/UCEMA Programación/Teoría/Introduccion-a-la-Informatica/Práctica Ciencia de Datos/Teoría - ANA/Ciencia de Datos/Análisis datos con pandas/personas_2011_cyt.csv", sep=";")
personas.head()

print(personas.info()) # Como verás esta es una descripción genérica de nuestro DataFrame, de la cuál podemos obtener el nombre de cada columna (variable),
                       # el tipo de datos correspondiente a cada una de ellas, y cuántas filas por columna poseen información.
                       # Sin embargo, el análisis de los datos implica hacernos preguntas sobre la información que estos contienen e 
                       # intentar encontrar respuestas, dentro de lo posible que sean generalizables. Aquí es donde entra en juego 🥁...¡Si: La estadística!

print(personas.describe()) # no sabemos que es el count

print(personas['maximo_grado_academico_id'].value_counts()) # nos devuelve la cantidad de veces que ser repite cierta "cosa" en la columna

print(personas.isnull().sum()) # devuelve cantidad de nulls de una columna


print(personas.dropna(inplace=True)) # es por fila  

print(personas.dropna(thresh=2, inplace=True)) # es por fila

print(personas.drop(['maximo_grado_academico_id'], axis=1, inplace=True))

print(personas.fillna(personas['columna_con_faltantes'].mean(), inplace=True)) # En columna_con_faltantes pongo el nombre de la columna que quiero completar con "mean"

print(personas.fillna(personas['columna_con_faltantes'].mode(), inplace=True)) # En columna_con_faltantes pongo el nombre de la columna que quiero completar con "mode"

print(personas.fillna(personas['columna_con_faltantes'].median(), inplace=True)) # En columna_con_faltantes pongo el nombre de la columna que quiero completar con "median"


print(personas['anio'].dtypes) # Devuelve el dataType 

print(personas.describe())
print(len(personas))

personas['edad'] = pd.to_numeric(personas['edad'], errors='coerce')
print(personas['edad'])

print(personas.drop_duplicates(inplace=True))
