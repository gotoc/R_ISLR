# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:40:25 2015

@author: Di
"""
###################################SVD##########
import numpy as np
M=np.array([[1,3,4],[2,3,5],[1,2,3],[5,4,6]])
print (M)
U,s,Vh=np.linalg.svd(M,full_matrices=False)
print np.shape(U), np.shape(s), np.shape(Vh)
print s

#matrix U contains information about rows
#Vh: contains all info about the columns
#s: Records the SVD process The sum of all the values in s tells you how much information was previously stored in your original matrix, and each value in r reports how much data has accumulated in each respective column of U and Vh.

print np.dot(np.dot(U,np.diag(s)),Vh) # Full matrix reconstuction 

# Shared Variance: Some variance is shared with one or more other variables, creating redundancy in the data. 
# Redundancy implies that you can find the same information, with slightly different values, in various features and across many observations.
# Unique Variance: Some variance is unique to vairable under examination. It cannot be associated to what happens to any other variables

#******************************************Looking for hidden factors SVD****************
from sklearn.datasets import load_iris
from sklearn.decomposition import FactorAnalysis
iris=load_iris()
X,y=iris.data,iris.target
factor=FactorAnalysis(n_components=4, random_state=101).fit(X)     #Results show there are only two factors, not four.


#******************************************PCA***************************PCA is not impacted by scale, as it uses correlation matrix*********
from sklearn.decomposition import PCA
import pandas as pd
pca=PCA().fit(X)
print 'Explained variance by component: %s'% pca.explained_variance_ratio_
print 
pd.DataFrame(pca.components_, columns=iris.feature_names)        #compoenent is different from factor, factors are related to root cause, component is not

#****************************PCA recgonizing faces*****************
from sklearn.datasets import fetch_olivetti_faces
dataset=fetch_olivetti_faces(shuffle=True, random_state=101)
train_faces=dataset.data[:350,:]
test_faces=dataset.data[350:,:]
train_answers=dataset.target[:350]
test_answers=dataset.target[350:]

from sklearn.decomposition import RandomizedPCA
n_components=25
Rpca=RandomizedPCA(n_components=n_components, whiten=True,random_state = 101). fit(train_faces) #Use RandomizedPCA tool to manipulate big datasets
print 'Explained variance by %i components: %0.3f' % (n_components, np.sum(Rpca.explained_variance_ratio_))
compressed_train_faces = Rpca.transform(train_faces) 
compressed_test_faces = Rpca.transform(test_faces)

import matplotlib.pyplot as plt
photo=17 
test_answers[photo]
plt.subplot(1,2,1)
plt.axis('off')
plt.title('Unknown face '+ str(photo) +' in test set')
plt.imshow(test_faces[photo]. reshape( 64,64), cmap = plt.cm.gray, interpolation ='nearest')
mask = compressed_test_faces[photo,]
squared_errors = np.sum((compressed_train_faces - mask)** 2, axis = 1) #calculate the sum of squared error of RanPCA components
minimum_error_face=np.argmin(squared_errors)   #choose the one with the least squared errors
most_resembling = list(np.where(squared_errors<20)[0])      
print 'Best resembling face in train test: %i' % train_answers[minimum_error_face]

import matplotlib.pyplot as plt
plt.subplot(2,2,1)
plt.axis('off')
plt.title('Unknown fact'+ str(photo)+ 'in test set')
plt.imshow(test_faces[photo].reshape(64,64),cmap=plt.cm.gray,interpolation='nearest')
for k, m in enumerate( most_resembling[: 3]): 
    plt.subplot(2, 2, 2 + k) 
    plt.title('Match in train set no. '+ str(m)) 
    plt.axis('off') 
    plt.imshow(train_faces[m].reshape(64,64), cmap = plt.cm.gray, interpolation ='nearest') 
plt.show()

#*************************Extracting data using NMF*********************
#Look for groups of words that tend to assoicate, newly formed group by dimentionality hint topics you'd like to know
#Words are features, you can discover topics by checking high-score features
#A resulting topics may be expressed by presnece of a word or by absence of it

from sklearn.datasets import fetch_20newsgroups
dataset=fetch_20newsgroups(shuffle=True,categories=['misc.forsale'],remove=('headers', 'footers', 'quotes'), random_state=101)
print 'Posts: %i' % len( dataset.data)
#Selecting objects=forsale, automatically removing headers,footers, quotes
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer( max_df=0.95,min_df=2, stop_words ='english') #remove stop words (the/end whatever shit)
tfidf = vectorizer.fit_transform(dataset.data)    #Term frequency-inverse document frequency (Tf-idf) is a simple calculation based on the frequency of a word in document. 

from sklearn.decomposition import NMF 
n_topics=5
nmf=NMF(n_components=n_topics, random_state=101).fit(tfidf)   
feature_names=vectorizer.get_feature_names()
n_top_words=15
for topic_idx, topic in enumerate(nmf.components_):
    print "Topic #%d:" % (topic_idx+1),
    print " ". join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
print nmf.components_[0,:].argsort()[:-n_top_words-1:-1] # Gets top words for topic 0
print vectorizer.get_feature_names()[1337] # transform indexes into words



















