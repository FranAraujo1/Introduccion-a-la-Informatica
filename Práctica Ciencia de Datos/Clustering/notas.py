import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

path = '/Users/frana/Documents/UCEMA Programación/iris_data.txt'
iris = pd.read_csv(path, sep = '\t')

scaler = StandardScaler()
iris_escaleado = scaler.fit_transform(iris)

k = 3  #definimos la cantidad de clusters
kmeans = KMeans(n_clusters = k, init="random", n_init=10, max_iter=300, random_state=123457) #tomamos los centroides de forma aleatoria y definimos un máximo de 300 iteraciones
kmeans.fit(iris_escaleado) #aplicamos el método a nuestros datos
print(kmeans)



# La asignación de cada punto a un cluster se obtiene el atributo labels_ del objeto clusters, esta propiedad me dice que etiqueta le puso a cada uno de mis datos.
print(kmeans.labels_)

# Los centroides pueden ser obtenidos con cluster_centers_:
kmeans.cluster_centers_


#Para entender mejor los resultados obtenidos grafiquemos la distribución de puntos, pintando cada punto según el color correspondiente al etiquetado
colores = ["red", "green", "blue"]
g = sns.scatterplot(x = iris_escaleado[:,2], y = iris_escaleado[:, 3], hue = kmeans.labels_, palette = colores, alpha = 0.5)
plt.show()


'''g = sns.scatterplot(x = kmeans.cluster_centers_[:,2], y = kmeans.cluster_centers_[:,3], zorder = 10, palette = colores, hue = [0, 1, 2], legend = False, marker=6, s=200)

plt.show()'''


