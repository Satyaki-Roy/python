def numberFromUnicode(strNum):
    return ord(strNum) - ord('0')


def strToInt(s):
    l = len(s) - 1
    n = numberFromUnicode(s[0])
    if l == 0:
        return n
    smallOutput = strToInt(s[1:])
    return (n * pow(10, l)) + smallOutput


str_inp = input()
print(strToInt(str_inp))
