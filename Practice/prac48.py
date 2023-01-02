from sys import stdin


# def rotate(arr, n, d):
#     if n == 0:
#         return
#     for i in range(d % n):
#         first_element = arr.pop(0)
#         arr.append(first_element)


def rotate(arr, n, d):
    empty_arr = [None] * n
    if n == 0:
        return
    for i in range(n):
        if i < d:
            empty_arr[n + i - d] = arr[i]
        else:
            empty_arr[i - d] = arr[i]
    return empty_arr


def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    arr = rotate(arr, n, d)
    printList(arr, n)

    t -= 1
