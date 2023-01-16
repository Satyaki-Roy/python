from sys import stdin


def checkRedundantBrackets(expression):
    arr = []
    for i in expression:
        if i == '(':
            arr.append({
                "bracket_type": 'in',
                "content": False
            })
        elif (i == '+' or i == '-' or i == '//' or i == '*' or i == '/' or i == '%') and len(arr):
            arr[-1]["content"] = True
        elif i == ')':
            if arr[-1]["content"]:
                arr.pop()
            else:
                return True
    return len(arr) != 0


# main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression):
    print("true")
else:
    print("false")
