from Stuff import Errors
import numpy as np
from keras.utils import np_utils

class Targets:
    def __init__(self, literal_labels):
        self.ininitial_labels = literal_labels
        self.uniques, self.ids = np.unique(literal_labels, return_inverse=True)
        self.one_hooks_labels = np_utils.to_categorical(self.ids)
    def which_label_it(self, number):
        print("here")
        index = search(self.one_hooks_labels, number)
        print index
#        label_index = self.ids[index]
#        print label_index
#        return label



def one_hot_encode_object_array(arr):
    '''One hot encode a numpy array of objects (e.g. strings)'''
    uniques, ids = np.unique(arr, return_inverse=True)
    return np_utils.to_categorical(ids, len(uniques))

def search(array, item):
    if len(array.shape) == 1: return search_in_one_dim(array, item)
    elif len(array.shape) == 2: return search_in_two_dim(array, item)
    else: raise Errors.TypeError()

def search_in_one_dim(array, item):
    if isinstance(array, np.ndarray) != True: raise Errors.TypeError()
    if len(array.shape) != 1: raise Errors.ShapeError()
    result = ()
    for number in np.arange(array.shape[0]):
        current = array[number]
        if current == item:  result = (number, )
    return result

def search_in_two_dim(array, item):
    if isinstance(array, np.ndarray) != True: raise Errors.TypeError()
    if len(array.shape) != 2: raise Errors.ShapeError()
    result = ()
    for row in np.arange(array.shape[0]):
        for number in np.arange(array.shape[1]):
            current = array[row, number]
            if np.array_equal(current, item): result = (row, number)
    return result

def one_hot_encode_object_array(arr):
    '''One hot encode a numpy array of objects (e.g. strings)'''
    uniques, ids = np.unique(arr, return_inverse=True)
    return np_utils.to_categorical(ids, len(uniques))