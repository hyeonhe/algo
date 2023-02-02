from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

d = deque(i for i in range(1, n+1))
idx = deque(map(int, input().split()))

cnt = 0
while idx:
    if idx[0] != d[0]:
        num = d.index(idx[0])
        if num * 2 > len(d):
            cnt += len(d) - num
            d.rotate(len(d) - num)
        else:
            cnt += num
            d.rotate(-num)
    else:
        d.popleft()
        idx.popleft()

print(cnt)