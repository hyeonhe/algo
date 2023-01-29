import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
ans = 0

for _ in range(n):
    heapq.heappush(heap, int(input()))

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    tmp = one + two
    ans += tmp
    heapq.heappush(heap, tmp)

print(ans)