# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(s):
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    smallOutput = removeConsecutiveDuplicates(s[1:])
    if s[0] == s[1]:
        return "" + smallOutput
    else:
        return s[0] + smallOutput


# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
