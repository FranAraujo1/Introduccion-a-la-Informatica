import pandas as pd

path = '/Users/frana/Documents/UCEMA Programación/iris_data.txt'
iris = pd.read_csv(path, sep = '\t')
print(iris)
# Las columnas que devuelve son 'sepal.lenght, sepal.width, petal.length, petal.width'

print(iris.info())
print(iris.describe())
iris['sepal.lenght'].median()
