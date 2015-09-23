# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:10:33 2015

@author: Di
"""
from sklearn.datasets import load_digits
digits=load_digits()
X=digits.data
ground_truth=digits.target

from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
pca=PCA(n_components=40)
Cx=pca.fit_transform(scale(X))
print 'Explained vairance %0.3f' % sum(pca.explained_variance_ratio_)

#***************************K-means***Need to guess how many clusters (K)***********************************
from sklearn.cluster import KMeans
clustering=KMeans(n_clusters=10, n_init=10, random_state=1) #Core function of K-means
clustering.fit(Cx)  #Core function of clustering

import numpy as np
import pandas as pd
ms=np.column_stack((ground_truth, clustering.labels_)) 
df=pd.DataFrame(ms, columns = ['Ground truth','Clusters']) 
print (pd.crosstab(df['Ground truth'], df['Clusters'], margins=True))

inertia=list()
delta_inertia=list()
for k in range(1,21): 
    clustering = KMeans(n_clusters = k, n_init = 10, random_state = 1) 
    clustering.fit(Cx)
    if inertia: # So we won't compare the solution k = = 1 
        delta_inertia.append(inertia[-1] - clustering.inertia_) #compare inertia of different clustering
    inertia.append(clustering.inertia_)

import matplotlib.pyplot as plt 
plt.figure()
plt.plot([k for k in range(2,21)],delta_inertia, 'ko-')
plt.xlabel('Number of clusters')
plt.ylabel('Range of change of inertia')
plt.show()             #Show the inertia and its explanatory power
#Inertia is the sum of all differences between every cluster member and its centroid
#If goups are similar, inertia would be small
#If the rate jumps up, it means that adding a cluster more than the previous solution brings much more benefit than expected;

#***********************DBScan*******No need to guess K clusters numbers**********
from sklearn.cluster import DBSCAN
DB=DBSCAN(eps=4.35,min_samples=25,random_state=1)  #DBSCAN core function
DB.fit(Cx)                         #DBSCAN core function 

#eps: maximum distance between 2 observations;
#min_sample: minimum number of observations in a neighborhood that transform into a core point
from collections import Counter
print Counter(DB.labels_)

import matplotlib.pyplot as plt
for k,cl in enumerate (np.unique(DB.labels_)):
    if cl>=0:
        example=np.min(np.where(DB.labels_==cl))
        plt.subplot(2,3,k)
        plt.imshow(digits.images[example],cmap ='binary', interpolation ='none') 
        plt.title('cl'+ str(cl))
plt.show()
ms=np.column_stack((ground_truth,DB.labels_))
df = pd.DataFrame(ms, columns = ['Ground truth','Clusters'])
print(pd.crosstab( df['Ground truth'], df['Clusters'], margins = True))




 
