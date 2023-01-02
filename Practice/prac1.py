n = int(input())
i = 1
space = n - 1


def print_num(j):
    m = 1
    k = j - 1
    p = 2
    while m <= k:
        print(p, end='')
        m = m + 1
        p = p + 1


def print_space(j):
    print(j*' ', end='')


def print_num_rev(j):
    while 1 <= j:
        print(j, end='')
        j = j - 1


while i <= n:
    print_space(space)
    print_num_rev(i)
    print_num(i)
    print()
    space = space - 1
    i = i + 1
