# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:40:32 2015

@author: Di
"""

def hashing_trick(input_string,vector_size=10):
    feature_vector=[0]*vector_size
    for word in input_string.split(' '):
        index=abs(hash(word))%vector_size  #turn the position in vector where hash(word)%vector_size into 1
        feature_vector[index]=1
    return feature_vector

# if vector_size too small, there will be easily overlapping

from scipy.sparse import csc_matrix
print csc_matrix([1, 0, 0, 0, 0, 1, 1, 0, 1, 0])

# Sparse CSC_matrix only record the position of 1, by eliminating 0, saving a lot of memory

#------------Using BUiltin HashingVectorizer -------------------
import sklearn.feature_extraction.text as txt
sklearn_hashing_trick = txt.HashingVectorizer( n_features = 20, binary = True, norm = None) 
text_vector = sklearn_hashing_trick.transform( [' Python for data science', 'Python for machine learning'])
text_vector

#transform text into vector, and surpress using sparse-like funciton

# CountVectorizer: Optimally encodes text into a data matrix but cannot address subsequent novelties in text.
# HashingVectorizer: Provides flexibility in situations when it is likely that the application will receive new data, but is less optimal than techniques based on hashing functions.





