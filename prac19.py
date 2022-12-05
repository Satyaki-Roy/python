from sys import setrecursionlimit


def sumArray(arr_input):
    # Please add your code here
    if len(arr_input) == 0:
        return 0

    if len(arr_input) == 1:
        return arr_input[0]

    return arr_input[0] + sumArray(arr_input[1:])


# Main
setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
