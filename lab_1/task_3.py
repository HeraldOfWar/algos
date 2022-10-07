# import numpy as np
import sys


def check_matrix(m, name):
    for line in m[1:]:
        if len(line) != len(m[0]):
            raise TypeError
    if max(len(m[0]), len(m)) <= 3:
        print(f'The rank of matrix {name} is equal to {np.linalg.matrix_rank(np.array(m))}.')


print('Please, enter two matrices in the following format (for example):'
      '\n1 2 3\n4 5 6\n7 8 9\n ...\nn n+1 n+2\n---'
      '\n-1 -2 -3\n-4 -5 -6\n  ...\n-n -n-1 -n-2 (press Enter and Ctrl+D to finish)')

try:
    matrices = [[[int(i) for i in line.strip().split()] for line in matrix.strip().split('\n')] for matrix in
                sys.stdin.read().strip().split('---') if matrix]
    matrix_1, matrix_2 = np.array(matrices[0]), np.array(matrices[1])
    m1, m2 = tuple(matrices)
    check_matrix(m1, 'A')
    print('Transposed matrix A:')
    for line in np.transpose(matrix_1):
        for i in line:
            print(i, end=' ')
        print()
    check_matrix(matrix_2, 'B')
    print('Transposed matrix B:')
    for line in np.transpose(matrix_2):
        for i in line:
            print(i, end=' ')
        print()
    print('The result of multiplying matrix A by matrix B:')
    for line in np.dot(matrix_1, matrix_2):
        for i in line:
            print(i, end=' ')
        print()
    print('The result of multiplying matrix B by matrix A:')
    for line in np.dot(matrix_2, matrix_1):
        for i in line:
            print(i, end=' ')
        print()
except ValueError:
    print('Invalid input format!')
except TypeError:
    print('Invalid matrix format!')
except ArithmeticError:
    print('It is impossible to multiply these matrices!')
sys.exit(0)
