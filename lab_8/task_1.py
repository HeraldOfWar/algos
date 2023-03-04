from random import randint, uniform


def hash_multi(table: dict, key: int, const: float, text: str) -> str:
    result = ''
    n = key * const
    for t in text:
        hash_key = int(len(table.items()) * n)
        table[hash_key] = t
        result += str(hash_key)
    return result


def hash_crc32(s: str) -> str:
    return s


s = input('Введите текст, который нужно захэшировать: ')
hash_table = {}
k, c = randint(1, 1000), uniform(0, 1)
print('Хэшированный текст (умножение):', hash_multi(hash_table, k, c, s))
print('Хэшированный текст (CRC-32):')