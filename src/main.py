# -*- coding: utf-8 -*-
'''
Created on 20/07/2014

@author: Roque Lopez
'''

from __future__ import unicode_literals
from classifier import Classifier
from feature_extractor import Feature_Extractor
from utils import print_metrics, punkt, mxterminator
from probabilistic_tagger import ProbabilisticTagger
import sys


if __name__ == '__main__':
    option =  sys.argv[1]
    if option not in ['proposal', 'punkt', 'mxterminator']:
        raise ValueError("Invalid option")
        
    train_path_list =  ["../resource/data/train_data/"]
    test_path = "../resource/data/test_data/"
    manual_punctuation_path = "../resource/data/test_data_annotated/"
    output_path = "../resource/data/output_data/"
    fe = Feature_Extractor(True, False)
    
    if option == 'proposal': 
        print "Reading training data..."
        fe.extract_to_train(train_path_list)
        
    size_train = fe.get_size()
    print "Reading test data..."
    fe.extract_to_test(test_path)
    print "Reading gold data..." 
    fe.update_labels(size_train, manual_punctuation_path)
    instance_list = fe.get_instance_list()
    label_list = fe.get_label_list()
    train_instances = instance_list[:size_train]
    train_labels = label_list[:size_train]
    test_instances = instance_list[size_train:]
    test_labels = label_list[size_train:]

    print "Classifying..."
    
    if option == 'proposal':
    #***************** Proposed Method *****************#       
        c = Classifier()
        c.set_classifier('bayes')
        c.train(train_instances, train_labels)
        predicted = c.classify(test_instances)
        print_metrics(test_labels, predicted)
        print "Outputs generated" 
        c.generate_output(output_path, test_instances, fe.get_texts_list()[size_train:], fe.get_tokens_list()[size_train:])
    
    elif option == 'punkt':
    #********************** Punkt **********************#
        predicted = punkt(test_path)
        print_metrics(test_labels, predicted)
    
    elif option == 'mxterminator':
    #******************* MXTERMINATOR ******************#
        predicted = mxterminator("../resource/data/mxterminator_output/")
        print_metrics(test_labels, predicted)
