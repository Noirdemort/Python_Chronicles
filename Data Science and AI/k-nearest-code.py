# k-nearest neighbor algorithm

# the k-nearest neighbor uses eculidean distance.

# it is calculated as given in eucled_dist.png

from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
import pandas as pd
import random
from collections import Counter
style.use('fivethirtyeight')

# a simple example
plot1 = [1,3]
plot2 = [2,5]

eucledian_dist = sqrt( (plot1[0]-plot2[0])**2 + (plot1[1]-plot2[1])**2 )
print(eucledian_dist)

dataset = { 'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}

new_feat = [5,7]

#[[plt.scatter(ii[0],ii[1],s=100,color=i) for ii in dataset[i]] for i in dataset]
#
#plt.show()

def k_nearest_nbr(data, predict,k=3):
    if len(data)>=k:
        warnings.warn('k is set to a value less than total voting groups, idiot!')
    distances = []
    for group in data:
        for features in data[group]:
            eucledian_dist = np.linalg.norm(np.array(features)-np.array(predict) )
            # the above is same as any eucledian distance
            distances.append([eucledian_dist, group])

    votes = [i[1] for i in sorted(distances)[:k]]
    #print( Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][1]/k

    return vote_result, confidence

#result = k_nearest_nbr(dataset, new_feat,k=3)
#print(result)
#
#[[plt.scatter(ii[0],ii[1],s=100,color=i) for ii in dataset[i]] for i in dataset]
#plt.scatter(new_feat[0],new_feat[1],color=result)
#plt.show()

accuracies = []

for _ in range(25):
    df = pd.read_csv('breast-cancer-wisconsin.data')
    df.replace('?',-99999,inplace=True)
    df.drop(['1000025'],1,inplace=True)

    full_data = df.astype(float).values.tolist()
    random.shuffle(full_data)

    test_size = 0.2
    train_set = {2:[], 4:[]}
    test_set = {2:[], 4:[]}
    train_data = full_data[:-int(test_size*len(full_data))]
    test_data = full_data[-int(test_size*len(full_data)):]

    for i in train_data:
        train_set[i[-1]].append(i[:-1])

    for i in test_data:
        test_set[i[-1]].append(i[:-1])

    correct = 0
    total = 0

    for group in test_set:
        for data in test_set[group]:
            vote, confidence = k_nearest_nbr(train_set,data,k=5)
            if group == vote:
                correct+=1
            else:
                print(confidence)
            total+=1
    print("Accuracy = ",correct/total)
    accuracies.append(correct/total)

print('Avg accuracy = ', sum(accuracies)/len(accuracies))
