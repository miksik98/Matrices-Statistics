import numpy as np


# import matplotlib.pyplot as pt


def det_2(matrix):
    if len(matrix) not in [0, 2] or len(matrix[0]) != 2:
        raise ValueError("Not 2x2 matrix provided: " + matrix)
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def det_3(matrix):
    if len(matrix) not in [0, 3] or len(matrix[0]) != 3:
        raise ValueError("Not 3x3 matrix provided: " + matrix)
    return matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) - matrix[0][1] * (
            matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) + matrix[0][2] * (
                   matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])


def inverse_2(matrix):
    if len(matrix) not in [0, 2] or len(matrix[0]) != 2:
        raise ValueError("Not 2x2 matrix provided: " + matrix)
    det = det_2(matrix)
    return np.array([[matrix[1][1] / det, -matrix[1][0] / det], [-matrix[0][1] / det, matrix[0][0] / det]])


def inverse_3(matrix):
    if len(matrix) not in [0, 3] or len(matrix[0]) != 3:
        raise ValueError("Not 3x3 matrix provided: " + matrix)
    m = matrix
    det = det_3(m)
    c00 = det_2([[m[1][1], m[1][2]], [m[2][1], m[2][2]]]) / det
    c01 = -det_2([[m[1][0], m[1][2]], [m[2][0], m[2][2]]]) / det
    c02 = det_2([[m[1][0], m[1][1]], [m[2][0], m[2][1]]]) / det
    c10 = -det_2([[m[0][1], m[0][2]], [m[2][1], m[2][2]]]) / det
    c11 = det_2([[m[0][0], m[0][2]], [m[2][0], m[2][2]]]) / det
    c12 = -det_2([[m[0][0], m[0][1]], [m[2][0], m[2][1]]]) / det
    c20 = det_2([[m[0][1], m[0][2]], [m[1][1], m[1][2]]]) / det
    c21 = -det_2([[m[0][0], m[0][2]], [m[1][0], m[1][2]]]) / det
    c22 = det_2([[m[0][0], m[0][1]], [m[1][0], m[1][1]]]) / det
    return np.array([[c00, c10, c20],
                     [c01, c11, c21],
                     [c02, c12, c22]])


def norm_p(x, p):
    return np.sum(np.abs(x) ** p, axis=0) ** (1 / p)


def norm_max(x, _p):
    return np.max(np.abs(x), axis=0)


def matrix_p_norm(A, dim, p):
    if p <= 2 or p == np.inf:
        print('ref: ' + str(np.linalg.norm(A, p)))

    x = np.random.randn(dim, 10000)
    norm = norm_p if p < np.inf else norm_max
    normalized_xs = x / norm(x, p)
    A_x = A.dot(normalized_xs)
    # pt.plot(normalized_xs[0], normalized_xs[1], "o", label="x")
    # pt.plot(A_x[0], A_x[1], "o", label="Ax")
    # pt.legend()
    # pt.gca().set_aspect("equal")
    # pt.show()
    print('calc: ' + str(np.max(norm(A_x, p))) + '\n')


def calc(dim, p):
    A = np.random.randn(dim, dim)
    print(f'{dim}x{dim} p={p}')
    matrix_p_norm(A, dim, p)

    if dim == 2:
        A_inv = inverse_2(A)
    else:
        A_inv = inverse_3(A)
    print(f'inverted {dim}x{dim} p={p}')
    matrix_p_norm(A_inv, dim, p)


calc(2, 1)
calc(2, 2)
calc(2, 3)
calc(2, np.inf)
calc(3, 1)
calc(3, 2)
calc(3, 3)
calc(3, np.inf)
