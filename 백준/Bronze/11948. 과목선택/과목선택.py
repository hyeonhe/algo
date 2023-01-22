a = [int(input()) for _ in range(4)]
b = [int(input()) for _ in range(2)]

a.sort()
b.sort()

ans = 0
ans += sum(a[1:])
ans += b[1]

print(ans)