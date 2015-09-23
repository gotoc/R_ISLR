# -*- coding: utf-8 -*-
import	numpy	as	 np
import	pandas	as	 pd
import	pandas.io.data as web

def Technical_Trading():
    sp500=web.DataReader('^GSPC', data_source='yahoo', start='1/1/2000', end='5/1/2015')
    sp500['42d']=np.round(pd.rolling_mean(sp500['Close'], window=42),2)
    sp500['252d']=np.round(pd.rolling_mean(sp500['Close'],window=252),2)
    sp500['42-252']=sp500['42d']-sp500['252d']
    SD=50
    sp500['Regime']=np.where(sp500['42-252']>SD,1,0)
    sp500['Regime']=np.where(sp500['42-252']<-SD,-1, sp500['Regime'])
    sp500['Market']=np.log(sp500['Close']/sp500['Close'].shift(1))
    sp500['Strategy']=sp500['Regime'].shift(1)*sp500['Market']
    sp500[['Market','Strategy']].cumsum().apply(np.exp).plot(grid=True,figsize=(8,5))
    print(sp500['Strategy'].sum())
    print(sp500['Market'].sum())
    










