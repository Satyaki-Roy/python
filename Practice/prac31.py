def checkPallindrom(givenStr, start, end):
    if start >= end:
        return True
    if givenStr[start] != givenStr[end]:
        return False
    return checkPallindrom(givenStr, start + 1, end - 1)


s = input()
print('true' if checkPallindrom(s, 0, len(s) - 1) else 'false')
