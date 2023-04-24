import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('d:/hello-git/workspace/chap09/data/iris.csv')
print(iris.info())

plt.scatter(iris['Sepal.Length'], iris['Petal.Length'])
plt.show()

print(iris['Species'].unique())

species = []
for s in iris['Species'] :
    if s == 'setosa' :
        species.append(1)
    elif s == 'versicolor' :
        species.append(2)
    else :
        species.append(3)

plt.scatter(iris['Sepal.Length'], iris['Petal.Length'], c=species)

plt.show()