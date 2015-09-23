# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 04:54:53 2015

@author: Di
"""

import random
import numpy as np
import matplotlib.pyplot as plt
position=0
walk=[position]
steps=1000
for i in xrange(steps):
    step=1 if random.randint(0,1)else -1
    position +=step
    walk.append(position)
plt.plot(walk)
plt.show()

nwalks=5000
nsteps=1000
draws=np.random.randint(0,2,size=(nwalks,nsteps))
steps=np.where(draws>0,1,-1)
walks=steps.cumsum(1)
