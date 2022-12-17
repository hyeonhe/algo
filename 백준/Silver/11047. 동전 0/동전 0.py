n, k = map(int, input().split())

money = []
for _ in range(n):
    money.append(int(input()))

cnt = 0

for i in money[::-1]:
    q = k // i
    if q > 0:
        cnt += q
        k -= q * i

print(cnt)