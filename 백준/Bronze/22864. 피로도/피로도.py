a, b, c, m = map(int, input().split())

work = 0
tired = 0

for i in range(24):
    if (tired + a) <= m:
        tired += a
        work += b
    else:
        tired -= c
        if tired < 0:
            tired = 0

print(work)