n = int(input())
n = 1000 - n
cnt = 0

money = [500, 100, 50, 10, 5, 1]

for i in money:
  a = n // i
  cnt += a
  n -= a * i

print(cnt)