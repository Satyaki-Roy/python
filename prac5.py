n = int(input())

for i in range(1, n+1, 2):
    # print(i)
    start = n * i - n + 1
    for j in range(1, n+1):
        if j < n:
            print(start, end=" ")
        else:
            print(start, end="")
        start += 1
    print()

if n % 2 == 0:
    for i in range(n, 1, -2):
        # print(i)
        start = n * i - n + 1
        for j in range(1, n + 1):
            if j < n:
                print(start, end=" ")
            else:
                print(start, end="")
            start += 1
        print()
else:
    for i in range(n-1, 1, -2):
        # print(i)
        start = n * i - n + 1
        for j in range(1, n + 1):
            if j < n:
                print(start, end=" ")
            else:
                print(start, end="")
            start += 1
        print()
