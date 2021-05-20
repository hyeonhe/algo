# 2021년 5월 20일 시간초과 나와서 통과 못함..

m, n = map(int, input().split())

for i in range(m, n+1):
    count = 0
    for j in range(1, i+1):
        if i % 2 == 0:
            break
        elif i % j == 0:
            count += 1
        if count == 3:
            break
    if count == 2:
        print(i)
