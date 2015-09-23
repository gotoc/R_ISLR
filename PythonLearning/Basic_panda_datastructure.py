import numpy as np
import pandas as pd

df=pd.DataFrame({'A': [2,3,1],'B':[1,2,3],'C': [5,3,4]})
df1=pd.DataFrame({'A': [4],'B':[4],'C': [4]})
df=df.append(df1)                                   #Use Append to add a row
df=df.reset_index(drop=True)                       #Use the rest_index to create a new index to make accessing cases easier
print df
df.loc[df.last_valid_index()+1]=[5,5,5]           #add one column to a location which is last valid index
print
print df
df2=pd.DataFrame({'D': [1,2,3,4,5]})
df=pd.DataFrame.join (df,df2)                     # Use Join to combine two dataframe 
print
print df

df=df.drop (df.index[[1]])                       #Remove the Row1
print df
df=df.drop ('B',1)                          #Remove the Column1 
print 
print df

df=df.sort_index(by=['A','C'],ascending=[True,True])    #Sort A first and base on that, sort C if it can 
df=df.reset_index(drop=True)
print 
print df

index=df.index.tolist()
np.random.shuffle(index)            #Randomly shuffle the index
df=df.ix[index]
df=df.reset_index(drop=True)
print
print df 


