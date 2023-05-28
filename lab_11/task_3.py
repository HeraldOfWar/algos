import numpy as np


def queens(size):
    def under_attack(col, queen):
        return col in queen or any(abs(col - x) == len(queen) - i for i, x in enumerate(queen))

    def solve(n):
        ss = [[]]
        for j in range(n):
            ss = [s + [i + 1] for s in ss for i in range(n) if not under_attack(i + 1, s)]
            print(ss)
        return ss

    for i in np.array(solve(size)):
        np.sort(i)
        print(i)


queens(8)

