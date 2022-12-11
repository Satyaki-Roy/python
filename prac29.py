def towerofhanoi(n, source, aux, dest):
    if n == 1:
        print(source, dest)
        return
    # moving element from A to B through C
    n -= 1
    towerofhanoi(n, source, dest, aux)
    # move nth element from A to C
    print(source, dest)
    # moving element from B to C through A
    towerofhanoi(n, aux, source, dest)


n = int(input())
towerofhanoi(n, 'a', 'b', 'c')
