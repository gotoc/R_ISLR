# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:47:51 2015

@author: Di
"""
from sklearn.preprocessing import scale
from scipy.stats import spearmanr
from scipy.stats.stats import pearsonr

stand_sepal_width=scale(iris_dataframe['sepal width (cm)'])   #Calculating the Z-score of the data
tranformations={'x': lambda x: x, '1/x': lambda x: 1/x, 'x**2': lambda x: x**2, 'x**3': lambda x: x**3, 'log(x)': lambda x: np.log(x)}
for transformation in transformations:
    pearsonr_coef, pearsonr_p = pearsonr( iris_dataframe['sepal length (cm)'], tranformations[ transformation]( iris_dataframe['sepal width (cm)']))
    print 'Transformation: %s \t Pearson\' s r: %0.3f' % (transformation, pearsonr_coef)



