import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
S0=100
r=0.05
v0=0.1
kappa=3.0
theta=0.25
sigma=0.1
rho=0.6
T=1

corr_mat=np.zeros((2,2,))
corr_mat[0,:]=[1.0,rho]
corr_mat[1,:]=[rho,1.0]
cho_mat=np.linalg.cholesky(corr_mat)

M=50
I=10000
ran_num=npr.standard_normal((2,M+1,I))

dt=T/M
v=np.zeros_like(ran_num[0])
vh=np.zeros_like(v)
v[0]=v0
vh[0]=v0
for t in range(1,M+1):
    ran=np.dot(cho_mat,ran_num[:,t,:])
    vh[t]=(vh[t-1]+kappa*(theta-np.maximum(vh[t-1],0))*dt+sigma*np.sqrt(np.maximum(vh[t-1],0))*np.sqrt(dt)+ran[1])
v=np.maximum(vh,0)

S=np.zeros_like(ran_num[0])
S[0]=S0
for t in range(1,M+1):
    ran=np.dot(cho_mat,ran_num[:,t,:])
    S[t]=S[t-1]*np.exp((r-0.5*v[t])*dt+np.sqrt(v[t])*ran[0]*np.sqrt(dt))

plt.ylim(-100,20)
plt.plot(S[:,:10],lw=1.5)
plt.plot(v[:,:10],lw=1.5)
plt.show()