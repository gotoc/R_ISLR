# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 06:08:53 2015

@author: Di
"""

import math
import numpy as np
from time import time

np.random.seed(20000)
t0=time()

S0=100; 
K=105.0;
T=1.0;
r=0.05;
sigma=0.2;
M=50
dt=T/M;
I=250000

S=np.zeros((M+1,I))
S[0]=S0
for t in range(1,M+1):
    z=np.random.standard_normal(I)
    S[t]=S[t-1]*np.exp((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*z)
C0=math.exp(-r*T)*np.sum(np.maximum(S[-1]-K,0))/I

S[0]=101
for t in range(1,M+1):
    z=np.random.standard_normal(I)
    S[t]=S[t-1]*np.exp((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*z)
C1=math.exp(-r*T)*np.sum(np.maximum(S[-1]-K,0))/I

delta=C1-C0
tnp1=time()-t0
print "European Option Value %7.3f"% C1
print "Delta %7.3f"% delta
print "Duration in Seconds %7.3f"% tnp1