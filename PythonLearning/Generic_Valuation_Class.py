# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 05:28:19 2015

@author: Di
"""

class valuation_class(object):
    def __int__(self,name,underlying,mar_env,payoff_func):
        try:
            self.name=name
            self.pricing_date=mar_env.pricing_date
            try:
                self.strike=mar_env.get_constant('strike')
            except:
                pass
            self.maturity=mar_env.get_constant('maturity')
            self.currency=mar_env.get_constant('currency')
            self.frequency=underlying.frequency
            self.paths=underlying.paths
            self.discount_curve=underlying.discount_curve
            self.payoff_func=payoff_func
            self.underlying=underlying
            self.underlying.special_dates.extend([self.pricing_date,self.maturity])
         except: 
            print "Error parsing market environment"
    
    def update(self, initial_value=None,volatility=None,strike=None,maturity=None):
        if initial_value is not None:
            self.underlying.update(initial_value=initial_value)
        if volatility is not None:
            self.underlying.update(volatility=volatility)
        if strike is not None:
            self.strike=strike
        if maturity is not None:
            self.maturity=maturity
            if not maturity in self.underlying.time_grid:
                self.underlying.special_dates.append(maturity)
                self.underlying.instrument_values=None
    
    def delta(self, interval=None, accuracy=4):
        if interval is None:
            interval=self.underlying.initial_value/50.
        value_left=self.present_value(fixed_seed=True)
        initial_del=self.underlying.initial_value+interval
        self.underlying.update(initial_value=initial_del)
        value_right=self.present_value(fixed_seed=True)
        self.underlying.upgrade(initial_value=initial_del-interval)
        delta=(value_right-value_left)/interval
        if delta<-1.0:
            return -1.0
        if delta>1.0:
            return 1.0
        else:
            return round(delta,accuracy)