def indexOfP(arr, p, start, end):
    count = 0
    for e in arr[start:end+1]:
        if e < p:
            count += 1
    return start + count


def partition(arr, start, end):
    pIndex = indexOfP(arr, arr[start], start, end)
    arr[pIndex], arr[start] = arr[start], arr[pIndex]
    i = start
    j = len(arr) - 1
    while i < pIndex < j:
        if arr[i] < arr[pIndex]:
            i += 1
        else:
            if arr[j] >= arr[pIndex]:
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
    return pIndex


def quickSort(arr, start, end):
    if start >= end:
        return
    i = partition(arr, start, end)
    quickSort(arr, start, i - 1)
    quickSort(arr, i + 1, end)


n = int(input()) - 1
arr = list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n)
print(*arr)
