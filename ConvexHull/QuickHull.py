import numpy as np
import matplotlib.pyplot as plt
import math
import time

class QuickHull():
        """docstring for QuickHull"""

        def getCrossProduct(self, a, b, c):
                y1 = a[1]- b[1];
                y2 = a[1]- c[1];
                x1 = a[0] - b[0];
                x2 = a[0] - c[0];
                return y2 * x1 - y1 * x2;

        def plot(self):
                plt.scatter(self.input[:, 0], self.input[:, 1],marker='o')
                for a,b in zip(self.input[:, 0], self.input[:, 1]):
                        plt.text(a, b, "%s, %s"%(a, b))

                plt.scatter(self.hull[:, 0], self.hull[:, 1], marker = 's')

                # try:
                #         plt.scatter(self.below[:, 0], self.below[:, 1], marker = "v")
                # except Exception as e:
                #         raise e
                #
                # try:
                #         plt.scatter(self.above[:, 0], self.above[:, 1], marker = "^")
                # except Exception as e:
                #         raise e
                plt.plot(self.divider[0],self.divider[1], color='grey',marker='x', linestyle='dashed', linewidth=1, markersize=8)
                plt.show()

        def is_below(self, a, b, point):
                '''
                        Returns True if point is on one side of the line
                '''
                try:
                        v1 = [a[0] - b[0], a[1]- b[1]]
                        v2 = [a[0] - point[0], a[1] - point[1]]
                        xp = v1[0] * v2[1] - v1[1] * v2[0]
                except Exception as e:
                        raise e

                return xp > 0

        def divide(self, a, b, points):
                above = []
                below = []
                for point in points:
                        if not (point==a).all() and not (point==b).all():
                                res = self.is_below(a, b, point)
                                if res:
                                        below.append(point)
                                else:
                                        above.append(point)
                below = np.asarray(below)
                above = np.asarray(above)
                return above, below

        def set_slope(self, a, b):
                diffY = b[1] - a[1]
                diff_X = b[0] - a[0]
                slope = diffY/diff_X
                return slope

        def set_min_max(self):
                min_X = min(self.input[:,0])
                minX = self.input[np.where((self.input[:, 0] == min_X))]
                if len(minX) > 1:
                        min_Y  = min(minX[:, 1])
                        minX = minX[np.where((minX[:, 1] == min_Y))]
                max_X = max(self.input[:,0])
                maxX = self.input[np.where((self.input[:, 0] == max_X))]
                if len(minX) > 1:
                        min_Y  = min(minX[:, 1])
                        maxX = maxX[np.where((maxX[:, 1] == min_Y))]
                self.minX = minX[0]
                self.maxX = maxX[0]


        def get_area(self, maxX, minX, point):
                return abs(0.5*(maxX[0]*(minX[1]-point[1])+minX[0]*(point[1]-maxX[1])+point[0]*(maxX[1] - minX[1])))


        def get_farthest_point(self, maxX, minX, points):
                largest_area = 0
                largest_area_point = []
                for point in points:
                        point_area = self.get_area(maxX, minX, point)
                        if point_area > largest_area:
                                largest_area = point_area
                                largest_area_point = point
                return largest_area_point

        def get_hull(self, maxX, minX, points):
                points_on_left = []
                points_coincident = []
                points_on_right = []

                for point in points:
                        orient = self.getCrossProduct(maxX, minX, point)
                        if orient <= 0:
                                points_on_left.append(point)
                        if orient > 0:
                                points_on_right.append(point)

                largest_top = self.get_farthest_point(maxX, minX, points_on_left)
                if len(largest_top) == 0:
                        return
                else:
                        self.hull = np.vstack((self.hull, largest_top))

                self.get_hull(maxX, largest_top, points_on_left)
                self.get_hull(largest_top, minX, points_on_left)

        def driver(self):
                self.set_min_max()
                self.hull = [self.maxX, self.minX]
                self.divider = [[self.minX[0], self.maxX[0]], [self.minX[1], self.maxX[1]]]

                self.get_hull(self.maxX, self.minX, self.input)

                self.get_hull(self.minX, self.maxX, self.input)



        def fit(self, input):
                self.input = input
                start_time = time.time()
                self.driver()
                self.exec_time = time.time() - start_time
                # print("Fitted %s points using QuickHull in --- %s seconds ---" % (len(self.input),  time.time() - start_time))


        def __init__(self):
                super(QuickHull, self).__init__()
