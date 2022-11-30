"""
    In order to print two or more integers in a line separated by a single
    space then you may consider printing it with the statement,

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648
"""

from sys import stdin


def findLargest(arr, nRows, mCols):
    if nRows == 0 or mCols == 0:
        print("row 0 -2147483648")

    highest_sum = 0
    sum = 0
    result_arr = ['', '', '']

    # row cal
    for i in range(nRows):
        sum = 0
        for j in range(mCols):
            sum += arr[i][j]
        if sum > highest_sum:
            highest_sum = sum
            result_arr = ['row', str(i), str(highest_sum)]

    # col cal
    for i in range(mCols):
        sum = 0
        for j in range(nRows):
            sum += arr[j][i]
        if sum > highest_sum:
            highest_sum = sum
            result_arr = ['column', str(i), str(highest_sum)]

    print(' '.join(result_arr))


# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1
