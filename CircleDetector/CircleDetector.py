from __future__ import division
import numpy as np
from ConvexHull.JarvisMarch import JarvisMarch
from ConvexHull.GrahamScan import GrahamScan
from ConvexHull.QuickHull import QuickHull
import matplotlib.pyplot as plt
import time

class CircleDetector(object):
        """

                Returns True if the given set of points form a circle

        """
        def plot(self):
                plt.scatter(self.input[:, 0], self.input[:, 1], marker='.')
                plt.scatter(self.hull[:, 0], self.hull[:, 1], marker='s')
                # plt.show()
                plt.savefig("Outputs/output_circle_detector.png")

        def get_center_point(self, a, b):
                return [(b[0] - a[0])/2, (b[1] - a[1]/2)]

        def get_distance(self, a, b):
                return np.linalg.norm(a-b)

        def getCenter(self, a, b, c):
                xcv = (a[0] - b[0])
                if xcv == 0:
                        xcv = 0.001
                k1 = float(a[1] - b[1]) / xcv
                #Two-point slope equation
                xcv = (a[0] - c[0])
                if xcv == 0:
                        xcv = 0.001
                k2 = float(a[1] - c[1]) / xcv

                #Same for the (A,C) pair

                midAB = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]
                #Midpoint formula
                midAC = [(a[0] + c[0]) / 2, (a[1] + c[1]) / 2]
                #Same for the (A,C) pair
                k1 = -1*k1
                #If two lines are perpendicular, then the product of their slopes is -1.
                k2 = -1*k2
                #Same for the other slope
                n1 = midAB[1] - (k1*midAB[0])
                #Determining the n element
                n2 = midAC[1] - k2*midAC[1]
                #Same for (A,C) pair
                #Solve y1=y2 for y1=k1*x1 + n1 and y2=k2*x2 + n2
                xcv = (k1-k2)
                if xcv == 0:
                        xcv = 0.001
                x = float(n2-n1) / xcv
                y = k1*x + n1
                return [x,y]

        def predict(self):
                triangle_points = self.hull[np.random.choice(len(self.hull), 3)]
                self.center = self.getCenter(triangle_points[0], triangle_points[1], triangle_points[2])
                radiis = [self.get_distance(x, self.center) for x in self.hull]
                radiis = np.array(radiis)
                limits = np.percentile(radiis, [25, 75])
                try:
                        iqr = limits[1] - limits[0]
                except Exception as e:
                        import ipdb; ipdb.set_trace()
                        print ("")
                bottom_cut = limits[0] - 1.5*iqr
                top_cut = limits[0] + 1.5*iqr
                inlier = [x for x in radiis if x > bottom_cut and x < top_cut]
                return len(inlier)/len(radiis) *100

        def fit(self, points):
                self.input = points
                self.client.fit(self.input)
                self.hull = self.client.hull

        def __init__(self, type):
                super(CircleDetector, self).__init__()
                self.type = type
                '''
                        Type 1: Jarvis March
                        Type 2: Graham Scan
                        Type 3: Quick Hull
                '''
                if type == 1:
                        self.client = JarvisMarch()
                elif type == 2:
                        self.client = GrahamScan()
                elif type == 3:
                        self.client = QuickHull()
