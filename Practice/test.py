n = int(input())
i = 1
j = n

while i <= n:
    print((i-1)*'0', end='')
    print('*', end='')
    print((j-1)*'0', end='')
    print('*', end='')
    print((j - 1) * '0', end='')
    print('*', end='')
    print((i - 1) * '0', end='')
    print()
    i = i + 1
    j = j - 1
