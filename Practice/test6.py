def maximumProfit(ar):
    ar.sort()
    maxProfitArr = []
    for i in range(len(ar)):
        maxProfitArr.append(ar[i] * (len(ar) - i))
    # print(maxProfitArr)
    return max(maxProfitArr)


n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr)
print(ans)
