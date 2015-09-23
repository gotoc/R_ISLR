# -*- coding: utf-8 -*-
import	numpy	as	 np
import	pandas	as	 pd
import	pandas.io.data as web

def Technical_Trading():
    sp500=web.DataReader('XLU', data_source='yahoo', start='1/1/2010', end='5/1/2015')
    perf={'long_MA':100000,'short_MA':100000, 'cumulative_Return':100000}
    perfx=pd.DataFrame(data=perf,index=[1,100000]) 
    for m in range (60,260,20):
        for n in range (20,m,20):
            sp500['42d']=np.round(pd.rolling_mean(sp500['Close'], window=n),2)
            sp500['252d']=np.round(pd.rolling_mean(sp500['Close'],window=m),2)
            sp500['42-252']=sp500['42d']-sp500['252d']
            for i in range (5,50,5):
                SD=i
                sp500['Regime']=np.where(sp500['42-252']>SD,1,0)
                sp500['Regime']=np.where(sp500['42-252']<-SD,-1, sp500['Regime'])
                sp500['Market']=np.log(sp500['Close']/sp500['Close'].shift(1))
                sp500['Strategy']=sp500['Regime'].shift(1)*sp500['Market']
                    #sp500[['Market','Strategy']].cumsum().apply(np.exp).plot(grid=True,figsize=(8,5))
                perfx[['long_MA'],['short_MA'],['cumulative_Return']]=(m,n,sp500['Strategy'].sum())
                
                
                

                
                
                
                
                 
                
                









