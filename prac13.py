from os import *
from sys import *
from collections import *
from math import *


def printRowNTimes(matrix, nR, mC):
    finalArr = []
    for i in range(nR):
        count = nR - i
        while count != 0:
            finalArr.append(matrix[i])
            count -= 1

    for r in finalArr:
        print(' '.join([str(x) for x in r]))


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
mat, nRows, mCols = take2DInput()
printRowNTimes(mat, nRows, mCols)
