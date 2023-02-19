import random

data = ['T♠', 'T♥', 'T♧', 'T♢',
        'K♠', 'K♥', 'K♧', 'K♢',
        'Q♠', 'Q♥', 'Q♧', 'Q♢',
        'J♠', 'J♥', 'J♧', 'J♢',
        '10♠', '10♥', '10♧', '10♢',
        '9♠', '9♥', '9♧', '9♢',
        '9♠', '9♥', '9♧', '9♢',
        '8♠', '8♥', '8♧', '8♢',
        '7♠', '7♥', '7♧', '7♢',
        '6♠', '6♥', '6♧', '6♢']

game_list_1 = []
game_list_2 = [['⊠' for _ in range(10)] for _ in range(4)]
for i in range(4):
    row = []
    for j in range(10):
        card = random.choice(data)
        row.append(card)
        data.remove(card)
    game_list_1.append(row)

while True:
    try:
        x_1, y_1 = input('Выберите первую карту, введя номер ряда и столбца через пробел: ').split()
        x_2, y_2 = input('Выберите вторую карту, введя номер ряда и столбца через пробел: ').split()
        if x_1 == x_2 and y_1 == y_2:
            raise ArithmeticError
        if game_list_2[int(x_1) - 1][int(y_1) - 1] == ' ' or game_list_2[int(x_2) - 1][int(y_2) - 1] == ' ':
            raise ValueError
        game_list_2[int(x_1) - 1][int(y_1) - 1] = game_list_1[int(x_1) - 1][int(y_1) - 1]
        game_list_2[int(x_2) - 1][int(y_2) - 1] = game_list_1[int(x_2) - 1][int(y_2) - 1]
    except ArithmeticError:
        print('Выберите разные карты!')
        continue
    except Exception:
        print('Некорректный ввод!')
        continue
    print(' \t' + '\t'.join([str(i) for i in range(1, 11)]))
    for i, row in enumerate(game_list_2):
        print(str(i + 1), ' ', '\t'.join(row))
    if game_list_2[int(x_1) - 1][int(y_1) - 1][:-1] == game_list_2[int(x_2) - 1][int(y_2) - 1][:-1]:
        print('Отлично, Вы угадали 2 карты!')
        game_list_1[int(x_1) - 1][int(y_1) - 1] = ' '
        game_list_1[int(x_2) - 1][int(y_2) - 1] = ' '
        game_list_2[int(x_1) - 1][int(y_1) - 1] = ' '
        game_list_2[int(x_2) - 1][int(y_2) - 1] = ' '
        print(' \t' + '\t'.join([str(i) for i in range(1, 11)]))
        for i, row in enumerate(game_list_2):
            print(str(i + 1), ' ', '\t'.join(row))
    else:
        game_list_2[int(x_1) - 1][int(y_1) - 1] = '⊠'
        game_list_2[int(x_2) - 1][int(y_2) - 1] = '⊠'

    flag = True
    for row in game_list_2:
        for col in row:
            if col != ' ':
                flag = False
    if flag:
        break


print('Вы победили!')



