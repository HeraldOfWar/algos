import sys


def check_matrix(A, name):
    for line in A[1:]:
        if len(line) != len(A[0]):
            raise TypeError
    if max(len(A[0]), len(A)) <= 3:
        print(f'The rank of matrix {name} is equal to {rank(A, min(len(A[0]), len(A)))}.')


def det(A, size):
    if size == 1:
        for line in A:
            for i in line:
                if i != 0:
                    return 1
        return 0
    if size == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    if size == 3:
        return (A[0][0] * A[1][1] * A[2][2] + A[0][1] * A[1][2] * A[2][0] + A[0][2] * A[1][0] * A[2][1]) - \
               (A[0][0] * A[1][2] * A[2][1] + A[0][1] * A[1][0] * A[2][2] + A[0][2] * A[1][1] * A[2][0])


def rank(A, max_rank):
    if max_rank == 1:
        if det(A, 1):
            return 1
        return 0
    elif max_rank == 2:
        if not det(A, 1):
            return 0
        if len(A) == len(A[0]) == 2:
            if det(A, 2):
                return 2
            return 1
        if len(A) == 3:
            if det(A[:2], 2) or det(A[1:], 2):
                return 2
            return 1
        if len(A[0]) == 3:
            m1, m2 = [], []
            for i in range(2):
                m1.append(A[i][:3])
            for i in range(2):
                m2.append(A[i][1:])
            if det(m1, 2) or det(m2, 2):
                return 2
            return 2
    elif max_rank == 3:
        if not det(A, 1):
            return 0
        if len(A) == len(A[0]) == 3:
            if det(A, 3):
                return 3
            m1, m2, m3, m4 = [], [], [], []
            for i in range(2):
                m1.append(A[i][:3])
                m2.append(A[i][1:])
            for i in range(1, 3):
                m3.append(A[i][:3])
                m4.append(A[i][1:])
            if det(m1, 2) or det(m2, 2) or det(m3, 2) or det(m4, 2):
                return 2
            return 1
        if len(A) == 4:
            if det(A[:3], 3) or det(A[1:], 3):
                return 3
            m1, m2, m3, m4, m5, m6 = [], [], [], [], [], []
            for i in range(2):
                m1.append(A[i][:2])
                m2.append(A[i][1:])
            for i in range(1, 3):
                m3.append(A[i][:2])
                m4.append(A[i][1:])
            for i in range(2, 4):
                m5.append(A[i][:2])
                m6.append(A[i][1:])
            if det(m1, 2) or det(m2, 2) or det(m3, 2) or det(m4, 2) or det(m5, 2) or det(m6, 2):
                return 2
            return 1
        if len(A[0]) == 4:
            m1, m2 = [], []
            for i in range(3):
                m1.append(A[i][:3])
            for i in range(3):
                m2.append(A[i][1:])
            if det(m1, 3) or det(m2, 3):
                return 3
            m4, m5, m6, m7, m8, m9 = [], [], [], [], [], []
            for i in range(2):
                m4.append(A[i][:2])
                m5.append(A[i][1:])
                m6.append(A[i][2:])
            for i in range(1, 3):
                m7.append(A[i][:2])
                m8.append(A[i][1:])
                m9.append(A[i][2:])
            if det(m4, 2) or det(m5, 2) or det(m6, 2) or det(m7, 2) or det(m8, 2) or det(m9, 2):
                return 2
            return 1


def transpose(A):
    t_matrix = []
    for i in range(len(A[0])):
        new_line = []
        for line in A:
            new_line.append(line[i])
        t_matrix.append(new_line)
    return t_matrix


def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M


def matrix_multiply(A, B):
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        raise ArithmeticError

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += A[i][k] * B[k][j]
            C[i][j] = total

    return C


def print_matrix(M):
    for row in M:
        print([round(x, 3) + 0 for x in row])


print('Please, enter two matrices in the following format (for example):'
      '\n1 2 3\n4 5 6\n7 8 9\n ...\nn n+1 n+2\n---'
      '\n-1 -2 -3\n-4 -5 -6\n  ...\n-n -n-1 -n-2 (press Enter and Ctrl+D to finish)')

try:
    matrices = [[[int(i) for i in line.strip().split()] for line in matrix.strip().split('\n')] for matrix in
                sys.stdin.read().strip().split('---') if matrix]
    matrix_1, matrix_2 = tuple(matrices)
    check_matrix(matrix_1, 'A')
    print('Transposed matrix A:')
    print_matrix(transpose(matrix_1))
    check_matrix(matrix_2, 'B')
    print('Transposed matrix B:')
    print_matrix(transpose(matrix_2))
    print('The result of multiplying matrix A by matrix B:')
    print_matrix(matrix_multiply(matrix_1, matrix_2))
    print('The result of multiplying matrix B by matrix A:')
    print_matrix(matrix_multiply(matrix_2, matrix_1))
except ValueError:
    print('Invalid input format!')
except TypeError:
    print('Invalid matrix format!')
except ArithmeticError:
    print('It is impossible to multiply these matrices!')
sys.exit(0)
