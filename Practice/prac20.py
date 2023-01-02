from sys import setrecursionlimit


def checkNumber(arr_input, x_input):
    if len(arr_input) == 0:
        return False

    if len(arr) == 1:
        return x == arr_input[0]

    if x == arr_input[0]:
        return True
    else:
        return checkNumber(arr_input[1:], x_input)


# Main
setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
