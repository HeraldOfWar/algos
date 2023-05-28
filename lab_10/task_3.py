from random import randint

data = [randint(-100, 100) for _ in range(10)]
print('Данный список:', data)

res = 0
for d in range(len(data) - 3):  # наивный
    for c in range(d + 1, len(data) - 2):
        for b in range(c + 1, len(data) - 1):
            for a in range(b + 1, len(data)):
                ans = data[a] - data[b] + data[c] - data[d]
                if ans > res:
                    res = ans
print('Ответ:', res)

a, b, c, d = 0, 0, 0, 0
res = float('inf')
for i in range(len(data) - 3):
    for j in range(i + 1, len(data) - 1):
        ans = data[i] + data[j]
        if ans < res:
            res = ans
            b, d = j, i
res = 0
for i in range(d + 1, b):
    for j in range(b + 1, len(data)):
        ans = data[i] + data[j]
        if ans > res:
            res = ans
            a, c = j, i
print('Ответ:', data[a] - data[b] + data[c] - data[d])

a, b, c, d = 0, 0, 0, 0
res = 0
for i in range(len(data) - 3):
    for j in range(i + 1, len(data) - 2):
        ans = data[j] - data[i]
        if ans > res:
            res = ans
            c, d = j, i
res = 0
for i in range(c + 1, len(data) - 1):
    for j in range(i + 1, len(data)):
        ans = data[j] - data[i]
        if ans > res:
            res = ans
            a, b = j, i
print('Ответ:', data[a] - data[b] + data[c] - data[d])
