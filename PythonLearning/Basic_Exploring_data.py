# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:52:57 2015

@author: Di
"""

from sklearn.datasets import load_iris
iris=load_iris()

import pandas as pd
import numpy as np
print pd.__version__
print np.__version__
iris_nparray=iris.data
iris_dataframe=pd.DataFrame(iris.data, columns=iris.feature_names)
iris_dataframe['group']=pd.Series([iris.target_names[k] for k in iris.target],
dtype="category")
# print iris_dataframe.describe()
#print iris_dataframe.mean(numeric_only=True)
#print iris_dataframe.median(numeric_only=True)
#print iris_dataframe.std(numeric_only=True)

iris_binned=pd.concat([
pd.qcut(iris_dataframe.ix[:,0],[0,.25,.5,.75,1]),
pd.qcut(iris_dataframe.ix[:,1],[0,.25,.5,.75,1]),
pd.qcut(iris_dataframe.ix[:,2],[0,.25,.5,.75,1]),
pd.qcut(iris_dataframe.ix[:,3],[0,.25,.5,.75,1]),
],join='outer', axis=1)

# Use Pandas to break down the data into different quantile

#t-test compares two group at a time, but requires variance of each beforehand
from scipy.stats import ttest_ind
group0=iris_dataframe['group']=='setosa'
group1=iris_dataframe['group']=='versicolor'
group2=iris_dataframe['group']=='virginica'
print 'var1%0.3fvar2%03f'% (iris_dataframe['petal length (cm)'] [group1].var(), 
                                           iris_dataframe['petal length (cm)'][group2].var())
t,pvalue=ttest_ind(iris_dataframe['sepal width (cm)'][group1],
                                 iris_dataframe['sepal width (cm)'][group2],axis=0,equal_var=False)                                           
print 't statistic %0.3f p-value %0.3f'% (t, pvalue)

# Print covariance / correlation matrix using pandas
print iris_dataframe.corr()   
print iris_dataframe.cov()
# Print covariance/ correlation matrix using Numpy
covariance_matrix=np.cov(iris_nparray,rowvar=0,bias=1)
correlation_matrix=np.corrcoef(iris_narray,rowvar=0,bias=1)
