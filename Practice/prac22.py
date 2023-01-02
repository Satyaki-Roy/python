from sys import setrecursionlimit


def firstIndex(arr, index, num):
    # Please add your code here
    if index > len(arr) - 1:
        return -1

    if arr[index] == num:
        return index

    return firstIndex(arr, index + 1, num)


# Main
setrecursionlimit(11000)
n = int(input())
arr_inp = list(int(i) for i in input().strip().split(' '))
num_inp = int(input())
print(firstIndex(arr_inp, 0, num_inp))
