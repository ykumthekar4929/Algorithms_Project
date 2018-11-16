import numpy as np
from Utils import InputGenerator


def readFile(filename):
        raw_lines = open(filename).read().splitlines()
        test_cases = raw_lines[0]
        points = []
        for line in raw_lines[1:]:
                curr = line.split(",")
                new_row = [float(x.strip()) for x in curr]
                points.append(new_row)

        points = np.array(points)
        x = 0
        y = 2
        points.T[[x, y]] = points.T[[y, x]]
        return int(test_cases), np.array(points)


def createTestFile(num, name = "Inputs/sample.txt"):
        f = open(name, "w+")
        f.write("%s\n"%(num))
        samples = InputGenerator.inputGenerator(num)
        ids = [[x] for x in range(1, num + 1)]
        samples = np.append(samples, ids, axis=1)
        for row in samples:
                _row = "%s, %s, %s\n"%(row[2], row[1], row[0])
                f.write(_row)
        f.close()


def saveOutput(name, hull):
        f = open(name, 'w+')
        for row in hull:
                f.write("%s, %s, %s\n"%(row[2], row[0], row[1]))
        f.close()
