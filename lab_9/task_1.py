from operator import itemgetter
from random import shuffle


# n = int(input("Введите количество людей: "))
# data = []
# for elem in range(n):
#     a, b = map(int, input("Введите рост и количество людей перед ним: ").split())
#     data.append((a, b))

data = [[1, 0], [2, 0], [3, 0], [5, 0], [4, 1]]
n = len(data)
# data = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
data.sort(key=itemgetter(1, 0))

ans = []
for i in range(n):
    curr_height, curr_num = data[i][0], data[i][1]
    over_height_data = []

    for j in ans:
        if j[0] >= curr_height:
            over_height_data.append(j)

    if len(over_height_data) == curr_num:
        ans.append(data[i])
    else:
        num_of_height = curr_num
        for w in range(len(ans)):
            if ans[w][0] >= curr_num:
                num_of_height -= 1
            if num_of_height == 0:
                ans.insert(w + 1, data[i])
                break
print(ans)


