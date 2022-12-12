from os import *
from sys import *
from collections import *
from math import *
setrecursionlimit(10000)


def multiply2number(m, n):
    if n == 0:
        return 0
    smallOutput = multiply2number(m, n-1)
    return m + smallOutput


m_inp = int(input())
n_inp = int(input())
print(multiply2number(m_inp, n_inp))
