import numpy as np
from numpy.linalg import norm, svd

from random import normalvariate
from math import sqrt


def random_v(n):
    unnormalized = [normalvariate(0, 1) for _ in range(n)]
    theNorm = sqrt(sum(x * x for x in unnormalized))
    return np.array([x / theNorm for x in unnormalized])


def svd_1d(A, epsilon):
    n, m = A.shape
    x = random_v(n)
    currentV = x

    while True:
        lastV = currentV
        currentV = np.dot(A, lastV)
        currentV = currentV / norm(currentV)

        if norm(currentV - lastV) < epsilon:
            return currentV


def svd_(A, epsilon):
    A = np.array(A, dtype=float)
    n, m = A.shape
    svdSoFar = []
    k = min(n, m)

    for i in range(k):
        matrixFor1D = A.copy()

        for singularValue, u, v in svdSoFar[:i]:
            matrixFor1D -= singularValue * np.outer(u, v)

        v = svd_1d(matrixFor1D, epsilon)
        u_unnormalized = np.dot(A, v)
        sigma = norm(u_unnormalized)
        u = u_unnormalized / sigma
        svdSoFar.append((sigma, u, v))

    singularValues, us, vs = [np.array(x) for x in zip(*svdSoFar)]
    return us.T, singularValues, vs

def print_solution(U, s, Vh, name):
    print(name)
    print("U -> " + str(U))
    print("s -> " + str(s))
    print("Vh -> " + str(Vh) + "\n")


matrix = np.array([
    [2, -1, 0],
    [-1, 2, -1],
    [0, -1, 2],
], dtype='float64')

U_, s_, Vh_ = svd_(matrix, 0.001)
print_solution(U_, s_, Vh_, "our solution")

U, s, Vh = svd(matrix)
print_solution(U, s, Vh, "numpy solution")
