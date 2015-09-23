import pandas as pd
import pandas.io.data as web
import numpy as np
import scipy.stats as scs

symbols=['^GDAXI','^GSPC','YHOO','MSFT']
data=pd.DataFrame()
for sym in symbols:
    data[sym]=web.DataReader(sym,data_source='yahoo', start='1/1/2006')['Adj Close']
data=data.dropna()            #dropping those N/A number
log_returns=np.log(data/data.shift(1))
log_returns.head()


def normality_test(arr):
    print "skew %14.3f"% scs.skew(arr)
    print "skew test p-value %14.3f" % scs.skewtest(arr)[1]
    print "Kurt of data set %14.3f" % scs.kurtosis(arr)
    print "Kurt test p-value %14.3f" % scs.kurtosistest(arr)[1]
    print "Norm test p-value %14.3f" % scs.normaltest(arr)[1]

for sym in symbols:
    print "\nResults for symbol %s" % sym
    print 32* "-"
    log_data=np.array(log_returns[sym].dropna())
    normality_test(log_data)
    
