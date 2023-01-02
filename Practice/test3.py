def solution(A, B):
    # write your code in Python 3.8.10
    i = 1
    count = 0
    while i < len(A):
        sum1 = sum(A[0:i])
        sum2 = sum(A[i:])
        sum3 = sum(B[0:i])
        sum4 = sum(B[i:])
        if sum1 == sum2 == sum3 == sum4:
            count += 1
        i += 1
    return count

# print(solution([0, 4, -1, 0, 3], [0, -2, 5, 0, 3]))
# print(solution([2, -2, -3, 3], [0, 0, 4, -4]))
# print(solution([2, 2], [2, 2]))
# print(solution([4, -1, 0, 3], [-2, 6, 0, 4]))
# print(solution([3, 2, 6], [4, 1, 6]))
# print(solution([1, 4, 2, -2, 5], [7, -2, -2, 2, 5]))

# A = [1,-1,    2,-2]
# B = [3,-3,    4,-4]
#
# prefix and sufix