def merge(a1, a2, a):
    i = 0
    j = 0
    k = 0
    while not (i == len(a1) or j == len(a2)):
        if a1[i] <= a2[j]:
            a[k] = a1[i]
            i += 1
            k += 1
        elif a1[i] >= a2[j]:
            a[k] = a2[j]
            j += 1
            k += 1
    while i != len(a1):
        a[k] = a1[i]
        i += 1
        k += 1
    while j != len(a2):
        a[k] = a2[j]
        j += 1
        k += 1


def mergeSort(a):
    if len(a) == 0 or len(a) == 1:
        return

    middle = len(a) // 2

    a1 = a[0:middle]
    a2 = a[middle:]

    mergeSort(a1)
    mergeSort(a2)

    merge(a1, a2, a)


# Main
n = int(input())
a = list(int(i) for i in input().strip().split(' '))
mergeSort(a)
print(*a)
