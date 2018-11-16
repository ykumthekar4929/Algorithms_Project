DAA Project

Implemented Convex Hull, Onion Hull and Skylines with Convex hulls

Requirements:
    Python 3, Numpy, matplotlib, Pandas

Running Instructions:
    python main.py -T <type> -F <sample_file_name>

Arguments:
T - Type of Run to make

    1 For running only the convex hull algorithms
    2 For running only the Onion Hull algorithm
    3 For running only Skylines algorithm
    4 For Running the Circle detector
    5 For running 1, 2, 3 together

F - Input sample file name defaults to a sample file in Input folder, for circle detector the data is generated on the fly.

Outputs are stored in the Outputs folder
Experiment
Developed a Circle detector based on convex hull, predicts if the given set of points forms a circle or not.
