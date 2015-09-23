# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 05:16:55 2015

@author: Di
"""
import pandas as pd
pd.options.display.float_format='{:.2f}'.format 
df = pd.DataFrame(X)

from sklearn.datasets import load_diabetes
diabetes=load_diabetes()
X,y=diabetes.data, diabetes.target

from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from pandas.tools.plotting import scatter_matrix

dim_reduction=PCA()
Xc=dim_reduction.fit_transform(scale(X))

from sklearn import svm
outliers_fraction =0.01 
nu_estimate=0.95*outliers_fraction+0.05
auto_detection=svm.OneClassSVM(kernel="rbf", gamma=0.01,degree=3,nu=nu_estimate)
auto_detection.fit(Xc)
evaluation=auto_detection.predict(Xc)
print df[evaluation==-1]

#gamma=whether to follow or approximate dataset distribution, for outlier detection, better to use <0
#nu_estimate=0.95*f+0.05, f is percentage of expected outliers
