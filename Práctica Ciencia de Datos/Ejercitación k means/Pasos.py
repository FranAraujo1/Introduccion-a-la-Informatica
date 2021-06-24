# %matplotlib inline
import pandas as pd #Pandas para usar dataframes
import matplotlib.pyplot as plt #Para graficar
'''import matplotlib.cm as cm #Para graficar el silhouette'''
import seaborn as sns #Para graficar
'''import numpy as np #Para realizar operaciones númericas con matrices y arrays
from sklearn import datasets #sklearn es LA biblioteca de machine learning de python
from sklearn.cluster import KMeans, DBSCAN #Para usar kmeans
from sklearn.preprocessing import StandardScaler #Para estandarizar nuestros datos
from sklearn.metrics import silhouette_samples, silhouette_score #Para el coeficiente de silhouette
from sklearn.cluster import AgglomerativeClustering #Para clustering jerárquico
from sklearn.metrics import pairwise_distances #Para las distancias a pares
from scipy.cluster.hierarchy import dendrogram, cophenet, linkage #Para graficar los dendrogramas y calcular el coeficiente cofenetico
from scipy.cluster import hierarchy #Para graficar los dendrogramas
from scipy.spatial.distance import pdist #Para calcular la distancia con el coeficiente cofenetico
import community as community_louvain #Para louvain
import networkx as nx #Para grafos'''

path = '/Users/frana/Documents/UCEMA Programación/Teoría/Introduccion-a-la-Informatica/dataset_clustering_teorico.csv'

stock_data = pd.read_csv(path)
stock_data.head()
print(stock_data)
print(stock_data.columns)

# CARACTERIZACIÓN


# nos devuelve la cantidad de NaN x columna

print(stock_data.isnull().sum())
print(stock_data.dropna(inplace=True))

# Más información
print(stock_data.describe())
print(stock_data.info(max_cols=1000))

# Gráfico
f = sns.histplot(data = stock_data, x = "2010-01-04", binwidth=0.25, kde = True, color= 'orange')
print(f)
#plt.show()

#Nan # duplicados # outlayers

# Rellenamos los 'espacios' de las columnas donde había nulls con la media
print(stock_data.fillna(stock_data['2010-01-07'].mean(), inplace=True)) 
print(stock_data.fillna(stock_data['2013-10-23'].mean(), inplace=True))

# Filtramos los valores 
df2 = stock_data.sort_values(by = ["2013-10-29"], ascending = False, ignore_index = True).head(10)
print(df2)


# Normailzar los datos y guardalos en una variable stock_data_normalizado

stock_data_normalizado = 

# cuantiles
Q1 = stock_data['2010-01-04'].quantile(0.07) # -0.4435993499999751
Q2 = stock_data['2010-01-04'].quantile(0.93) # 0.9708959100000023

# 
outliers = df[df[col] > df[col].mean() + 3 * df[col].std()]
outliers = df[df[col] < df[col].mean() - 3 * df[col].std()]

# la normalización sirve para trabajar mejor con los datos, perdes un poco la identidad de los mismos

scaler = StandardScaler()
stock_data_normalizado = scaler.fit_transform(stock_data)

# siempre hacer un test - 
# si es mayor a 0,005 es normal

'''k = 14  #definimos la cantidad de clusters
kmeans = KMeans(n_clusters = k, init="random", n_init=10, max_iter=300, random_state=123457) #tomamos los centroides de forma aleatoria y definimos un máximo de 300 iteraciones
kmeans.fit() #aplicamos el método a nuestros datos
print(kmeans)'''





