from sys import stdin


def merge(arr1, arr2, ar):
    i, j, k = 0, 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ar[k] = arr1[i]
            i += 1
        else:
            ar[k] = arr2[j]
            j += 1
        k += 1
    while i != len(arr1):
        ar[k] = arr1[i]
        i += 1
        k += 1
    while j != len(arr2):
        ar[k] = arr2[j]
        j += 1
        k += 1


def mergeSort(ar):
    if len(ar) == 1 or len(ar) == 0:
        return

    middle = (len(ar) // 2)

    ar1 = ar[0:middle]
    ar2 = ar[middle:]

    mergeSort(ar1)
    mergeSort(ar2)

    merge(ar1, ar2, ar)

    return ar


def intersection(arr1, arr2, n, m):
    arr1.sort()
    arr2.sort()
    i, j, finalArr = 0, 0, []
    while i < n and j < m:
        if arr1[i] == arr2[j]:
            finalArr.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
    print(*finalArr, sep=" ")


# Taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().strip())

while t > 0:
    arr1_input, n_input = takeInput()
    arr2_input, m_input = takeInput()
    intersection(arr1_input, arr2_input, n_input, m_input)
    print()

    t -= 1
