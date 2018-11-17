import numpy as np
from ConvexHull.JarvisMarch import JarvisMarch
from ConvexHull.GrahamScan import GrahamScan
from ConvexHull.QuickHull import QuickHull
import matplotlib.pyplot as plt
import time


class OnionHull(object):
        """
        Generates onion hull based on followin 3 types

                Type 1: Jarvis March
                Type 2: Graham Scan
                Type 3: Quick Hull

                Default type : QuickHull

        """

        def plot(self):
                # import ipdb; ipdb.set_trace()

                plt.scatter(self.input[:, 0], self.input[:, 1])
                for hull in self.peels:
                        plt.plot(hull[:, 0], hull[:, 1])
                plt.show()

        def save_hull_to_peels(self, hull):
                self.peels.append(hull)

        def hull_minus(self, points, hull):
                hull = set([tuple(x) for x in hull])
                points = set([tuple(x) for x in points])
                return np.array(list(points - hull))

        def driver(self, points):

                if len(points)  <= 3:
                        self.peels.append(points)
                        return

                while(len(points) > 3):
                        self.client.fit(points)
                        self.save_hull_to_peels(self.client.hull)
                        points = self.hull_minus(points, self.client.hull)

                self.peels.append(points)

                # if len(new_points) <=3:
                #         self.peels.append(new_points)
                #         return
                # else:
                #         self.driver(new_points)

        def peel(self, points):
                self.peels = []
                self.input = points
                start_time = time.time()
                self.driver(self.input)
                self.exec_time = time.time() - start_time



        def __init__(self, type=3):
                '''
                        Type 1: Jarvis March
                        Type 2: Graham Scan
                        Type 3: Quick Hull
                '''
                super(OnionHull, self).__init__()
                self.hull = []
                if type == 1:
                        self.client = JarvisMarch()
                elif type == 2:
                        self.client = GrahamScan()
                elif type == 3:
                        self.client = QuickHull()
