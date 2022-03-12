# a -> 피로도, b -> 일의 양, c -> 피로도 회복량, m -> 최대 피로도
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