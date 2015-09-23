# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 06:21:05 2015

@author: Di
"""

import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

s0=100.
r=0.05
v0=0.1
kappa=3.0
theta=0.25
sigma=0.1
rho=0.6
T=1.0

corr_mat=np.zeros((2,2))   #Initialize a matrix of correlation with 0,0 
corr_mat[0,:]=[1.0,rho]    #Put value in the matrix correlation Row1
corr_mat[1,:]=[rho,1.0]    #Row 2
cho_mat=np.linalg.cholesky(corr_mat)  #Cholesky decomposition of the matrix

M=50     #50 walks
I=10000  #each walk 10000 steps
ran_num=npr.standard_normal((2,M+1,I))  # Simulate two sets of random number, each set has 51 walks, each walk 1000 steps

dt=T/M
v=np.zeros_like(ran_num[0])
vh=np.zeros_like(v)
v[0]=v0
vh[0]=v0

for t in range(1, M+1):
    ran=np.dot(cho_mat,ran_num[:,t,:]) #generate two walks which are correlated, taking walk t  of set1 and set2
    vh[t]=(vh[t-1]+kappa*(theta-np.maximum(vh[t-1],0))*dt+sigma*np.sqrt(np.maximum(vh[t-1],0))*np.sqrt(dt)*ran[1])
v=np.maximum(vh,0)   #Simulate the stochastic vol, using walk1 

S=np.zeros_like(ran_num[0])
S[0]=s0
for t in range(1,M+1):
    ran=np.dot(cho_mat,ran_num[:,t,:]) 
    S[t]=S[t-1]*np.exp((r-0.5*v[t])*dt+np.sqrt(v[t])*ran[0]*np.sqrt(dt))
    #Simulate the index level, using walk0    
    #Given cholesky decomp, the walk1 and walk 0 should be correlated
fig, (ax1,ax2)=plt.subplots(2,1, sharex=True, figsize=(2,5))
ax1.plot(S[:,:10],lw=1.5)
ax1.grid(True)
ax2.plot(v[:,:10],lw=1.5)
ax2.set_xlabel('time')
ax2.set_ylabel('vol')
ax2.grid(True)
plt.show()

    