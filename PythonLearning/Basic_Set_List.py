from sets import Set                                                       #Basic Set Operation
SetA=Set([' Red', 'Blue', 'Green', 'Black']) 
SetB=Set([' Black', 'Green', 'Yellow', 'Orange']) 
SetX=SetA.union(SetB) 
SetY=SetA.intersection(SetB) 
SetZ = SetA.difference(SetB)            
print (SetA.issuperset(SetY))                          #set operation. issuperset
print (SetA.issubset(SetY))
List=[0,1,2,3,4,5]
List2=[2,3,5,7,9]
List.extend(List2)
for value in List2:                                    #Use of List 
    print (value)
    

import numpy as np                                
x=np.array([[[1,2,3],[4,5,6],[7,8,9],],
        [[11,12,13],[14,15,16],[17,18,10],],
        [[21,22,23],[24,25,26],[27,28,29]]])
        
print x[1]               #the second row
print x[:,1]             #the second column
print x[1,1]             #row 1 and column 1  
print x[:,1,1]          #
print x[1,:,1]          #the column 1 element of row 1
print x[1:2,1:2]        #row 1 and 2 of column 1 and 2
print
print x[:,1,1]            
