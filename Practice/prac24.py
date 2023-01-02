# Problem: Remove x from string
def removeX(s, a, b):
    if len(s) == 0:
        return ""
    smallOutput = removeX(s[1:], a, b)
    if s[0] == a:
        return b + smallOutput
    else:
        return s[0] + smallOutput


# Main
string = input()
print(removeX(string, 'x', ''))
