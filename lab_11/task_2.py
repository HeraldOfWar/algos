m, n = map(int, input('Введите размеры матрицы MxN через пробел: ').split())
matrix = []
for i in range(m):
    matrix.append(list(map(int, input('Введите элементы строки матрицы по возрастанию через пробел: ').split())))
    print(matrix[i])
x = int(input('Введите искомый элемент матрицы: '))

flag = True
for i in range(m):
    if matrix[i][0] <= x <= matrix[i][-1]:
        for j in range(n):
            if matrix[i][j] == x:
                print(i + 1, j + 1)
                flag = False
                break
if flag:
    print(-1, -1)