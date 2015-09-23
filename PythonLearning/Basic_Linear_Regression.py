# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 05:22:57 2015

@author: Di
"""

from sklearn.datasets import load_boston
boston=load_boston()
X,y=boston.data,boston.target
print X.shape, y.shape

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
regression=LinearRegression()
regression.fit (X,y)
print 'Mean squared error: %.2f'% mean_squared_error(y_true=y,y_pred=regression.predict(X))

#How to break the sample down to Train set and Test set, show mean squared error of both
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=5)
print X_train.shape, X_test.shape

regression.fit(X_train,y_train)
print 'Train mean squared error:%.2f' %mean_squared_error(y_true=y_train,y_pred=regression.predict(X_train))
print 'Test mean squared error: %.2f' %mean_squared_error(y_true=y_test,y_pred=regression.predict(X_test))

#****************************Cross_Validation****************************************
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold 
crossvalidation = KFold(n=X.shape[0], n_folds=10, shuffle=True, random_state=1) 
scores=cross_val_score(regression, X, y, scoring ='mean_squared_error', cv = crossvalidation, n_jobs = 1)
print 'Folds: %i, mean squared error: %.2f std: %.2f'%(len(scores), np.mean(np.abs(scores)), np.std(scores))

#K-fold validation


from sklearn.cross_validation import StratifiedKFold
stratification = StratifiedKFold(y=X[:,3],n_folds=10,shuffle=True, random_state=1)
scores=cross_val_score(regression, X, y, scoring ='mean_squared_error', cv = stratification, n_jobs = 1)
print 'Stratified: %i, folds cross validation mean' + 'squared error: %.2f std: %.2f' %(len(scores), np.mean(np.abs(scores)), np.std(scores))









