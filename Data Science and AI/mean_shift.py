import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from sklearn.cluster import MeanShift
from sklearn import preprocessing, cross_validation
import pandas as pd
import math, random
style.use('ggplot')

df = pd.read_csv('ship-train.csv')
ids = df.PassengerId
sdm = ['A','B','C','D','E','F','G']
df.drop(['PassengerId','Name','Ticket'],1,inplace=True)
df.Sex = df['Sex'].map({'male':0, 'female':1})
df.Embarked = df['Embarked'].map({'S':1, 'Q':0, 'C':2})
df['Cabin'].fillna(random.choice(sdm),inplace=True)
df.fillna('1',inplace=True)
for i in range(len(df)):
    df.Cabin.loc[i] = ord(str(df.Cabin.loc[i])[0])%65

df1 = pd.read_csv('ship-test.csv')
df1.drop(['Name','Ticket'],1,inplace=True)


df1.Sex = df1['Sex'].map({'male':0, 'female':1})
df1.Embarked = df1['Embarked'].map({'S':1, 'Q':0, 'C':2})

for i in range(len(df1)):
    df1.Cabin.loc[i] = random.randint(0,7)

df1.fillna('1',inplace=True)

# for conversion to float
for i in df.columns:
    df[i] = df[i].astype(np.float64)

for i in df1.columns:
    df1[i] = df1[i].astype(np.float64)

x = np.array(df.drop(['Survived'],1))
x = preprocessing.scale(x)
y = np.array(df['Survived'])

clf = MeanShift()
clf.fit(x)

labels = clf.labels_
cluster_centers = clf.cluster_centers_
odf = pd.DataFrame.copy(df)

odf['cluster_group'] = np.nan
for i in range(len(x)):
    odf['cluster_group'].iloc[i] = labels[i]

n_clusters_ = len(np.unique(labels))

survival_rates = {}
for i in range(n_clusters_):
    temp_df = odf[ odf['cluster_group']==float(i) ]
    survival_cluster = temp_df[ temp_df['Survived']==1 ]
    survival_rate = len(survival_cluster)/len(temp_df)
    survival_rates[i] = survival_rate

print(survival_rate)
