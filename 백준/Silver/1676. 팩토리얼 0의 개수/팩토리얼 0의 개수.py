from math import factorial

n = int(input())
num = str(factorial(n))

cnt = 0
for i in num[::-1]:
    if i != '0':
        break
    cnt += 1

print(cnt)