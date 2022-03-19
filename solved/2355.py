a, b = map(int, input().split())
n_max = max(a, b)
n_min = min(a, b)
n = n_max - n_min + 1
ans = n * (n_min + n_max) // 2

print(ans)