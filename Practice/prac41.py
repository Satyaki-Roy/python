def power(x, n):
    if n == 0:
        return 1
    smallPower = power(x, n // 2)
    if n % 2 == 0:
        return smallPower * smallPower
    else:
        return smallPower * smallPower * x


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
x_inp, n_inp = list(int(i) for i in input().strip().split(' '))
print(power(x_inp, n_inp))
