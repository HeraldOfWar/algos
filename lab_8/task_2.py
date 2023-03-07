def xor(a, b):
    # initialize result
    result = []

    # Traverse all bits, if bits are
    # same, then XOR is 0, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


# Performs Modulo-2 division
def mod2div(dividend, divisor):
    # Number of bits to be XORed at a time.
    pick = len(divisor)

    # Slicing the dividend to appropriate
    # length for particular step
    tmp = dividend[0:pick]

    while pick < len(dividend):

        if tmp[0] == '1':

            # replace the dividend by the result
            # of XOR and pull 1 bit down
            tmp = xor(divisor, tmp) + dividend[pick]

        else:  # If leftmost bit is '0'

            # If the leftmost bit of the dividend (or the
            # part used in each step) is 0, the step cannot
            # use the regular divisor; we need to use an
            # all-0s divisor.
            tmp = xor('0' * pick, tmp) + dividend[pick]

        # increment pick to move further
        pick += 1

    # For the last n bits, we have to carry it out
    # normally as increased value of pick will cause
    # Index Out of Bounds.
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword


# Function used at the sender side to encode
# data by appending remainder of modular division
# at the end of data.
def encode_data(data, key):
    l_key = len(key)

    # Appends n-1 zeroes at end of data
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)

    # Append remainder in the original data
    codeword = data + remainder
    return codeword


s = input('Введите текст, который нужно хэшировать: ')
data = ''.join(format(ord(x), 'b') for x in s)
crc = '00000100110000010001110110110111'
ans = encode_data(data, crc)
print('Хэшированный текст (CRC-32):', data)
print('Хэшированный текст (CRC-32):', ans)


# table = []
# for byte in range(256):
#     crc = 0
#     for bit in range(8):
#         if (byte ^ crc) & 1:
#             crc = (crc >> 1) ^ 0xEDB88320
#         else:
#             crc >>= 1
#         byte >>= 1
#     table.append(crc)
#
#
# def crc32(string):
#     value = 0xffffffff
#
#     for ch in string:
#         value = table[(ord(ch) ^ value) & 0xff] ^ (value >> 8)
#
#     return hex(value)
#
#
# s = input('Введите текст, который нужно хэшировать: ')
# print(crc32(s))
