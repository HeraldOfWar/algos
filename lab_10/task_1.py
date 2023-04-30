from operator import itemgetter

data = []
for i in range(int(input('Введите количество экспонатов: '))):
    a, b = map(int, input('Введите вес и цену экспоната через пробел: ').split())
    data.append((a, b, b / a))
data.sort(key=itemgetter(2, 0), reverse=True)
m, k = map(int, input('Введите количество заходов и максимальный вес, который может унести вор за раз, через пробел: '))

ans = 0
for i in range(m):
    curr_w = k
    new_data = data.copy()
    for j in range(len(data)):
        if data[j][0] <= curr_w:
            curr_w -= data[j][0]
            ans += data[j[1]]
            del new_data[j]
    data = new_data.copy()

print('Максимальная сумма украденного:', ans)