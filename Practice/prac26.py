def bubbleSort(arr, si, li, num):
    if li == -1:
        li = len(arr) - 1
    if si == li:
        return arr[si] == num
    mi = ((si + li) // 2)
    if arr[mi] == num:
        return True
    else:
        if arr[mi] > num:
            return bubbleSort(arr, si, mi-1, num)
        else:
            return bubbleSort(arr, mi+1, li, num)


print(bubbleSort([1, 2, 3, 4, 5, 6, 7, 8], 0, -1, 7))
