from sys import stdin


# first way
# def arrayEquilibriumIndex(arr, n):
#     for i in range(n):
#         if sum(arr[0:i]) == sum(arr[i + 1:]):
#             return i
#     return -1


# second way
# def suffix_sum(ar):
#     finalArr = []
#     currentSum = 0
#     for i in range(len(ar)):
#         if i == 0:
#             finalArr.append(0)
#         else:
#             currentSum += ar[i - 1]
#             finalArr.append(currentSum)
#     return finalArr
#
#
# def prefix_sum(ar):
#     finalArr = [None] * len(ar)
#     currentSum = 0
#     i = len(ar) - 1
#     while i >= 0:
#         if i == len(ar) - 1:
#             finalArr[i] = 0
#         else:
#             currentSum += ar[i + 1]
#             finalArr[i] = currentSum
#         i -= 1
#     return finalArr
#
#
# def arrayEquilibriumIndex(arr, n):
#     suffixSumArr = suffix_sum(arr)
#     # print(suffixSumArr)
#     prefixSumArr = prefix_sum(arr)
#     # print(prefixSumArr)
#     for i in range(n):
#         if suffixSumArr[i] == prefixSumArr[i]:
#             return i
#     return -1


# third way
def arrayEquilibriumIndex(arr, n):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(n):
        right_sum = total_sum - left_sum - arr[i]
        # print(total_sum, left_sum, right_sum)
        if right_sum == left_sum:
            return i
        left_sum += arr[i]
    return -1


# Taking input using fast I/O method
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
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t -= 1
