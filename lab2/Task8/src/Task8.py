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


# result
if __name__ == "__main__":
    with open('input.txt', 'r') as infile:
        n = int(infile.readline())
        data_a = str(infile.readline())
        data_b = str(infile.readline())

    A = [int(i) for i in data_a.split()]
    B = [int(i) for i in data_b.split()]

    arr = multiplication(A, B)
    result = ' '.join(str(i) for i in arr)

    with open('output.txt', 'w') as outfile:
        outfile.write(result)