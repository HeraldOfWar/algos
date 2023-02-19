def is_correct(s):
    depth, ind = 0, 0
    depth1, ind1 = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            depth += 1
        elif s[i] == ')':
            depth -= 1
            if depth1 > 0 and ind < ind1:
                return i + 1
        elif s[i] == '[':
            depth1 += 1
        elif s[i] == ']':
            depth1 -= 1
            if depth > 0 and ind1 < ind:
                return i + 1
        if depth < 0:
            return min(i + 1, ind1)
        elif depth > 0 and not ind:
            ind = i + 1
        elif depth == 0:
            ind = 0
        if depth1 < 0:
            return min(ind, i + 1)
        elif depth1 > 0 and not ind1:
            ind1 = i + 1
        elif depth1 == 0:
            ind1 = 0
    if ind and ind1:
        return min(ind, ind1)
    elif ind:
        return ind
    elif ind1:
        return ind1
    return True


print(is_correct(input()))
