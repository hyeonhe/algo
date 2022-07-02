
n = int(input())
sum = 0

num = 1
while sum != n:
    sum += num
    num = str(num)

    for i in num:
        sum += int(i)
    
    if sum == n:
        break

    num = int(num) + 1
    sum = 0

print(num)