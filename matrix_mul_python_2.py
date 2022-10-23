import numpy as np
from timeit import timeit
from multiprocessing import Pool
import os


def mmul(matrix):
    for i in range(1000):
        matrix = matrix * matrix
    return matrix

if __name__ == '__main__':
    matrices = []
    for i in range(4):
        matrices.append(np.random.random_integers(100, size=(1000, 1000)))


    start_time = timeit(lambda: map(mmul, matrices), number=20)
    pool = Pool(8)
    os.system("taskset -p 0xff %d" % os.getpid())
    end_time = timeit(lambda: pool.map(mmul, matrices), number=20)
    print("Start Time - ",start_time)
    print("End Time - ",end_time)
    time_diff = end_time-start_time
    print("Time difference -  ", time_diff)