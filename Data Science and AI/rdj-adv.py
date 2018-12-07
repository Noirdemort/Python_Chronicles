from sklearn.svm import LinearSVC, SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

import numpy as np
import cv2
import numpy, os
from tqdm import tqdm
import pickle
import csv

#from sklearn.metrics import classification_report
#from sklearn.metrics import confusion_matrix
#from sklearn.cross_validation import train_test_split
#from sklearn.grid_search import GridSearchCV
#from sklearn.decomposition import RandomizedPCA

path = "./train"
test = "./test"

#Flat image Feature Vector
x=[]
#Int array of Label Vector
y=[]


conv_dict = {'dog':1, 'cat':0}

for file in tqdm(os.listdir(path)):
    try:
        img = cv2.imread(path+'/'+file, cv2.IMREAD_GRAYSCALE)
        p = img.shape
        img = cv2.resize(img,(60,60))
        featurevector=np.array(img).flatten()
        label = list(file.split('.'))
        y.append(conv_dict[label[0]])
        x.append(featurevector)
    except Exception as e:
        print(e)

x = np.array(x)
y = np.array(y)

predict_x = []

for file in tqdm(os.listdir(test)):
    img = cv2.resize(cv2.imread(test+'/'+file, cv2.IMREAD_GRAYSCALE),(60,60))
    featurevector=np.array(img).flatten()
    predict_x.append(featurevector)
    
predict_x = np.array(predict_x,dtype=np.float64)

clf = RandomForestClassifier(max_depth=20, random_state=0)

print('started training')
clf.fit(x,y)

#
#with open('trained.pickle','wb') as f:
#    pickle.dump(clf,clf)
#
##f = open('trained.pickle','r')
##clf = pickle.load(f)

print()
print('started writing file')
file = open('write_me_adv.csv','w')
sqd = csv.writer(file,delimiter=',')

predict_x = predict_x.reshape(len(predict_x),-1)
prediction = clf.predict(predict_x)
sqd.writerow(['id','label'])

for i in tqdm(range(len(prediction))):
    sqd.writerow([i+1,prediction[i]])
file.close()

print('started scoring')
print('Accuracy = {}'.format(clf.score(x,y)))

