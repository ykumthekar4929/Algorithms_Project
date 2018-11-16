# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:17:06 2018

@author: pradn
"""

import random
# import matplotlib.pyplot as plt
import numpy as np

def inputGenerator(samples):

    '''
        Input: samples int denoting number of samples
        Output: an array of shape (samples, 2) with range between - samples
        to samples
    '''

    rangeOfValues = (-samples, samples)
    randPoints = []
    i = 0
    while i<=samples -1:
        x = random.randrange(*rangeOfValues)
        y = random.randrange(*rangeOfValues)
        randPoints.append((x,y))
        i += 1
    sampleSet = np.asarray(randPoints);
    return sampleSet




if __name__ == '__main__':
        print (inputGenerator(100))
