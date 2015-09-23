# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:23:07 2015

@author: Di
"""

from sklearn.datasets import load_digits
digits=load_digits()
X,y=digits.data,digits.target
from sklearn.svm import SVC
from sklearn.cross_validation import cross_val_score

# %timeit single_core_learning=cross_val_score(SVC(),X,y, cv=20,n_jobs=1)
# %timeit multi_core_learning=cross_val_score(SVC(),X,y,cv=20,n_jobs=-1)
# using n_jobs=-1, deploy all the necessary instances of CPU, n_jobs=1, 
   # using only one instance
