import pandas as pd
import seaborn as sns
import scipy.stats as ss 

personas =  pd.read_csv("/Users/frana/Documents/UCEMA Programación/Teoría/Introduccion-a-la-Informatica/Práctica Ciencia de Datos/Teoría - ANA/Ciencia de Datos/Análisis datos con pandas/personas_2011_cyt.csv", sep=";")
categorias = pd.read_csv("/Users/frana/Documents/UCEMA Programación/Teoría/Introduccion-a-la-Informatica/Práctica Ciencia de Datos/Teoría - ANA/Ciencia de Datos/Análisis datos con pandas/ref_categoria_conicet.csv")
personas_cat = pd.merge(personas, categorias, on='categoria_conicet_descripcion')

print(personas)
print(categorias)
print(personas_cat)

#personas.to_csv(path_al_arch, index=False, header=True)


