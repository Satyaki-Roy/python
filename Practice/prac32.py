def sumOfDigitsOfNumber(num):
    if num // 10 == 0:
        return num
    smallOutput = sumOfDigitsOfNumber(num // 10)
    return (num % 10) + smallOutput


n = int(input())
print(sumOfDigitsOfNumber(n))
