import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = '/Users/frana/Documents/UCEMA Programación/iris_data.txt'
iris = pd.read_csv(path, sep = '\t')
#g = sns.histplot(data = iris, x = "sepal.length", binwidth=0.25, kde = True, color= 'orange')

g = sns.pairplot(iris)

print(g)
plt.show()

