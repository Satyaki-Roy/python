def printStar(s, ci=-100):
    if ci == -100:
        ci = len(s) - 1

    if ci <= 0:
        return s[0] == 'a'

    if s[ci] == 'a':
        return printStar(s, ci - 1)
    elif s[ci] == 'b':
        if s[ci - 1] == 'b':
            return printStar(s, ci - 2)
        else:
            return False
    else:
        return False


print(printStar(input()))
