from sys import stdin


def findDuplicate(arr, n):
    end_number = n - 2
    sum_of_n_number = (end_number * (end_number + 1)) // 2
    sum_of_arr = sum(arr)
    return sum_of_arr - sum_of_n_number


# Taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1
