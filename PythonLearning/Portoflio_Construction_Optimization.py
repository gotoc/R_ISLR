import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
import scipy.optimize as sco

symbols=['AAPL','MSFT','YHOO','DB','GLD']
noa=len(symbols)

data=pd.DataFrame()
for sym in symbols:
    data[sym]=web.DataReader(sym,data_source='yahoo', end='1/1/2014')['Adj Close']
data.columns=symbols
rets=np.log(data/data.shift(1))
rets.mean()*252        #Calculate the mean of price of each stock use 252 as factor to annualize
rets.cov()*252      #Generate the covariance matrix 
rets.corr()         #Generate the correlation matrix 
weights=np.random.random(noa)    #Generate five random number as initial weights
weights/=np.sum(weights)     #Normalize the randomly generated weights to make the sum as 1
PortReturn=np.sum(rets.mean()*weights)*252 
PortCov=np.dot(weights.T,np.dot(rets.cov()*252,weights))   #Dot fucntion gives dot product of two vectors/matrix. T is transpose function; this line calculates portfolio variance
PortSD=np.sqrt(PortCov)

prets=[]
pvols=[]
for p in range(2500):
    weights=np.random.random(noa)
    weights/=np.sum(weights)
    prets.append(np.sum(rets.mean()*weights)*252)
    pvols.append(np.sqrt(np.dot(weights.T,np.dot(rets.cov()*252,weights))))
prets=np.array(prets)
pvols=np.array(pvols)
plt.figure(figsize=(8,4))
plt.scatter(pvols,prets,c=prets/pvols,marker='o')
plt.grid(True)
plt.xlabel('expected volatility')
plt.ylabel('expected return')
plt.colorbar(label='Sharpe ratio')
plt.show()

def statistic (weights):
    weights=np.array(weights)
    pret=np.sum(rets.mean()*weights)*252
    pvol=np.sqrt(np.dot(weights.T,np.dot(rets.cov()*252,weights)))
    return np.array([pret,pvol,pret/pvol])
    
def min_func_sharpe(weights):
    return -statistic(weights)[2]

cons=({'type':'eq','fun':lambda x: np.sum(x)-1})  #Constraints is all parameters(weights)add up to 1, expressed as: minimize sum-1;
bnds=tuple((0,1) for x in range(noa)) #bound the parameter values (weights) to be within 0 and 1
opts=sco.minimize(min_func_sharpe, noa*[1./noa,], method='SLSQP',bounds=bnds,constraints=cons) #Minimize the negative sharpe ratio
print (opts['x'].round(3))
print (statistic(opts['x']).round(3))

def min_func_variance(weights):
    return statistic(weights)[1]**2                            #Expression of variance of the portfolio

optv=sco.minimize(min_func_variance,noa*[1./noa,], method='SLSQP',bounds=bnds,constraints=cons)
print (optv['x'].round(3))
print (statistic(opts['x']).round(3))                                           #Minimize the variance of portoflio 



