import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer

s=pd.Series([1,2,3,np.NaN,5,6,None])
imp=Imputer(missing_values='NaN',strategy='mean', axis=0)         #    
imp.fit([1,2,3,4,5,6,7])
x=pd.Series(imp.transform(s).tolist()[0])


print s.isnull()
print s[s.isnull()]                  #use isnull to detect missing values
print s.fillna(int(s.mean()))        #fill the void with mean 
print
print s.dropna()                     #Drop the void
print
print (x)
