from os import path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = '/Users/frana/Documents/UCEMA Programación/Datos.csv'
datos = pd.read_csv(path)
print(datos)

# nos devuelve la cantidad de NaN x columna
print(datos.isnull().sum())
print(datos.dropna(inplace=True))



# rellenamos los 'espacios' de las columnas donde había nulls con la media
print(datos.fillna(datos['Sueldo'].mean(), inplace=True)) 
print(datos.fillna(datos['Altura'].mean(), inplace=True))

'''df2 = datos.fillna(datos['Sueldo'].mean(), inplace=True)
print(df2)

df3 = datos.fillna(datos['Altura'].mean(), inplace=True)
print(df3)'''

# sacamos diferentes valores
print(datos['Sueldo'].mean())
print(datos['Sueldo'].mode())
print(datos['Sueldo'].median())

print(datos['Altura'].median())
print(datos['Altura'].mean())
print(datos['Altura'].mode())


# filtramos el DataFrame x los que más ganan y los que más miden
df2 = datos.sort_values(by = ["Sueldo"], ascending = False, ignore_index = True).head(10)
print(df2)

df3 = datos.sort_values(by = ["Altura"], ascending = False, ignore_index = True).head(10)
print(df3)

# 
print(datos.drop_duplicates(inplace=True))

#
#g = sns.histplot(data = datos, x = "Altura", binwidth=0.25, kde = True, color= 'orange')
#print(g)
#plt.show()

f = sns.histplot(data = datos, x = "Sueldo", binwidth=0.25, kde = True, color= 'blue')
print(f)
plt.show()