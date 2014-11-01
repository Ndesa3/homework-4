import os
import fnmatch
import pickle
#import shelve
#from data_load import data_list


def get_traversal_data(d):
    f1=open(d,"br")
    b = pickle.load(f1)
    f1.close()
   
    return b

