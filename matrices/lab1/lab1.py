import numpy as np
import time

def ijk(first, second, SIZE):
    sum = 0
    multiply = np.zeros((size, size))
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            for k in range(0, SIZE):
                sum += first[i][k]*second[k][j]
            multiply[i][j] = sum
            sum = 0
    return 0

sizes = [10, 100, 1000]
algorithms = [ijk]

for size in sizes:
    first = np.random.rand(size, size)
    second = np.random.rand(size, size)
    for algorithm in algorithms:
        start = time.time()
        algorithm(first, second, size)
        stop = time.time()
        print(algorithm.__name__ + " / " + str(size) + ": " + str(stop - start))