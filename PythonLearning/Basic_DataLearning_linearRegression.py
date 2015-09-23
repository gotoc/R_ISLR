# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 05:29:51 2015

@author: Di
"""

from sklearn.datasets import load_boston
from sklearn.preprocessing import scale
boston=load_boston()
X,y=scale(boston.data),boston.target #Standardize the data is a good habit before Regression

from sklearn.linear_model import LinearRegression 
regression=LinearRegression()
regression.fit(X,y)

print regression.score(X,y)  #Score=R-square

#Limitation of linear regression 
#  1. Big impact from missing value
#  2. Outliers have big residual, forcing algo focus more on it
#  3. Most based on single coefficients, no complex relation like parabola
#  4. Can only do quantitative data Cannot deal with categories



#*****************Logistic Regression***********************************************
#Probability of a class = exp(r) / (1 + exp(r));
#r is the regression result;
#A regression using this formula to transfer result into probability is Logistic R
from sklearn.datasets import load_iris
iris=load_iris()
X,y=iris.data[:-1,:],iris.target[:-1]

from sklearn.linear_model import LogisticRegression 
logistic=LogisticRegression()
logistic.fit(X,y)
print 'Predicted class %s, real class %s' % (logistic.predict(iris.data[-1,:]), iris.target[-1])
print 'Probabilities for each class from 0 to 2: %s' % (logistic.predict_proba(iris.data[-1,:]))

#*******************Logistic Regression on multiClass*****************************
from sklearn.datasets import load_digits
digits=load_digits()
X,y=digits.data[:1700,:],digits.target[:1700]
tX,ty=digits.data[1700:,:],digits.target[1700:]

from sklearn.multiclass import OneVsRestClassifier 
from sklearn.multiclass import OneVsOneClassifier
OVR=OneVsRestClassifier(LogisticRegression()).fit(X,y) 
OVO=OneVsOneClassifier(LogisticRegression()).fit(X, y) 
print 'One vs rest accuracy: %.3f'% OVR.score(tX, ty)





















