n = int(input())
num = n
final_num = 0
length = len(str(n))
while num > 0:
    rem = num % 10
    final_num += pow(rem, length)
    num = num // 10
    # print(n, num, final_num)
if final_num == n:
    print('true')
else:
    print('false')

