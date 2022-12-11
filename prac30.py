from os import *
from sys import *
from collections import *
from math import *


def sumOfGP(n):
    if n == 0:
        return 1
    smallOutput = sumOfGP(n - 1)
    return pow(1 / 2, n) + smallOutput


n = int(input())
# print(round(sumOfGP(n), 5))
print('%.5f' % round(sumOfGP(n), 5))
