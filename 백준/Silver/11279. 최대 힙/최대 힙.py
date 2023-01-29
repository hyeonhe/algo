import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            item = heapq.heappop(heap)
            print(item[1])
    else:
        heapq.heappush(heap, (-x, x))