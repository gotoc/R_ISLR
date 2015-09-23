# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
boston=load_boston()
X,y=boston.data,boston.target
hypothesis=LinearRegression(normalize=True)
hypothesis.fit(X,y)
print X.shape, y.shape   #Print the dimension of the arrays
print hypothesis.coef_     
print hypothesis.score(X,y)  #Score returns the R-square comparing predictor to a simple mean
                                #High R-square means predictor is working well


#------------------Transform Preprocessing--------------------
import numpy as np
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
scaler.fit(X)
new_observation = np.array( [1,0,1,0,0.5,7,59,6,3,200,20,350,4], dtype = float)
print scaler.transform(new_observation)

