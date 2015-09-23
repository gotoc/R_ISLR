# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:31:24 2015

@author: Di
"""

import numpy as np
from sklearn.datasets import load_boston
from random import shuffle

boston=load_boston()
new_index=range(boston.data.shape[0])
shuffle(new_index)
X,y=boston.data[new_index],boston.target[new_index]
print x.shape, y.shape

import pandas as pd
df=pd.DataFrame(X,columns=boston.feature_names)
df['target']=y

scatter = df.plot(kind ='scatter', x ='LSTAT', y ='target', c ='r')

#########Measure the cross-validation score of pair of each compoenents
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
regression=LinearRegression(normalize=True)
crossvalidation=KFold(n=X.shape[0],n_folds=10,shuffle=True,random_state=1)

df=pd.DataFrame(X,columns=boston.feature_names)
baseline=np.mean(cross_val_score(regression,df,y,scoring='r2',cv=crossvalidation, n_jobs=1))
interactions=list()
for feature_A in boston.feature_names:
    for feature_B in boston.feature_names:
        if feature_A>feature_B:
            df['interaction']=df[feature_A]*df[feature_B]
            score=np.mean(cross_val_score(regression,df,y,scoring='r2',cv=crossvalidation,n_jobs=1))
            if score>baseline:
                interactions.append((feature_A,feature_B,round(score,3)))
print 'Baseline R2: %.3f'% baseline
print 'Top 10 interactions: %s'% sorted(interactions,key=lambda(x):x[2], reverse=True)[:10]

#######Measure the cross-validation score of pair of PolyX Squared and y...........
polyX=pd.DataFrame(X,columns=boston.feature_names)
baseline=np.mean(cross_val_score(regression, polyX,y, scoring='mean_squared_error', cv=crossvalidation,n_jobs=1))
improvements=[baseline]
for feature_A in boston.feature_names:
    polyX[feature_A+'^2']=polyX[feature_A]**2
    improvements.append(np.mean(cross_val_score(regression,polyX,y,scoring='mean_squared_error',cv=crossvalidation,n_jobs=1)))
    for feature_B in boston.feature_names:
        if feature_A>feature_B:
            polyX[feature_A+'*'+feature_B]=polyX[feature_A]*polyX[feature_B]
            improvements.append(np.mean(cross_val_score(regression,polyX,y,scoring='mean_squared_error', cv=crossvalidation,n_jobs=1)))
crossvalidation=KFold(n=X.shape[0],n_folds=10,shuffle=True,random_state=1)
print 'Mean Squared error %.3f'% abs(np.mean(cross_val_score(regression,polyX,y,scoring='mean_squared_error',cv=crossvalidation,n_jobs=1)))
