# k-means flate clustering
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

x = np.array([ [1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9,11], [1,3], [8,9], [0,3], [5,4], [6,4] ])

#plt.scatter(x[:,0], x[:,1], s=150, linewidths=5)
#plt.show()

colors = 10*['g','r','c','b','k']

class K_Means:
    def __init__(self,k=2, tol=0.001, max_iter=500):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self,data):
        # pick starting centers
        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]
        
        # if true
        for i in range(self.max_iter):
            self.classifications = {}
            
            for i in range(self.k):
                self.classifications[i] = []
            # cycle through data and assign to class closest to it
            for featureset in data:
                # compare distance to either centroid
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                #print(distances)
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)
                # prev_centroids[classification] = self.centroid[centroid]
                
            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                # on first run don't do this ... but then add
                self.centroids[classification] = np.average(self.classifications[classification],axis=0)
            
            optimized = True
            
            for c in self.centroids:
                original_centroid  =  prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid-original_centroid)/original_centroid*100)>self.tol:
                    #print(np.sum((current_centroid-original_centroid)/original_centroid*100))
                    optimized=False
                    
                if optimized:
                    break

    def predict(self, data):
        # compare distance to either centroid
        distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
        # print(distances)
        classification = distances.index(min(distances))
        return classification

clf = K_Means()
clf.fit(x)

for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1], marker="o", color='k',s=150, linewidths=5)

for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0],featureset[1],marker='*',color=color, s=100, linewidths=3)

#unknowns = np.array( [[1,3], [8,9], [0,3], [5,4], [6,4] ])
#
#for u in unknowns:
#    classification = clf.predict(u)
#    plt.scatter(u[0],u[1],marker='.',color = colors[classification],s=150,linewidths=2)

plt.show()
