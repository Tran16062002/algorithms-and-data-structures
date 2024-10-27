from time import perf_counter
from math import *


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


t1_start = perf_counter()

if __name__ == "__main__":
    with open('input.txt', 'r') as infile:
        n = int(infile.readline())
        data = infile.readline().split()
        A_values = list(map(int, data[:n * n]))
        A = [A_values[i * n:(i + 1) * n] for i in range(n)]
        B_values = list(map(int, data[n * n:]))
        B = [B_values[i * n:(i + 1) * n] for i in range(n)]

    size = next_size(n)
    A_padded = pad_matrix(A, size)
    B_padded = pad_matrix(B, size)
    C_padded = strassen(A_padded, B_padded)
    result = [row[:n] for row in C_padded[:n]]
    # print(result)

    with open('output.txt', 'w') as outfile:
        for row in result:
            outfile.write(' '.join(map(str, row)) + '\n')

t1_stop = perf_counter()
print('Время работы: %s секунд ' % (t1_stop - t1_start))