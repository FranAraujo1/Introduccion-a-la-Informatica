import pandas as pd

personas =  pd.read_csv("/Users/frana/Documents/UCEMA Programación/Teoría/Introduccion-a-la-Informatica/Práctica Ciencia de Datos/Teoría - ANA/Ciencia de Datos/Análisis datos con pandas/personas_2011_cyt.csv", sep=";")
conicet = pd.read_csv("/Users/frana/Documents/UCEMA Programación/Teoría/Introduccion-a-la-Informatica/Práctica Ciencia de Datos/Teoría - ANA/Ciencia de Datos/Análisis datos con pandas/ref_categoria_conicet.csv", sep=";")

'''print(personas)
print(personas['persona_id'])
print(conicet)'''

pers = pd.concat([personas["persona_id"], personas["anio"], personas["categoria_conicet_id"]],axis=1)
print(pers)

'''mergePers = pd.merge(pers, conicet, how='inner',left_on="persona_id", right_on = "categoria_conicet_id")
print(mergePers)


pers2 = pd.concat([personas["persona_id"], personas["anio"]], axis=1)
print(pers2)

print(pd.merge(pers2, conicet,how='right', left_on="persona_id", right_on = "categoria_conicet_descripcion"))'''

print(pd.merge(pers, conicet,how="outer", on = "categoria_conicet_id"))
print(pd.merge(pers, conicet,how="inner", on = "categoria_conicet_id"))