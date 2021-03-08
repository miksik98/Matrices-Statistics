import numpy as np


def simple_gauss(A, B, n):
    x = np.zeros(n)
    for i in range(n):
        if A[i][i] == 0:
            raise Exception("0 value is forbidden on diagonal. Found 0 at {}".format(i))
        for j in range(i + 1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(n):
                A[j][k] -= ratio * A[i][k]
            B[j] -= ratio * B[i]
    x[n - 1] = B[n - 1] / A[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = B[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] = x[i] / A[i][i]
    return x


def gauss_pivoting(A, B, n):
    x = np.zeros(n)
    for i in range(n):
        max = abs(A[i][i])
        row = i

        for k in range(i + 1, n):
            if abs(A[k][i]) > max:
                max = abs(A[k][i])
                row = k
        if row != i:
            A[row], A[i] = A[i].copy(), A[row].copy()
            B[i], B[row] = B[row], B[i]

        for k in range(i + 1, n):
            ratio = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= ratio * A[i][j]
            B[k] -= ratio * B[i]

    x[n - 1] = B[n - 1] / A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = B[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] = x[i] / A[i][i]
    return x


A = [[-1, 2, 1], [1, -3, -2], [3, -1, -1]]
B = [-1, -1, 4]
print(simple_gauss(A, B, 3))
print(gauss_pivoting(A, B, 3))
