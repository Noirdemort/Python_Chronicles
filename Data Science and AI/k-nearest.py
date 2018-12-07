# K clustering program

import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import pickle

df = pd.read_csv('breast-cancer-wisconsin.data', sep=",")
df.replace('?',-99999,inplace=True)
df.columns = ['id','clump thickness','unif cell size','unif cell shape','marg adhesion','single epith cell size','bare nuclei','bland chrom','norm nucleoli','mitoses','class']
ids = df.id
df.drop(['id'],1,inplace=True)
ids.dropna(inplace=True)
x = np.array(df.drop(['class'],1))
y = np.array(df['class'])

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)

clf = neighbors.KNeighborsClassifier() # n-jobs available for this.
clf.fit(x_train, y_train)

accuracy = clf.score(x_test,y_test)
print(accuracy)

#now to make prediction

example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,2,1,2,3,2,1]])
example_measures = example_measures.reshape(len(example_measures),-1)
print(example_measures)

prediction = clf.predict(example_measures)
print(prediction)

# add code for visualization
k_means = KMeans(n_clusters=2)
k_means.fit(x)
print(k_means.cluster_centers_)
print(len(y), len(x))
plt.scatter(range(len(y)),y, c=k_means.labels_, cmap='rainbow')
plt.show()

