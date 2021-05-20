# 이것도 시간초과..
a, b, c = map(int, input().split())
ans = pow(a, b) % c
print(ans)
