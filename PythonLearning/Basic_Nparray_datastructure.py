import numpy as np

x=np.array([[[1,2,3],[4,5,6],[7,8,9],],
        [[11,12,13],[14,15,16],[17,18,10],],
        [[21,22,23],[24,25,26],[27,28,29]]])
        
x[1]               #the second row
x[:,1]             #the second column
x[1,1]             #row 1 and column 1  
x[:,1,1]          #
x[1,:,1]          #the column 1 element of row 1
x[1:2,1:2]        #row 1 and 2 of column 1 and 2
x[:,1,1]            

dataset=np.array([[2,4,6,8,3,2,5],[7,3,5,1,6,8,0],[1,3,2,1,0,0,8]])
print np.max(dataset,axis=1)
print np.min(dataset,axis=1)

dataset2=np.array([2,4,6,8,3,2,5])              #manipulation of vector defined by Np.Array
dataset2=dataset2*3
print dataset2

dataproduct=np.dot(dataset,dataset2)               #Dot operation between matrix
print dataproduct 

# Difference between matrix & vector: A matrix is simply a rectangular array of numbers and a vector is a row (or column) of a matrix.
