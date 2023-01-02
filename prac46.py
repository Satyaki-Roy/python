from sys import stdin


# def pairSum(arr, n, num):
#     count = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[i] + arr[j] == num:
#                 print(arr[i], arr[j])
#                 count += 1
#     return count

def sumOfNNumber(n):
    return ((n - 1) * n) // 2


def pairSum(arr, n, num):
    arr.sort()
    arr_dict = {}
    arr_unique = []
    count = 0

    for i in range(n):
        if i == 0:
            arr_dict[arr[i]] = 1
            arr_unique.append(arr[i])
        elif arr[i - 1] != arr[i]:
            arr_dict[arr[i]] = 1
            arr_unique.append(arr[i])
        else:
            arr_dict[arr[i]] += 1

    i = 0
    j = len(arr_unique) - 1

    while i <= j:
        num1 = arr_unique[i]
        num2 = arr_unique[j]
        if num1 == num / 2 and arr_dict[num1] > 1:
            count += sumOfNNumber(arr_dict[num1])
            i += 1
            # print('hi1')
        elif num1 == num / 2 and arr_dict[num1] == 1:
            i += 1
            # print('hi2')
        elif num2 == num / 2 and arr_dict[num2] > 1:
            count += sumOfNNumber(arr_dict[num2])
            j -= 1
            # print('hi3')
        elif num2 == num / 2 and arr_dict[num2] == 1:
            j -= 1
            # print('hi4')
        elif num1 + num2 == num:
            count += arr_dict[num1] * arr_dict[num2]
            i += 1
            j -= 1
            # print('hi5')
        elif num1 + num2 > num:
            j -= 1
            # print('hi6')
        elif num1 + num2 < num:
            i += 1
            # print('hi7')

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
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))

    t -= 1
