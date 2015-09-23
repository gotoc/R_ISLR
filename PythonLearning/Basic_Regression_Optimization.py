# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 04:50:02 2015

@author: Di
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)+0.5*x

x=np.linspace(-2*np.pi,2*np.pi,50)  #np.linspace(start,stop,num) return num points beginning with start and end with stop. It displays function over fixed interval
plt.plot(x,f(x),'b')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')

reg=np.polyfit(x,f(x),deg=7)    #linear regression (deg=1)/ high-dimensional regression (deg>1), estimates saved in ry
ry=np.polyval(reg,x)

plt.plot(x,f(x),'b',label='f(x)')
plt.plot(x,ry,'r',label='regression')
plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
print(reg)   #print the coefficient of the items
print (np.sum((f(x)-ry)**2)/len(x)) #print the mean squared error 

matrix=np.zeros((3+1,len(x)))
matrix[3,:]=np.sin(x)       #Knowing the dependent function has sin(x)
matrix[2,:]=x**2
matrix[1,:]=x
matrix[0,:]=1

reg2=np.linalg.lstsq(matrix.T,f(x))[0] #Use linalg. least squared optimizaiton
ry2=np.dot(reg2,matrix)  #Get the estiamtes using dot product
print(reg2)
plt.plot(x,f(x),'b',label='f(x)')
plt.plot(x,ry2,'r',label='regression')
plt.legend(loc=0)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')


#**********************Constrainted Optimization********************
from math import sqrt
import scipy.optimize as spo 

def EU((s,b)):
    return -(0.5*sqrt(s*15+b*5)+0.5*sqrt(s*5+b*12))   #Target functions to be optimzied
#Constraints
cons=({'type':'ineq','fun':lambda(s,b):100-s*10-b*10})  #Constraints
#Budget constraint
bnds=((0,1000),(0,1000)) #upper bounds large enough   #Bounds of parameters

result=spo.minimize(EU,[5,5],method='SLSQP',bounds=bnds,constraints=cons)
print (result)                #Page 233 of Python Finance Book 

#*********************Monte Carlo & Integration**********************
import scipy.integrate as sci
def f(x):
    return np.sin(x)+0.5*x
a=0.5
b=9.5
for i in range(1,20):   #increasing the number of draws from 10 to 200
    np.random.seed(1000)
    x=np.random.random(i*10)*(b-a)+a #Generate a list consisting of i*10 numbers which are random number between a and b
    print np.sum(f(x))/len(x)*(b-a)   #Calcualte the mean of f(x), and square of f(x)*(b-1)based on that
    
#Draw I random values of x between integral limits and evaluate the integration function at every random value of x.
#Sum up all the function values and take the average to arrive at an average function value over the integral interval.
#Multiply this value by the length of the integration interval to derive an estimate for the integral value
    