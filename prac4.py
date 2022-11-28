n = int(input())

repeat_num = n
repeat_count = n*2 - 1
for i in range(n, 0, -1):
    for j in range(n, i, -1):
        print(j, end="")
    if i == repeat_num:
        print(repeat_count * str(repeat_num), end="")
        repeat_num -= 1
        repeat_count -= 2
    for j in range(i+1, n+1, 1):
        print(j, end="")
    print()

repeat_num = 2
repeat_count = 3
for i in range(2, n+1):
    for j in range(n, i, -1):
        print(j, end="")
    if i == repeat_num:
        print(repeat_count * str(repeat_num), end="")
        repeat_num += 1
        repeat_count += 2
    for j in range(i+1, n+1, 1):
        print(j, end="")
    print()
