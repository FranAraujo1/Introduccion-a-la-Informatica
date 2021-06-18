import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

path = '/Users/frana/Documents/UCEMA Programación/iris_data.txt'
iris = pd.read_csv(path, sep = '\t')

scaler = StandardScaler()
iris_escaleado = scaler.fit_transform(iris)

k = 0
datos = {"K": [], "Inercia":[]}
valoresDeK = []
inercias = []

while k < 10:
    k += 1
    kmeans = KMeans(n_clusters = k, init="random", n_init=10, max_iter=300, random_state=123457) #tomamos los centroides de forma aleatoria y definimos un máximo de 300 iteraciones
    kmeans.fit(iris_escaleado) #aplicamos el método a nuestros datos
    inercia = kmeans.inertia_
    valoresDeK.append(k)
    inercias.append(inercia)

datos["K"] = valoresDeK
datos["Inercia"] = inercias

datosDataFrame = pd.DataFrame(datos)
print(datosDataFrame)

datosDataFrame = sns.pointplot(data = datosDataFrame, x = "K", y = "Inercia")
print(datosDataFrame)
plt.show()



    






