n = int(input())
i = 1
space = (n * 2) - 2


def print_num(j):
    k = 1
    while k <= j:
        print(k, end='')
        k = k + 1


def print_space(j):
    print(j*' ', end='')


def print_num_rev(j):
    while 1 <= j:
        print(j, end='')
        j = j - 1


while i <= n:
    print_num(i)
    print_space(space)
    print_num_rev(i)
    print()
    space = space - 2
    i = i + 1
