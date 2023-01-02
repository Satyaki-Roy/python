def split(arr, i, lsum, rsum):
    if i == len(arr):
        return lsum == rsum

    if arr[i] % 5 == 0:
        lsum += arr[i]
    elif arr[i] % 3 == 0:
        rsum += arr[i]
    else:
        return split(arr, i+1, lsum+arr[i], rsum) or split(arr, i+1, lsum, rsum+arr[i])

    return split(arr, i+1, lsum, rsum)


n = input()
arr = [int(ele) for ele in input().split()]
ans = split(arr, 0, 0, 0)
if ans is True:
    print('true')
else:
    print('false')
