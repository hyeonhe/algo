n = int(input())

answer = n
temp = 0
count = 0

while True:
    a = answer // 10  
    b = answer % 10
    count += 1
    answer = b * 10 + (a + b) % 10

    if n == answer:
        break

print(count)