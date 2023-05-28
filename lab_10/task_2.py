p = list(map(int, input('Введите размерности матриц через пробел: ').split()))
n = len(p) - 1
dp = [[0 for _ in range(n)] for _ in range(n)]

for s in range(1, n):
    for i in range(n - s):
        j = i + s
        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1])

print('Минимальное число скалярных операций:', dp[0][n - 1])