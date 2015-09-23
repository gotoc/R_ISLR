# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 05:12:41 2015

@author: Di
"""

from sklearn.datasets import fetch_20newsgroups
newsgroups_train=fetch_20newsgroups(subset='train', remove=('headers','footers','quotes'))
newsgroups_test =fetch_20newsgroups(subset ='test', remove=('headers', 'footers', 'quotes'))

from sklearn.naive_bayes import BernoulliNB, MultinomialNB
Bernoulli = BernoulliNB(alpha = 0.01) 
Multinomial = MultinomialNB(alpha = 0.01)

import sklearn.feature_extraction.text as txt
multinomial_hashing_trick=txt.HashingVectorizer(stop_words ='english', binary = False, norm = None, non_negative = True) 
binary_hashing_trick=txt.HashingVectorizer(stop_words ='english', binary = True, norm = None, non_negative = True)

Multinomial.fit(multinomial_hashing_trick.transform(newsgroups_train.data), newsgroups_train.target) 
Bernoulli.fit(binary_hashing_trick.transform(newsgroups_train.data), newsgroups_train.target)

from sklearn.metrics import accuracy_score
for m, h in [(Bernoulli, binary_hashing_trick), (Multinomial, multinomial_hashing_trick)]: 
    print 'Accuracy for %s: %.3f'% (m, accuracy_score(y_true = newsgroups_test.target, y_pred = m.predict(h.transform(newsgroups_test.data))))


