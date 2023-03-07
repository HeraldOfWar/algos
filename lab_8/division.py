from random import randint


def hash_div(table, text):
    result = ''
    for i in range(len(text)):
        hash_key = int(randint(1, 1000) % len(text))
        if hash_key not in table.keys():
            table[hash_key] = []
        table[hash_key].append(text[i])
        result += str(hash_key)
    return result


def dehash_div(table: dict, hash_text: str) -> str:
    result = ''
    i, curr_i = 0, 0
    while i < len(hash_text):
        if i == curr_i:
            i += 1
            if int(hash_text[i]) in table.keys() and table[int(hash_text[i])]:
                result += table[int(hash_text[i])].pop(0)
                curr_i = i
        else:
            i += 1
            if int(hash_text[curr_i:i]) in table.keys() and table[int(hash_text[curr_i:i])]:
                result += table[int(hash_text[curr_i:i])].pop(0)
                curr_i = i
    return result


s = input('Введите текст, который нужно хэшировать: ')
hash_table = {}
hash_s = hash_div(hash_table, s)
print('Хэшированный текст (деление):', hash_s)
print(hash_table)
print('Исходный текст (деление):', dehash_div(hash_table, hash_s))