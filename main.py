import sys
import numpy as np
from Utils.InputGenerator import generateCircularData
from Utils.InputGenerator import inputGenerator
from ConvexHull.JarvisMarch import JarvisMarch
from ConvexHull.GrahamScan import GrahamScan
from ConvexHull.QuickHull import QuickHull
from OnionHull.OnionHull import OnionHull
from SkyLines.SkyLine import SkyLine
from CircleDetector.CircleDetector import CircleDetector
from Utils import FileHandler

sys.setrecursionlimit(1500)


def run_hulls_only(samples):
        times = []
        jm = JarvisMarch()
        jm.fit(samples)

        # print("\nCompleted running Jarvis March on the Data")
        # print("Inputs : ", len(samples))
        # print("Peels Generated: ", len(jm.hull))
        # print("Execution time : ", jm.exec_time)
        # print("Hull(%s): " % len(jm.hull), jm.hull)
        # print("Saving output ... ")
        # FileHandler.saveOutput("Outputs/JarvisMarch.txt", jm.hull)
        times.append(jm.exec_time)

        gs = GrahamScan()
        gs.fit(samples)
        # print("\nCompleted running Graham Scan on the Data")
        # print("Inputs : ", len(samples))
        # print("Peels Generated: ", len(gs.hull))
        # print("Execution time : ", gs.exec_time)
        # print("Hull(%s): " % len(gs.hull), gs.hull)
        # print("Saving output ... ")
        # FileHandler.saveOutput("Outputs/GrahamScan.txt", jm.hull)
        times.append(gs.exec_time)

        qh = QuickHull()
        qh.fit(samples)
        # print("\nCompleted running Quick Hull on the Data")
        # print("Inputs : ", len(samples))
        # print("Peels Generated: ", len(qh.hull))
        # print("Execution time : ", qh.exec_time)
        # print("Hull(%s): " % len(qh.hull), qh.hull)
        # print("Saving output ... ")
        # FileHandler.saveOutput("Outputs/QuickHull.txt", jm.hull)
        times.append(qh.exec_time)

        return times


def run_onion_hulls(samples):
        times = []
        types = [1, 2, 3]
        names = {
                1: "GrahamScan",
                2: "JarvisMarch",
                3: "QuickHull"
        }
        ax = OnionHull(3)
        ax.peel(samples)
                # print("\nCompleted Onion Hull using %s" % (names[x]))
                # print("Inputs : ", len(samples))
                # print("Peels Generated: ", len(ax.peels))
                # print("Execution time : ", ax.exec_time)
        times.append(ax.exec_time)
        # for x in types:
        #         ax = OnionHull(x)
        #         ax.peel(samples)
        #         # print("\nCompleted Onion Hull using %s" % (names[x]))
        #         # print("Inputs : ", len(samples))
        #         # print("Peels Generated: ", len(ax.peels))
        #         # print("Execution time : ", ax.exec_time)
        #         times.append(ax.exec_time)
        return times


def run_skylines(samples):
        times = []
        types = [1, 2, 3]
        names = {
                1: "GrahamScan",
                2: "JarvisMarch",
                3: "QuickHull"
        }
        for x in types:
                ax = SkyLine(x)
                ax.match(samples)
                # print("\nCompleted SkyLine using %s" % (names[x]))
                # print("Inputs : ", len(samples))
                # print("Points in Hull: ", len(ax.hull))
                # print("Points in Skyline: ", len(ax.skyline))
                # print("Execution time : ", ax.exec_time)
                times.append(ax.exec_time)
        return times

nums = [10000, 25000, 50000, 100000, 500000]
# nums = [10, 50, 100, 250, 500, 750, 1000, 5000]
# nums = [10000, 25000, 50000, 100000, 500000]
# nums = [10, 50]
cv_memo = {}
sk_memo = {}
oh_memo = {}

for n in nums:
        print (n)
        samples = inputGenerator(n)

        # run_times = run_hulls_only(samples)
        # cv_memo.update({
        #         n:run_times
        # })

        # run_times_2 = run_skylines(samples)
        # sk_memo.update({
        #         n:run_times_2
        # })
        #
        run_times_3 = run_onion_hulls(samples)
        oh_memo.update({
                n:run_times_3
        })

file = open("oh_test_ouput_2.txt", "w+")
# file.write("\n\n============Convex Hulls==============\n\n")
# file.write(str(cv_memo))
file.write("\n\n============Onion Hulls==============\n\n")
file.write(str(oh_memo))
# file.write("\n\n============Skylines==============\n\n")
# file.write(str(sk_memo))
file.close()


# def run_skylines(samples):
#         sk = SkyLine(2)
#         sk.match(samples)


# FileHandler.createTestFile(10000)
# test_cases, samples = FileHandler.readFile('Inputs/sample.txt')
# samples = inputGenerator(500)
# run_skylines(samples)
#
# def run_circle_detector(samples):
#         cd = CircleDetector(3)
#         cd.fit(samples)
#         return cd.predict()
#
# # FileHandler.createTestFile(100000)
# test_cases, samples = FileHandler.readFile('Inputs/sample.txt')
# run_hulls_only(samples)

# samples = generateCircularData(10000)
# xcv = inputGenerator(500)
# samples = np.vstack((samples, xcv))

# print (run_circle_detector(samples))
