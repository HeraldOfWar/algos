graph = {
    'Тверская улица': {'Страстной бульвар': 0.6, 'Охотный ряд': 1.2},
    'Страстной бульвар': {'Тверская улица': 0.6, 'Пушкинская площадь': 0.9},
    'Пушкинская площадь': {'Страстной бульвар': 0.9, 'Тверская улица': 1.4, 'Чкаловская улица': 1.2},
    'Чкаловская улица': {'Пушкинская площадь': 1.2, 'улица Арбат': 1.4},
    'улица Арбат': {'Чкаловская улица': 1.4, 'Смоленская площадь': 1.1},
    'Смоленская площадь': {'улица Арбат': 1.1, 'Кутузовский проспект': 1.5},
    'Кутузовский проспект': {'Смоленская площадь': 1.5, 'улица Новый Арбат': 1.3},
    'улица Новый Арбат': {'Кутузовский проспект': 1.3, 'Охотный ряд': 1.7},
    'Охотный ряд': {'Тверская улица': 1.2, 'улица Новый Арбат': 1.7}
}

while True:
    curr_street = input('Введите название московской улицы: ')
    if curr_street in graph.keys():
        break
    print('Такой улицы нет!')

streets = [curr_street] + [key for key in graph.keys() if key != curr_street]
dist_matrix = [[float('inf') for j in range(len(streets))] for i in range(len(streets))]
for i in range(len(streets)):
    for neighbour, dist in graph[streets[i]].items():
        dist_matrix[i][streets.index(neighbour)] = dist

paths = dict([(i, []) for i in range(len(streets))])
d = [float('inf') for _ in range(len(streets))]
d[0] = 0
d1 = [0 for _ in range(len(d))]
prev_y, y, inds = 0, 0, [i for i in range(1, len(streets))]
for _ in range(len(streets) - 1):
    l1, l2 = [], []
    for x in inds:
        d[x] = min(d[x], d[y] + dist_matrix[y][x])
        l1.append(d[x])
        l2.append(x)
        if d[x] == d[y] + dist_matrix[y][x]:
            d1[x] = y
    y = l2[l1.index(min(l1))]
    inds.remove(y)
    paths[d1[y]].append(y)

for i in range(1, len(streets)):
    res, k = [0, i], i
    while k != 0:
        for key, item in paths.items():
            if k in item and key == 0:
                k = key
                break
            elif k in item:
                k = key
                res.insert(-2, k)
                break
    res = list(map(lambda x: streets[x], res))
    print(' -> '.join(res))

