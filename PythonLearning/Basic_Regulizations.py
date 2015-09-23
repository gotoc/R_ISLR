# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:17:48 2015

@author: Di
"""
from sklearn.datasets import load_boston
from random import shuffle
import pandas as pd

boston=load_boston()
new_index=range(boston.data.shape[0])
shuffle(new_index)
X,y=boston.data[new_index],boston.target[new_index]
polyX=pd.DataFrame(X,columns=boston.feature_names)

############L2 Ridge regression ###make coefficients smaller, but never equal to zero##
import numpy as np
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import Ridge
ridge=Ridge(normalize=True)   
search=GridSearchCV(estimator=ridge,param_grid={'alpha': np.logspace(-5,2,8)}, scoring ='mean_squared_error', n_jobs = 1, refit = True, cv = 10)
search.fit(polyX,y)

print 'Best parameters: %s'% search.best_params_
print 'CV MSE of best parameters: %.3f'% abs(search.best_score_)

#############L1 Lasso#####reduce effect of less useful coefficients down towards zero###
from sklearn.linear_model import Lasso
lasso=Lasso(normalize=True)
search=GridSearchCV(estimator=lasso,param_grid={'alpha': np.logspace(-5,2,8)}, scoring ='mean_squared_error', n_jobs = 1, refit = True, cv = 10)
search.fit(polyX,y)
print 'Best parameters: %s'% search.best_params_
print 'CV MSE of best parameters: %.3f'% abs(search.best_score_)

lasso=Lasso(normalize=True,alpha=0.01)
lasso.fit(polyX,y)
print polyX.columns[np.abs(lasso.coef_)>0.0001].values
#Select a greater or lesser number of variables, setting alpha parameter to 0.01, obtaining a much simplified solution as result

from sklearn.linear_model import ElasticNet
elastic=ElasticNet(normalize=True)
search=GridSearchCV(estimator=elastic,param_grid={'alpha': np.logspace(-5,2,8)}, scoring ='mean_squared_error', n_jobs = 1, refit = True, cv = 10)
search.fit(polyX,y)
print 'Best parameters: %s' % search.best_params_ 
print 'CV MSE of best parameters: %.3f' % abs(search.best_score_)


##################Stochastic Gradient Descent##########################
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
SGD=SGDRegressor(loss='squared_loss', penalty='12', alpha=0.0001, l1_ratio=0.15,n_iter=2000)
scaling=StandardScaler()
scaling.fit(polyX)
scaled_X=scaling.transform(polyX)


######################Partial Fit####################
from sklearn.metrics import mean_squared_error
from sklearn.cross_validation import train_test_split
X_train, X_test,y_train,y_test=train_test_split(scaled_X,y,test_size=0.20,random_state=2)
SGD=SGDRegressor(loss='squared_loss', penalty='12', alpha=0.0001, l1_ratio=0.15,n_iter=2000)
improvements=list()
for z in range(1000):
    SGD.partial_fit(X_train,y_train)
    improvements.append(mean_squared_error(y_test,SGD.predict(X_test)))

import matplotlib.pyplot as plt
plt.subplot(1,2,1)
plt.plot(range(1,11),np.abs(improvements[:10]), 'o--')
plt.xlabel('Partial fit initial iterations')
plt.ylabel('Test set mean squared error')
plt.subplot(1,2,2)
plt.plot(range(100,1000,100),np.abs(improvements[100:1000:100]),'o--')
plt.xlabel('Partial fit ending iterations')
plt.show()


