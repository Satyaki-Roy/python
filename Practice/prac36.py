def printStar(s, pi=0, ci=0):
    if ci == len(s) - 1:
        if s[pi] == s[ci]:
            return '*' + s[ci]
        else:
            return s[ci]
    if pi == ci:
        return s[ci] + printStar(s, pi, ci + 1)
    elif s[pi] == s[ci]:
        return '*' + s[ci] + printStar(s, pi + 1, ci + 1)
    elif s[pi] != s[ci]:
        return s[ci] + printStar(s, pi + 1, ci + 1)


print(printStar(input()))
