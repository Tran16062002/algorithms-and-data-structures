import unittest


def add_polynomials(A, B):
    return [a + b for a, b in zip(A, B)] + A[len(B):] + B[len(A):]


def multiplication(A, B):
    n = len(A)

    if n == 1:
        return [A[0] * B[0]]

    m = n // 2

    A1, A0 = A[:m], A[m:]
    B1, B0 = B[:m], B[m:]

    P1 = multiplication(A1, B1)
    P2 = multiplication(A0, B0)
    P3 = multiplication(add_polynomials(A1, A0), add_polynomials(B1, B0))

    result = [0] * (2 * n - 1)

    for i in range(len(P1)):
        result[i] += P1[i]

    for i in range(len(P2)):
        result[i + 2 * m] += P2[i]

    for i in range(len(P3)):
        result[i + m] += P3[i] - (P1[i] if i < len(P1) else 0) - (P2[i] if i < len(P2) else 0)

    return result


class TestPolynomialOperations(unittest.TestCase):

    def test_add_polynomials_equal_length(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        result = add_polynomials(A, B)
        self.assertEqual(result, [5, 7, 9])

    def test_add_polynomials_different_length(self):
        A = [1, 2]
        B = [3, 4, 5]
        result = add_polynomials(A, B)
        self.assertEqual(result, [4, 6, 5])  # [1 + 3, 2 + 4, 5]

    def test_multiplication_single_terms(self):
        A = [2]
        B = [3]
        result = multiplication(A, B)
        self.assertEqual(result, [6])  # 2 * 3 = 6

    def test_multiplication_two_terms(self):
        A = [1, 2]  # 1 + 2x
        B = [3, 4]  # 3 + 4x
        result = multiplication(A, B)
        self.assertEqual(result, [3, 10, 8])  # 3 + 10x + 8x^2

    def test_multiplication_more_terms(self):
        A = [1, 2, 3]  # 1 + 2x + 3x^2
        B = [4, 5, 6]  # 4 + 5x + 6x^2
        result = multiplication(A, B)
        self.assertEqual(result, [4, 13, 28, 27, 18])

    def test_multiplication_with_zeros(self):
        A = [0, 1]
        B = [0, 2]
        result = multiplication(A, B)
        self.assertEqual(result, [0, 0, 2])  # 0 polynomial


if __name__ == '__main__':
    unittest.main()