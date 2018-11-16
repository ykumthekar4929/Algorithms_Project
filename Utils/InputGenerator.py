# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 12:17:06 2018

@author: pradn
"""

import random
import matplotlib.pyplot as plt
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


def generateCircularData(num, error=0):
        theta = np.linspace(0, 2*np.pi, num)
        a, b = 1 * np.cos(theta), 1 * np.sin(theta)
        r = np.random.rand((num))
        x, y = r * np.cos(theta), r * np.sin(theta)
        samples = []
        for _ in range(num):
                samples.append([x[_], y[_]])
        wrongs = np.random.uniform(low=-0.5, high=1.5, size=(error, 2) )
        return np.vstack((np.array(samples), wrongs))
        # plots
        # plt.figure(figsize=(7,6))
        # plt.plot(a, b, linestyle='-', linewidth=2, label='Circle')
        # plt.plot(x, y, marker='o', linestyle='dashed', label='Samples')
        # plt.ylim([-1.5,1.5])
        # plt.xlim([-1.5,1.5])
        # plt.grid()
        # plt.legend(loc='upper right')
        # plt.show(block=True)



if __name__ == '__main__':
        print (generateCircularData(100000))
