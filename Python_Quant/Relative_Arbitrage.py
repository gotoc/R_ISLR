# -*- coding: utf-8 -*-
import	numpy	as	np
import	pandas	as	pd
import	pandas.io.data as	web

def Relative_Arbitrage ():

    sp500=web.DataReader('^GSPC', data_source='yahoo', start='1/1/2000', end='5/1/2015')
    F=web.DataReader('IBM', data_source='yahoo', start='1/1/2000', end='5/1/2015')
    Struct={'sp500':sp500['Close'],'F':F['Close']}  #define as dict
    DF=pd.DataFrame.from_dict(Struct)   #Convert Dict into dataframe (Pandas function)
    DF['3d Correl']=pd.rolling_corr(DF['sp500'],DF['F'],window=2)
    DF['sp500_Return']=np.log(DF['sp500']/DF['sp500'].shift(2))
    DF['F_Return']=np.log(DF['F']/DF['F'].shift(2))
    DF['Sp500 op']=0
    DF['F op']=0
    DF['Port Op']=0
    DF['Port Op']=np.where((DF['3d Correl']<-0.4),1,0)
    DF['Port Op']=np.where((DF['Port Op'].shift(1)==1)&(DF['3d Correl']<0.95),1,0)
    DF['sp500 op']=np.where((DF['Port Op']==1)&(DF['F_Return']>0.01),1,0)
    DF['F op']=np.where(DF['sp500 op']==1,-1,0)
    DF['sp500 1d return']=np.log(DF['sp500']/DF['sp500'].shift(1))
    DF['F 1d return']=np.log(DF['F']/DF['F'].shift(1))
    DF['Strategy']=DF['sp500 1d return']*DF['sp500 op'].shift(1)+DF['F 1d return']*DF['F op'].shift(1)
    DF[['sp500 1d return','Strategy']].cumsum().apply(np.exp).plot(grid=True,figsize=(8,5))
    
