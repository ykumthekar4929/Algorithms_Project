import sys
import argparse
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

        print("\nCompleted running Jarvis March on the Data")
        print("Inputs : ", len(samples))
        print("Length of hull: ", len(jm.hull))
        print("Execution time : ", jm.exec_time)
        print("Hull(%s): " % len(jm.hull), jm.hull)
        print("Saving output to - %s "%("Outputs/results_JarvisMarch.txt"))
        jm_result = sorted(jm.hull[:, 2])
        FileHandler.saveOutput("Outputs/results_JarvisMarch.txt", jm_result)
        times.append(jm.exec_time)

        gs = GrahamScan()
        gs.fit(samples)
        print("\nCompleted running Graham Scan on the Data")
        print("Inputs : ", len(samples))
        print("Length of hull: ", len(gs.hull))
        print("Execution time : ", gs.exec_time)
        print("Hull(%s): " % len(gs.hull), gs.hull)
        print("Saving output to - %s "%("Outputs/results_GrahamScan.txt"))
        gs_result = sorted(gs.hull[:, 2])
        FileHandler.saveOutput("Outputs/results_GrahamScan.txt", gs_result)

        times.append(gs.exec_time)

        qh = QuickHull()
        qh.fit(samples)
        print("\nCompleted running Quick Hull on the Data")
        print("Inputs : ", len(samples))
        print("Length of hull: ", len(qh.hull))
        print("Execution time : ", qh.exec_time)
        print("Hull(%s): " % len(qh.hull), qh.hull)
        print("Saving output to - %s "%("Outputs/results_QuickHull.txt"))
        qh_result = sorted(qh.hull[:, 2])
        FileHandler.saveOutput("Outputs/results_QuickHull.txt", qh_result)
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
        for x in types:
                ax = OnionHull(x)
                ax.peel(samples)
                print("\nCompleted Onion Hull using %s" % (names[x]))
                print("Inputs : ", len(samples))
                print("Peels Generated: ", len(ax.peels))
                print("Execution time : ", ax.exec_time)
                save_file = "Outputs/output_onion_%s.txt"%(names[x])
                print("Saving output to - %s "%(save_file))
                FileHandler.saveOutput(save_file, ax.peels)
                times.append(ax.exec_time)
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
                print("\nCompleted SkyLine using %s" % (names[x]))
                print("Inputs : ", len(samples))
                print("Points in Hull: ", len(ax.hull))
                print("Points in Skyline: ", len(ax.skyline))
                print("Execution time : ", ax.exec_time)
                save_file = "Outputs/output_skylines_%s.txt"%(names[x])
                print("Saving output to - %s "%(save_file))
                sk_result = sorted(ax.skyline[:, 2])
                FileHandler.saveOutput(save_file, sk_result)
                times.append(ax.exec_time)
        return times


def test_runner():
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


def run_circle_detector(samples):
        cd = CircleDetector(3)
        cd.fit(samples)
        res = cd.predict()
        print ("There is a %s chance that given points form a Circle"%(res))
        cd.plot()


def read_file(name):
        test_cases, samples = FileHandler.readFile(name)
        return samples


def run_all(samples):
        run_hulls_only(samples)
        run_skylines(samples)
        run_onion_hulls(samples)


def main(type, filename):
        samples = []
        if type == 4:
                samples = generateCircularData(10000)
                xcv = inputGenerator(50)
                # samples = np.vstack((samples, xcv))
        else:
                samples = read_file(filename)
                # samples = inputGenerator(40)


        if type ==1:
                run_hulls_only(samples)
        elif type ==2:
                run_onion_hulls(samples)
        elif type == 3:
                run_skylines(samples)
        elif type == 4:
                run_circle_detector(samples)
        elif type == 5:
                run_all(samples)


if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument("-T", "--type", required = False, default = 1)
        parser.add_argument("-F", "--filename", required = False, default = "Inputs/sample.txt")
        args = parser.parse_args()
        type = int(args.type)
        filename = args.filename

        if type <=5 and type>0:
                main(type, filename)
        else:
                print( "Wrong type please select between 1-4")

# FileHandler.createTestFile(50)
