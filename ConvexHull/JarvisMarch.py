import numpy as np
import matplotlib.pyplot as plt
import time


class JarvisMarch(object):

        """
                docstring for JarvisMarch
        """

        def getLeftMost(self):
                min_X = min(self.input[:, 0])
                minX = self.input[np.where((self.input[:, 0] == min_X))]
                if len(minX) > 1:
                        min_Y = min(minX[:, 1])
                        minX = minX[np.where((minX[:, 1] == min_Y))]
                return minX[0]


        def getCrossProduct(self, a, b, c):
                y1 = a[1] - b[1]
                y2 = a[1] - c[1]
                x1 = a[0] - b[0]
                x2 = a[0] - c[0]
                return y2 * x1 - y1 * x2

        def getOrientations(self, point):
                memo = {}
                for sample in self.input:
                        prod = self.getCrossProduct(point, sample)
                        memo.update({prod.tolist(): sample})
                return memo

        def compare(self, a, b):
                if a > b:
                        return 1
                elif b > a:
                        return -1
                else:
                        return 0

        def distance(self, initialPoint, a, b):
                d1 = np.linalg.norm(initialPoint-a)
                d2 = np.linalg.norm(initialPoint-b)
                return self.compare(d1, d2)

        def getFarthestPoint(self, initialPoint, a, b):
                result = self.distance(initialPoint, a, b)
                if result < 0:
                        return b
                else:
                        return a

        def driver(self, initialPoint=None):
                try:
                        initialPoint = self.getLeftMost()
                except Exception as e:
                        raise e
                startPoint = initialPoint
                hull = []
                nextPoint = self.input[0]
                collinear = []
                while not np.array_equal(startPoint, nextPoint):
                        nextPoint = self.input[0]
                        for current in self.input:
                                if np.array_equal(current, nextPoint) or \
                                        np.array_equal(current, initialPoint):
                                        pass
                                else:
                                        prod = self.getCrossProduct(initialPoint, \
                                                nextPoint, current)
                                        if (prod > 0):
                                                collinear = []
                                                nextPoint = current
                                        elif (prod == 0):
                                                result = self.distance(initialPoint, \
                                                        nextPoint, current)
                                                if result < 0:
                                                        nextPoint = current
                                                collinear.append(current)
                                        else:
                                                pass

                        for x in collinear:
                                hull.append(x)

                        hull.append(nextPoint)
                        initialPoint = nextPoint
                self.hull = np.asarray(hull)

        def plotter(self, points):
                plt.scatter(points[:, 0], points[:, 1])
                plt.scatter(self.hull[:, 0], self.hull[:, 1])
                plt.show()

        def fit(self, input):
                self.input = input
                start_time = time.time()
                self.driver()
                self.exec_time = time.time() - start_time

        def __init__(self):
                super(JarvisMarch, self).__init__()
