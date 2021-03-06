import numpy as np
import time


# i -> m
# j -> n
# k -> l

def jki(first, second, m, n, l):
    multiply = np.zeros((m, n))
    for j in range(0, n):
        for k in range(0, l):
            for i in range(0, n):
                multiply[i][j] += first[i][k] * second[k][j]
    return multiply


def jik(first, second, m, n, l):
    multiply = np.zeros((m, n))
    for j in range(0, n):
        for i in range(0, m):
            for k in range(0, l):
                multiply[i][j] += first[i][k] * second[k][j]
    return multiply


def kij(first, second, m, n, l):
    multiply = np.zeros((m, n))
    for k in range(0, l):
        for i in range(0, m):
            for j in range(0, n):
                multiply[i][j] += first[i][k] * second[k][j]
    return multiply


def kji(first, second, m, n, l):
    multiply = np.zeros((m, n))
    for k in range(0, l):
        for j in range(0, n):
            for i in range(0, m):
                multiply[i][j] += first[i][k] * second[k][j]
    return multiply


def ijk(first, second, m, n, l):
    multiply = np.zeros((m, n))
    for i in range(0, m):
        for j in range(0, n):
            for k in range(0, l):
                multiply[i][j] += first[i][k] * second[k][j]
    return multiply


def ikj(first, second, m, n, l):
    multiply = np.zeros((m, n))
    for i in range(0, m):
        for j in range(0, n):
            for k in range(0, l):
                multiply[i][j] += first[i][k] * second[k][j]
    return multiply


sizes = [10, 100, 200]
algorithms = [ijk, ikj, kij, kji, jki, jik]

for size in sizes:
    first = np.random.rand(size, size)
    second = np.random.rand(size, size)
    for algorithm in algorithms:
        start = time.time()
        algorithm(first, second, size, size, size)
        stop = time.time()
        print(algorithm.__name__ + " / " + str(size) + ": " + str(stop - start))