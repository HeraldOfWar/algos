s = input()
s1 = [i for i in s]
c = 0

for i in range(len(s) - 1):
    if s[i] == 'W' and s[i + 1] == 'B':
        c += 2
        s1.remove('W')
        s1.remove('B')

while True:
    flag1, flag2 = False, False
    for i in s1:
        if i == 'W':
            flag1 = True
        if flag1 and i == 'B':
            flag2 = True
    if flag2:
        c += 2
        s1.remove('B')
        s1.remove('W')
    else:
        break

if len(s) == 0:
    print(f'{c}\nНИКОГО НЕ ОСТАЛОСЬ')
else:
    print(f'{c}\n{"".join(s1)}')
