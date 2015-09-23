# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 05:54:09 2015

@author: Di
"""

from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
digits=load_digits()
pca=PCA(n_components=25)
pca.fit(digits.data[:1700,:])
X,y=pca.transform(digits.data[:1700,:]),digits.target[:1700]
tX,ty=pca.transform(digits.data[1700:,:]),digits.target[1700:]  #PCA to reduce dimensions

from sklearn.neighbors import KNeighborsClassifier
kNN = KNeighborsClassifier(n_neighbors = 5) 
kNN.fit(X, y)
print 'Accuracy: %.3f' % kNN.score(tX, ty) 
print 'Prediction: %s actual: %s' % (kNN.predict(tX[: 10,:]), ty[: 10])


#How to set K
for k in [1,5,10,100,200]:
    kNN=KNeighborsClassifier(n_neighbors = k).fit(X, y) 
    print 'for k = %3i accuracy is %.3f' % (k, kNN.score(tX, ty))

#small k: consider more homogeneous pool of neighbors but can easily make errors
#bigger k: consider more cases at a higher risk of observing neighbors too far
#Try different number, start from the low and try upward 

