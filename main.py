import sys
from ConvexHull.JarvisMarch import JarvisMarch
from ConvexHull.GrahamScan import GrahamScan
from ConvexHull.QuickHull import QuickHull
from OnionHull.OnionHull import OnionHull
from SkyLines.SkyLine import SkyLine
from Utils import FileHandler

sys.setrecursionlimit(1500)


def run_hulls_only(samples):
        jm = JarvisMarch()
        jm.fit(samples)

        print("\nCompleted running Jarvis March on the Data")
        print("Inputs : ", len(samples))
        print("Peels Generated: ", len(jm.hull))
        print("Execution time : ", jm.exec_time)
        print("Hull(%s): " % len(jm.hull), jm.hull)
        print("Saving output ... ")
        FileHandler.saveOutput("Outputs/JarvisMarch.txt", jm.hull)

        gs = GrahamScan()
        gs.fit(samples)
        print("\nCompleted running Graham Scan on the Data")
        print("Inputs : ", len(samples))
        print("Peels Generated: ", len(gs.hull))
        print("Execution time : ", gs.exec_time)
        print("Hull(%s): " % len(gs.hull), gs.hull)
        print("Saving output ... ")
        FileHandler.saveOutput("Outputs/GrahamScan.txt", jm.hull)

        qh = QuickHull()
        qh.fit(samples)
        print("\nCompleted running Quick Hull on the Data")
        print("Inputs : ", len(samples))
        print("Peels Generated: ", len(qh.hull))
        print("Execution time : ", qh.exec_time)
        print("Hull(%s): " % len(qh.hull), qh.hull)
        print("Saving output ... ")
        FileHandler.saveOutput("Outputs/QuickHull.txt", jm.hull)


def run_onion_hulls(samples):
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


def run_skylines(samples):
        sk = SkyLine(3)
        sk.match(samples)


FileHandler.createTestFile(100000)
test_cases, samples = FileHandler.readFile('Inputs/sample.txt')
run_hulls_only(samples)
