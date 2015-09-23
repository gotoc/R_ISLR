# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 05:54:40 2015

@author: Di
"""

from sklearn.datasets import load_diabetes
diabetes=load_diabetes()
X,y=diabetes.data, diabetes.target

import pandas as pd
pd.options.display.float_format='{:.2f}'.format 
df = pd.DataFrame(X)
print df.describe()
            #Basic description tells you who's the outlier, the max/min far from 75%/25%
box_plots=df.boxplot()
            #boxplot also shows the outlier
from sklearn.preprocessing import StandardScaler
Xs=StandardScaler().fit_transform(X)
o_idx=np.where(np.abs(Xs)>3)
print df[(np.abs(Xs)>3).any(1)]
 #Convert the dataset into Gaussian distribution, showing outliers

#*****************Using PCA to detect outlier****************************
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from pandas.tools.plotting import scatter_matrix

dim_reduction=PCA()
Xc=dim_reduction.fit_transform(scale(X))
print 'variance explained by first 2 components %0.1f'%(sum(dim_reduction.explained_variance_ratio_[-2:]* 100))
df = pd.DataFrame(Xc, columns =['comp_' + str(j+1) for j in range(10)])
first_two = df.plot(kind ='scatter', x ='comp_1', y ='comp_2', c ='DarkGray', s = 50) 
last_two = df.plot( kind ='scatter', x ='comp_9', y ='comp_10', c ='DarkGray', s = 50)
outlying=(Xc[:,-1] < -0.3) | (Xc[:,-2] < -1.0) 
print df[outlying] #Print outliers found out by PCA

#**************************Using Cluster Analysis***************************
from sklearn.cluster import DBSCAN
DB=DBSCAN(eps=2.5, min_samples=25, random_state=101)
DB.fit(Xc)
from collections import Counter
print Counter (DB.labels_),'\n'
print df[DB.labels_==-1]
Counter({0:414,-1:28})
#*************************Using OneClassSVM******************************
from sklearn import svm
outliers_fraction =0.01 
nu_estimate=0.95*outliers_fraction+0.05
auto_detection=svm.OneClassSVM(kernel="rbf", gamma=0.01,degree=3,nu=nu_estimate)
auto_detection.fit(Xc)
evaluation=auto_detection.predict(Xc)
print df[evaluation==-1]













