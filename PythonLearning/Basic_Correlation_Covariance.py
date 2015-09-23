# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:03:14 2015

@author: Di
"""

#Calculate Spearman & Pearson Correlation************
from scipy.stats import spearmanr
from scipy.stats.stats import pearsonr
spearmanr_coef, spearmanr_p=spearmanr(iris_dataframe['sepal length (cm)'], iris_dataframe['sepal width (cm)'])                                                 
pearsonr_coef, pearsonr_p=pearsonr(iris_dataframe['sepal length (cm)'], iris_dataframe['sepal width (cm)'])
print 'Pearson correlation %0.3f | Spearman correlation %0.3f'% (pearsonr_coef,spearmanr_coef)

#Spearman correlation test is used to test nonparametric correlation
#It transform your data into rankings and then correlates the rankings
#Thus it minimizes the influence of non-linear relationship between the two variables

#************************Chi-square**********************
import pandas as pd
from scipy.stats import chi2_contingency
table=pd.crosstab(iris_dataframe['group'], iris_binned['petal length (cm)'])
chi2,p,dof,expected = chi2_contingency(table.values)
print 'Chi-square %0.2f p-value %0.3f' % (chi2, p)

# Chi-square is used to assess the goodness of fit between observed values & expected.
# The chi-square statistic tells you when the table distribution of two variables 
# is statistically comparable to a table in which the two variables are hypothesized 
# as not related to each other (the so-called independence hypothesis).





