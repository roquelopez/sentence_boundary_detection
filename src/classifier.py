# -*- coding: utf-8 -*-
'''
Created on 21/07/2014

@author: Roque Lopez
'''
from __future__ import unicode_literals
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree, svm, cross_validation
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
import os
import re
import codecs


class Classifier(object):
    '''
    Machine learning method to classify the words in a sentence as 'boundary' or 'no_boundary'
    '''
    
    def __init__(self):
        self.__label_list = None
        self.__instance_list = None
        self.__vec = DictVectorizer(sparse=True)
        self.__classifier = None
        self.__predicted = None
        
    def set_classifier(self, name='bayes'):
        ''' Choose a machine learning method to classify the data '''
        if name == 'bayes':
            self.__classifier = BernoulliNB()
        elif name == 'gd':
            self.__classifier = SGDClassifier()
        elif name == 'svm':
            self.__classifier =  svm.LinearSVC()
        elif name == 'tree':
            self.__classifier = tree.DecisionTreeClassifier()
        elif name == 'knn':
            self.__classifier =  KNeighborsClassifier(n_neighbors=5)

    def train(self, instance_list, label_list):
        self.__label_list = label_list
        self.__instance_list = instance_list
        data_vectorized = self.__vec.fit_transform(instance_list)
        self.__classifier.fit(data_vectorized, label_list)

    def classify(self, instance_list):
        ''' Classify the data and return the results '''
        data_vectorized = self.__vec.transform(instance_list)
        self.__predicted = self.__classifier.predict(data_vectorized)
        return self.__predicted
       
    def generate_output(self, output_path, instances, texts_list, token_list):
        ''' Generate an output for each file of the test set '''
        i = 0
        
        for file_name, text in texts_list:
            position = 0
            begin = 0
            iterator = 0
            new_text = ""
            
            while True:
                token_size = len(token_list[i])
                position = text[iterator:].find(token_list[i]) + token_size
                iterator += position
                
                if position != token_size and self.__predicted[i-1] == 0:
                    new_text += text[begin:iterator-token_size].strip()
                    if new_text[-1:] == '.': new_text += "<S>\n"
                    else: new_text += ".<S>\n"
                    begin =  iterator-token_size
                
                if instances[i]['at7'] == 'None':
                    with codecs.open(os.path.join(output_path, file_name), 'w', encoding='utf-8') as f:
                        new_text += text[begin:iterator].strip()
                        if new_text[-1:] == '.': new_text += "<S>\n"
                        else: new_text += ".<S>\n"
                        f.write(re.sub("\s{2,}", "\n", new_text))   
                    i += 1    
                    break  
                i += 1
