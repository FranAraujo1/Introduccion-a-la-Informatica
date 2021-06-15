#  Obtener las 10 personas con mayor edad y generar un nuevo DataFrame con la información de el id de la persona,
#  el año, su edad, el id de la categoría conicet y las producciones académicas de los últimos 4 años. Unirlo con el DataFrame
#  conicet y en base a ese generar una tabla con el id de la persona
#  y la descripción de la categoría en conicet. Luego guardar este último DataFrame en un archivo.

import pandas as pd

personas =  pd.read_csv("/Users/frana/Documents/UCEMA Programación/Teoría/Introduccion-a-la-Informatica/Práctica Ciencia de Datos/Teoría - ANA/Ciencia de Datos/Análisis datos con pandas/personas_2011_cyt.csv", sep=";")
conicet = pd.read_csv("/Users/frana/Documents/UCEMA Programación/Teoría/Introduccion-a-la-Informatica/Práctica Ciencia de Datos/Teoría - ANA/Ciencia de Datos/Análisis datos con pandas/ref_categoria_conicet.csv", sep=";")

# Encontrar las 10 personas con mayor edad 


print(personas.sort_values(by = ["edad"], ascending = False) .head(10))

df2 = personas.sort_values(by = ["edad"], ascending = False) .head(10)
print(df2)

df2 = personas.sort_values(by = ["edad"], ascending = False, ignore_index = True).head(10)




# Tiene que tener el id de la persona, el año, su edad, el id de la categoria conicet y las producciones academicas de los ultimos 4 años
pers = pd.concat([personas["persona_id"],personas['edad'], personas["anio"], personas["categoria_conicet_id"], personas['producciones_ult_4_anios']],axis=1)
print(pers)

df3 = pd.merge(pers, conicet,how="inner", on = "categoria_conicet_id")


# Generar una tabla con el id de la persona y la descripcion de la categoria conicet
df4 = pd.concat([df3['persona_id'],df3['categoria_conicet_descripcion']], axis=1)
print(df4)
df4.to_csv('NuevoDataFrame', index= False)




