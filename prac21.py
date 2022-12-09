arr_inp = [int(x) for x in input().split()]
num_inp = int(input())


def findIndex(arr, index, num):
    if index > len(arr) - 1:
        return -1

    if arr[index] == num:
        return index

    return findIndex(arr, index+1, num)


print(findIndex(arr_inp, 0, num_inp))
