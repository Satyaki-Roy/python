n = int(input())
i = 1

while i <= n:
    if i <= (n/2 + 1):
        if i == 1:
            print(i * '*', end='')
        else:
            print((i - 2) * ' ', end='')
            print(i * ' *', end='')
    else:
        if i == n:
            print((n - i + 1) * '*', end='')
        else:
            print((n - i - 1) * ' ', end='')
            print((n - i + 1) * ' *', end='')
    print()
    i = i + 1

# n = int(input())
# i = 1
#
# while i <= n:
#     if i <= (n/2 + 1):
#         print((i - 2) * ' ', end='')
#         print(i * ' *', end='')
#     else:
#         print((n-i-1) * ' ', end='')
#         print((n-i+1) * ' *', end='')
#     print()
#     i = i + 1
