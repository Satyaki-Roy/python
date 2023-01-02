n = int(input())
mid = n//2 + 1
space = mid - 1

for i in range(1, n+1, 2):
    print(space * " ", end="")
    print(i * "*", end="")
    print()
    space -= 1

space = 1
for i in range(n-2, 0, -2):
    print(space * " ", end="")
    print(i * "*", end="")
    print()
    space += 1
