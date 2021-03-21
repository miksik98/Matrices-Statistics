def norm_p(matrix, p):
    n = len(matrix)
    if n == 0:
        return 0
    if n != len(matrix[0]):
        raise ValueError("Not square matrix provided: " + matrix)
    sums = []
    for row in matrix:
        sum = 0
        for number in row:
            sum += number ** p
        sums.append(sum)
    return max(sums) ** (1 / p)


def norm_max(matrix):
    n = len(matrix)
    if n == 0:
        return 0
    if n != len(matrix[0]):
        raise ValueError("Not square matrix provided: " + matrix)
    sums = []
    for i in range(len(matrix[0])):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[i][j]
        sums.append(sum)
    return max(sums)


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
    return [[matrix[1][1]/det, -matrix[1][0]/det], [-matrix[0][1]/det, matrix[0][0]/det]]


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
    return [[c00, c10, c20],
            [c01, c11, c21],
            [c02, c12, c22]]


A = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

B = [[1, 2], [3, 4]]
print(norm_p(A, 1))
print(norm_max(A))
print(det_3(A))
print(det_2(B))
print(inverse_2(B))
print(inverse_3(A))
