import time
import numpy as np
from ConvexHull.JarvisMarch import JarvisMarch
from ConvexHull.GrahamScan import GrahamScan
from ConvexHull.QuickHull import QuickHull
import matplotlib.pyplot as plt


class SkyLine(object):
        """
        Generates SkyLines based on followin 3 types

                Type 1: Jarvis March
                Type 2: Graham Scan
                Type 3: Quick Hull

                Default type : QuickHull

        """
        def plot(self):
                plt.scatter(self.input[:, 0], self.input[:, 1], marker = '.')
                plt.scatter(self.hull[:, 0], self.hull[:, 1], marker = "o")
                plt.show()


        def getInitialPoint(self, points):
                max_Y = max(points[:, 1])
                matches = points[np.where((points[:, 1] == max_Y))]
                min_X = min(matches[:, 0])
                matches_X = matches[np.where((matches[:, 0] == min_X))]
                return matches_X[0]

        def driver(self):
                initial_point = self.getInitialPoint(self.hull)
                hull = [x for x in self.hull if x[0] > initial_point[0]]
                hull = np.asarray(hull)
                if len(hull) == 0:
                        np.vstack((hull, initial_point))
                hullSorted = hull[hull[:,1].argsort()][::-1]
                hullSorted = np.asarray(hullSorted)
                maxX = initial_point[0]
                tempY=0
                skylines = []
                skylines.append(initial_point)
                for x in hullSorted:
                    if(x[1] == initial_point[1]):
                        skylines.append(x)
                    if(x[0] > maxX):
                        skylines.append(x)
                        maxX = x[0]
                        tempY = x[1]
                    elif((x[0] == maxX) and (x[1] > tempY)):
                        skylines.append(x)


                final_skyline= np.unique(skylines, axis = 0)
                final_skyline = sorted(final_skyline, key = lambda k: [k[1], k[0]])
                self.skyline = final_skyline


        def match(self, points):
                self.input = points
                start_time = time.time()
                self.client.fit(self.input)
                self.hull = self.client.hull
                self.driver()
                self.exec_time = time.time() - start_time

        def __init__(self, type):
                '''
                        Type 1: Jarvis March
                        Type 2: Graham Scan
                        Type 3: Quick Hull
                '''
                super(SkyLine, self).__init__()
                self.skyline = []
                if type == 1:
                        self.client = JarvisMarch()
                elif type == 2:
                        self.client = GrahamScan()
                elif type == 3:
                        self.client = QuickHull()
