from sys import setrecursionlimit


def firstLastIndex(arr, index, num):
    # Please add your code here
    if index < 0:
        return -1

    if arr[index] == num:
        return index

    return firstLastIndex(arr, index - 1, num)


# Main
setrecursionlimit(11000)
n = int(input())
arr_inp = list(int(i) for i in input().strip().split(' '))
num_inp = int(input())
print(firstLastIndex(arr_inp, n-1, num_inp))
