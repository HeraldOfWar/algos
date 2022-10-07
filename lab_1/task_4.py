# import numpy as n
import sys


def check_matrix(m):
    for line in m[1:]:
        if len(line) != len(m[0]):
            raise TypeError
    if len(m) != len(m[0]) or len(m) != 3:
        raise TypeError


def check_squareness(A):
    if len(A) != len(A[0]):
        raise ArithmeticError("Matrix must be square to inverse.")


def determinant(A, total=0):
    indices = list(range(len(A)))

    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    for fc in indices:
        As = copy_matrix(A)
        As = As[1:]
        height = len(As)
        builder = 0

        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc + 1:]

        sign = (-1) ** (fc % 2)
        sub_det = determinant(As)
        total += A[0][fc] * sign * sub_det

    return total


def check_non_singular(A):
    det = determinant(A)
    if det != 0:
        return det
    else:
        raise ArithmeticError("Singular Matrix!")


def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M


def identity_matrix(n):
    I = zeros_matrix(n, n)
    for i in range(n):
        I[i][i] = 1.0

    return I


def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC


def print_matrix(M):
    for row in M:
        print([round(x, 3) + 0 for x in row])


def transpose(M):
    t_matrix = []
    for i in range(len(M[0])):
        new_line = []
        for line in M:
            new_line.append(line[i])
        t_matrix.append(new_line)
    return t_matrix


def matrix_multiply(A, B):
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        raise ArithmeticError('Number of A columns must equal number of B rows.')

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C


def check_matrix_equality(a, b, tol=None):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False
    for i in range(len(a)):
        for j in range(len(a[0])):
            if tol == None:
                if a[i][j] != b[i][j]:
                    return False
            else:
                if round(a[i][j], tol) != round(b[i][j], tol):
                    return False

    return True


def invert_matrix(A, tol=None):
    check_squareness(A)
    check_non_singular(A)

    n = len(A)
    AM = copy_matrix(A)
    I = identity_matrix(n)
    IM = copy_matrix(I)

    indices = list(range(n))
    for fd in range(n):
        fdScaler = 1, 0 / AM[fd][fd]
        for j in range(n):
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        for i in indices[0:fd] + indices[fd + 1:]:
            crScaler = AM[i][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

    # Section 4: Make sure that IM is an inverse of A within the specified tolerance
    if check_matrix_equality(I, matrix_multiply(A, IM), tol):
        return IM
    else:
        raise ArithmeticError("Matrix inverse out of tolerance.")


print('Please, enter 3x3 matrix in the following format (for example):'
      '\n1 2 3\n4 5 6\n7 8 9 (press Enter and Ctrl+D to finish)')

try:
    matrix = [[int(i) for i in line.strip().split()] for line in sys.stdin.read().strip().split('\n')]
    check_matrix(matrix)
    print('Inversed matrix by me:')
    print_matrix(matrix)
    # print('Inversed matrix by numpy: ')
    # for line in np.linalg.inv(np.array(matrix)):
    #     for i in line:
    #         print(i, end=' ')
    #     print()
except ValueError:
    print('Invalid input format!')
except TypeError:
    print('Invalid matrix format!')
sys.exit(0)
