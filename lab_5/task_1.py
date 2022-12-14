def is_correct(s):
    depth, ind = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            depth += 1
        elif s[i] == ')':
            depth -= 1
        if depth < 0:
            return i + 1
        elif depth > 0 and not ind:
            ind = i + 1
        elif depth == 0:
            ind = 0
    if ind:
        return ind
    return True


print(is_correct(input()))
