from os import *
from sys import *
from collections import *
from math import *


def countZero(num):
    if num // 10 == 0:
        if num == 0:
            return 1
        else:
            return 0
    smallOutput = countZero(num // 10)
    if num % 10 == 0:
        return 1 + smallOutput
    else:
        return 0 + smallOutput


n = int(input())
print(countZero(n))
