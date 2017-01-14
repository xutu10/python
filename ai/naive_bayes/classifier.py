#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from preprocess_documents import read_and_preprocess_documents
import sys
import argparse
import pickle
"""

  KI Exercise "Naive Bayes" 
  -------------------------
  a small interface for document classification.
  Fill in code (see FIXMEs) and implement your own 
  document classifier.

  Train the classifier on the training documents like this:

  > python classifier.py --train nytimes_data/train/*/*

  Apply the classifier to the test documents like this:

  > python classifier.py --apply nytimes_data/test/*/*

"""

class Classifier:

    def __init__(self):

        """ The classifier should store all its learned information
            in this 'model' object. Pick whatever form seems appropriate
            to you. """
        self.model = None

    def train(self, features, labels):
        """
        trains a document classifier and stores all relevant
        information in 'self.model'.

        @type features: dict
        @param features: Each entry in 'features' represents a document
                         by its (sparse) bag-of-words vector. 'features'
                         is of the following form (i.e., for each document, 
                         all terms occurring in the document and their
                         counts are stored in a dictionary):
                         {
                           'doc1.txt':
                              {
                                'the' : 17,
                                'world': 3, 
                                ...
                              },
                           'doc2.txt':
                              {
                                'community' : 2,
                                'college': 1, 
                                ...
                              },
                            ...
                         }
        @type labels: dict
        @param labels: 'labels' contains the class labels for all documents
                       in dictionary form:
                       {
                           'doc1.txt': 'arts',
                           'doc2.txt': 'business',
                           'doc3.txt': 'sports',
                           ...
                       }
        """
        raise NotImplementedError()

    def apply(self, features):
        """
        applies a classifier to a set of documents. Requires the classifier
        to be trained (i.e., you need to call train() before you can call test()).

        @type features: dict
        @param features: Each entry in 'features' represents a document
                         by its (sparse) bag-of-words vector. 'features'
                         is of the following form (i.e., for each document, 
                         all terms occurring in the document and their
                         counts are stored):
                         {
                           'doc1.txt':
                              {
                                'the' : 17,
                                'world': 3, 
                                ...
                              },
                           'doc2.txt':
                              {
                                'community' : 2,
                                'college': 1, 
                                ...
                              },
                            ...
                         }
        @rtype: dict
        @return: For each document classified, apply() returns the label
                 of the class the document has been assigned to. The return value
                 is a dictionary of the form:
                 {
                   'doc1.txt': 'arts',
                   'doc2.txt': 'travel',
                   'doc3.txt': 'sports',
                   ...
                 }
        """
        raise NotImplementedError()


class NaiveBayesClassifier():

    def __init__(self):
        # FIXME: implement (Exercise 02)
        self.pc = {}
        self.pxc = {}
#        raise NotImplementedError()

    def train(self, features, labels):
        # FIXME: implement (Exercise 02)
        counter = 0

        # beginning of for loop
        for k in features.keys():
            counter += 1
            class_name = labels[k]

            # handle self.pc
            if class_name in self.pc.keys():
                self.pc[class_name] += 1.0
            else:
                # class occurs first time
                # add class_name as key in self.pc
                self.pc.update({class_name:1.0})
        
            # handle self.pxc
            # store subdict in features
            dict_temp = features[k]
            # whether class already as key in self.pxc
            if class_name in self.pxc.keys():
                # increment counter of class
                self.pxc[class_name]['class_counter'] += 1
                # walk through subdict in features
                for key in dict_temp.keys():
                    # whether word as key already in subdict of self.pxc 
                    if key in self.pxc[class_name].keys():
                        # increment value of word
                        self.pxc[class_name][key] += 1
                    else:
                        # add new word in subdict
                        self.pxc[class_name].update({key:1.0})
            else:
                # class name occurs first time
                # add class name as key in self.pxc
                # and add classcounter as key in subdict of self.pxc
                self.pxc.update({class_name:{}})
                self.pxc[class_name].update({'class_counter':1})
                # walk through subdict from feature
                # add word in subdict of self.pxc
                for key in dict_temp.keys():
                    self.pxc[class_name].update({key:1.0})

        # ending of for loop

        # calculate probability for each class in self.pc
        for k in self.pc.keys():
            self.pc[k] /= counter

        #calculate pro for each word in each class
        for k in self.pxc.keys():
            # store counter of class
            counter_tmp = self.pxc[k]['class_counter']
            # remove the counter item from subdict
            del self.pxc[k]['class_counter']
    
            for key in self.pxc[k].keys():
                # frequency devided by freqeuency of class
                self.pxc[k][key] /= counter_tmp

#        raise NotImplementedError()

    def apply(self, features):
        # FIXME: implement (Exercise 03)
        raise NotImplementedError()


if __name__ == "__main__":

    # parse command line arguments (no need to touch)
    parser = argparse.ArgumentParser(description='A text classifier based on Naive Bayes.')
    parser.add_argument('documents', metavar='doc', type=str, nargs='+',
                        help='documents to train/apply the classifier on/to')
    parser.add_argument('--train', help="train the classifier", action='store_true')
    parser.add_argument('--apply', help="apply the classifier (you'll need to train or load"\
                                        "a trained model first)", action='store_true')

    args = parser.parse_args()

    # reads and preprocesses the documents listed as commandline arguments. 
    # You can use the resulting features for classification.
    wordmap, features = read_and_preprocess_documents(args.documents)

    # estimate class labels ('arts', 'business', 'dining', ...)
    # from directory names
    labels = {}
    for filename in features:
        tokens = filename.split("/")
        classlabel = tokens[-2]
        labels[filename] = classlabel

    # FIXME: have a look at 'features' and 'labels'
    # for k,v in labels.items():
    #     print k,'-',v,
    # print '--------'

    # for k,v in features.items():
    #     print k,'-',v,
    # print '-----------'
    classifier = NaiveBayesClassifier()

    #  train classifier on 'features' and 'labels' 
    # (using documents from the 'train' folder)
    if args.train:
        classifier.train(features, labels)
        pickle.dump(classifier,file("classifier.pickle","wb"))
    # apply the classifier to documents from
    # the 'test' folder
    if args.apply:
        result = classifier.apply(features)
        
    # FIXME: measure error rate on 'test' folder (Exercise 04)

