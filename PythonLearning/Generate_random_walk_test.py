import numpy as np
import scipy.stats as scs
#import statsmodels.api as sm
import matplotlib as mpl
import matplotlib.pyplot as plt

def gen_paths (S0,r,sigma,T,M,I):
    dt=float(T)/M
    paths=np.zeros((M+1,I),np.float64)
    paths[0]=S0
    for t in range (1,M+1):
        rand=np.random.standard_normal(I)
        rand=(rand-rand.mean())/rand.std()
        paths[t]=paths[t-1]*np.exp((r-0.5*sigma**2)*dt+sigma*np.sqrt(dt)*rand)
    plt.plot(paths[:,:3],lw=1.5)
    plt.show()
    return paths

def normality_test(arr):
    print "skew %14.3f"% scs.skew(arr)
    print "skew test p-value %14.3f" % scs.skewtest(arr)[1]
    print "Kurt of data set %14.3f" % scs.kurtosis(arr)
    print "Kurt test p-value %14.3f" % scs.kurtosistest(arr)[1]
    print "Norm test p-value %14.3f" % scs.normaltest(arr)[1]
    
