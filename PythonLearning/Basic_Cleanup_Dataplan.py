import pandas as pd
df=pd.DataFrame ({'A': [0,0,0,0,1,1,1],          
                'B': [1,2,3,5,4,2,5],
                'C': [5,3,4,1,1,2,3]})
a_group_desc=df.groupby('A').describe()
unstacked=a_group_desc.unstack()
print unstacked

# Data Plan,"Randomly" split the dataset into different group and see if the stats descriptions of groups are consistent

