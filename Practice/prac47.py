from sys import stdin


# def tripletSum(arr, n, num):
#     count = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 if arr[i] + arr[j] + arr[k] == num:
#                     count += 1
#     return count


def sumOfNNumber(n):
    return ((n - 1) * n) // 2


def pairSum(arr, n, num):
    # arr.sort()
    # print(arr)
    count = 0
    i = 0
    j = n - 1

    while i < j:
        if arr[i] + arr[j] == num:
            start_num = arr[i]
            start_count = 1
            while arr[i + 1] == start_num:
                start_count += 1
                i += 1
            end_num = arr[j]
            end_count = 1
            while arr[j - 1] == end_num:
                end_count += 1
                j -= 1
            # print(start_num, start_count, end_num, end_count)
            if start_num == end_num:
                count += sumOfNNumber(start_count)
            else:
                count += start_count * end_count
            i += 1
            j -= 1
        elif arr[i] + arr[j] > num:
            j -= 1
        else:
            i += 1

    return count


def tripletSum(arr, n, num):
    arr.sort()
    i = 0
    count = 0
    while i < n - 2:
        count += pairSum(arr[i + 1:], n - i - 1, num - arr[i])
        i += 1
    return count


# taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr_input, n_input = takeInput()
    num_input = int(stdin.readline().strip())
    print(tripletSum(arr_input, n_input, num_input))

    t -= 1
