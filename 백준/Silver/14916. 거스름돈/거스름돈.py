n = int(input())

answer = 0
while n > 0:
    if n % 5 == 0:
        answer += n // 5
        # n //= 5
        n = 0
    else:
        answer += 1
        n -= 2

if n:
    print(-1)
else:
    print(answer)