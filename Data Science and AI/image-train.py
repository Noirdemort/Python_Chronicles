import pandas as pd
import numpy as np
from sklearn import preprocessing, svm, neighbors
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from tqdm import tqdm

df = pd.read_csv('image-train.csv')
df1 = pd.read_csv('image-test.csv')

for i in tqdm(df.columns):
    df[i] = df[i].astype(np.float64)

for i in tqdm(df1.columns):
    df1[i] = df1[i].astype(np.float64)

x = np.array(df.drop(['label'],1))
x = preprocessing.scale(x)
y = np.array(df.label)

clf = RandomForestClassifier(max_depth=14, random_state=0)
print('starting fitting')
clf.fit(x,y)
print('done fitting')
print(clf.score(x,y))

predict_x = np.array(df1)
predict_x = predict_x.reshape(len(predict_x),-1)
prediction = clf.predict(predict_x)

import csv
with open('upload-image.csv','w') as fp:
    sw = csv.writer(fp, delimiter=',')
    sw.writerow(['ImageId','Label'])
    for i in range(len(prediction)):
        sw.writerow([i+1,(prediction[i])])