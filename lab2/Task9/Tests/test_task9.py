import unittest


def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    P1 = strassen(A11, subtract_matrices(B12, B22))
    P2 = strassen(add_matrices(A11, A12), B22)
    P3 = strassen(add_matrices(A21, A22), B11)
    P4 = strassen(A22, subtract_matrices(B21, B11))
    P5 = strassen(add_matrices(A11, A22), add_matrices(B11, B22))
    P6 = strassen(subtract_matrices(A12, A22), add_matrices(B21, B22))
    P7 = strassen(subtract_matrices(A11, A21), add_matrices(B11, B12))

    C11 = add_matrices(subtract_matrices(add_matrices(P5, P4), P2), P6)
    C12 = add_matrices(P1, P2)
    C21 = add_matrices(P3, P4)
    C22 = subtract_matrices(add_matrices(P5, P1), add_matrices(P3, P7))

    # result
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C


def next_size(n):
    from math import log2, floor
    num = floor(log2(n))
    if n == pow(2, num):
        size = n
        return size
    else:
        size = int(pow(2, num + 1))
        return size


def pad_matrix(A, size):
    padded = [[0] * size for _ in range(size)]
    for i in range(len(A)):
        for j in range(len(A[i])):
            padded[i][j] = A[i][j]
    return padded


class TestMatrixOperations(unittest.TestCase):

    def test_add_matrices(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        result = add_matrices(A, B)
        expected = [[6, 8], [10, 12]]
        self.assertEqual(result, expected)

    def test_subtract_matrices(self):
        A = [[5, 6], [7, 8]]
        B = [[1, 2], [3, 4]]
        result = subtract_matrices(A, B)
        expected = [[4, 4], [4, 4]]
        self.assertEqual(result, expected)

    def test_strassen_single_element(self):
        A = [[2]]
        B = [[3]]
        result = strassen(A, B)
        expected = [[6]]  # 2 * 3
        self.assertEqual(result, expected)

    def test_strassen_2x2(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        result = strassen(A, B)
        expected = [[19, 22], [43, 50]]  # Result of 2x2 matrix multiplication
        self.assertEqual(result, expected)

    def test_strassen_4x4(self):
        A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        B = [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
        result = strassen(A, B)
        expected = [[80, 70, 60, 50], [240, 214, 188, 162],
                    [400, 358, 316, 274], [560, 502, 444, 386]]  # Example expected result
        self.assertEqual(result, expected)

    def test_pad_matrix(self):
        A = [[1, 2], [3, 4]]
        size = 4
        result = pad_matrix(A, size)
        expected = [[1, 2, 0, 0], [3, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()