import numpy as np
import pprint
import matplotlib.pyplot as plt
import math
from collections import OrderedDict
import time

class GrahamScan(object):
        """docstring for GrahamScan"""

        def getInitialPoint(self):
                minY = min(self.input[:,1])
                minYs =[x for x in self.input if x[1] == minY]
                minYs = np.asarray(minYs)
                minX = min(minYs[:,0])
                return [x for x in minYs if x[0] == minX][0]


        def polarAngle(self,a,b):
            a1 = np.asarray(a)
            b1 = np.asarray(b)
            if(np.array_equal(a1,b1)):
                return 0
            return math.atan2(b[1]-a[1],b[0]-a[0])


        def getCrossProduct(self, a, b, c):
            y1 = b[1]- a[1];
            y2 = c[1]- a[1];

            x1 = b[0] - a[0];
            x2 = c[0] - a[0];
            val = x1 * y2 - x2 * y1;
            return val


        def sortByPolarAngle(self, a, points):
            angle_points = dict()
            for x in points:
                angle = self.polarAngle(a, x)
                if angle in angle_points:
                    values = angle_points.get(angle)
                    values.append(x)
                    angle_points[angle] = values
                values =[x]
                angle_points[angle] = values
            points = sorted(points, key=lambda x: self.polarAngle(a, x))
            return points


        def getNextToTop(self,stack):
            top = stack.pop()
            nextToTop = stack.pop()
            stack.append(nextToTop)
            stack.append(top)
            return nextToTop

        def getTop(self,stack):
            top = stack.pop()
            stack.append(top)
            return top

        def plot(self, hull):
            plt.scatter(self.input[:, 0], self.input[:, 1])
            plt.plot(hull[:, 0], hull[:, 1])
            plt.show()


        def driver(self):
            self.initial_point = self.getInitialPoint()
            points = self.sortByPolarAngle(self.initial_point, self.input)
            stack=[]
            stack.append(points[0])
            stack.append(points[1])
            stack.append(points[2])
            for x in points[2:]:
                #print(stack)
                while (len(stack)>1 and self.getCrossProduct(self.getNextToTop(stack),self.getTop(stack),x) < 0):
                    pop = stack.pop()
                if(not(stack) or not(np.array_equal(stack[-1],x))):
                    stack.append(x)
            hull = stack[::-1]
            self.hull = np.asarray(hull)


        def fit(self, input):
            self.input = input
            start_time = time.time()
            self.driver()
            self.exec_time = time.time() - start_time
            # print("Fitted %s points using GrahamScan in --- %s seconds ---" % (len(self.input),  time.time() - start_time))

        def __init__(self):
                super(GrahamScan, self).__init__()
