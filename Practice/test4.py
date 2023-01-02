# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.8.10
    listOfNum = []
    for i in range(len(S) - 1):
        listOfNum.append(int(S[i:i + 2]))
    return max(listOfNum)

# print(solution("011239092"))

# "505255"