# -*- coding: utf-8 -*-
import	numpy	as	 np
import	pandas	as	 pd
import	pandas.io.data as web

def VIX():
    sp500=web.DataReader('^GSPC', data_source='yahoo', start='1/1/2000', end='5/1/2015')
    VIX=web.DataReader('^VIX', data_source='yahoo', start='1/1/2000', end='5/1/2015')
    VIX['10d']=np.round(pd.rolling_mean(VIX['Close'], window=10),2)
    VIX['50d']=np.round(pd.rolling_mean(VIX['Close'],window=50),2)
    VIX['10-50']=VIX['10d']-VIX['50d']
    SD=0.8               #We should use Skew Steepness, not vol scheme as singal, will be more accurate# 
    VIX['Regime']=np.where((VIX['10-50']>SD)&(VIX['10d']<20),1,0)  #In low vol scheme: If 10d VIX MACD - 50d > 1, then buy SPX
    VIX['Regime']=np.where((VIX['10-50']<-SD)&(VIX['10d']<20),-1, VIX['Regime']) #In low vol scheme: if 10d-50d<-1, then sell SPX
    VIX['Regime']=np.where((VIX['10-50']>SD)&(VIX['10d']>20),-1,VIX['Regime'])  #In high vol scheme: If 10d VIX MACD - 50d > 1, then sell SPX
    VIX['Regime']=np.where((VIX['10-50']<-SD)&(VIX['10d']>20),1, VIX['Regime']) #In low vol scheme: if 10d-50d<-1, then buy SPX
    VIX['Market']=np.log(sp500['Close']/sp500['Close'].shift(1))
    VIX['Strategy']=VIX['Regime'].shift(1)*VIX['Market']
    VIX[['Market','Strategy']].cumsum().apply(np.exp).plot(grid=True,figsize=(8,5))
  










