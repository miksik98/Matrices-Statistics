import numpy as np
import time


def jki(first, second, SIZE):
    multiply = np.zeros((SIZE, SIZE))
    for j in range(0, SIZE):
        for k in range(0, SIZE):
            for i in range(0, SIZE):
                multiply[i][j] += first[i][k] * second[k][j]
    return multiply


def jik(first, second, SIZE):
    multiply = np.zeros((SIZE, SIZE))
    for j in range(0, SIZE):
        for i in range(0, SIZE):
            for k in range(0, SIZE):
                multiply[i][j] += first[i][k] * second[k][j]
    return multiply


def kij(first, second, SIZE):
    multiply = np.zeros((SIZE, SIZE))
    for k in range(0, SIZE):
        for i in range(0, SIZE):
            for j in range(0, SIZE):
                multiply[i][j] += first[i][k] * second[k][j]
    return multiply


def kji(first, second, SIZE):
    multiply = np.zeros((SIZE, SIZE))
    for k in range(0, SIZE):
        for j in range(0, SIZE):
            for i in range(0, SIZE):
                multiply[i][j] += first[i][k] * second[k][j]
    return multiply


def ijk(first, second, SIZE):
    multiply = np.zeros((SIZE, SIZE))
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            for k in range(0, SIZE):
                multiply[i][j] += first[i][k] * second[k][j]
    return multiply


def ikj(first, second, SIZE):
    multiply = np.zeros((SIZE, SIZE))
    for i in range(0, SIZE):
        for k in range(0, SIZE):
            for j in range(0, SIZE):
                multiply[i][j] += first[i][k] * second[k][j]
    return multiply


sizes = [10, 100, 1000]
algorithms = [ijk, ikj, kij, kji, jki, jik]

for size in sizes:
    first = np.random.rand(size, size)
    second = np.random.rand(size, size)
    for algorithm in algorithms:
        start = time.time()
        algorithm(first, second, size)
        stop = time.time()
        print(algorithm.__name__ + " / " + str(size) + ": " + str(stop - start))
