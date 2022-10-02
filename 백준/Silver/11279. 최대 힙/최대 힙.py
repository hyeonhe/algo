import heapq
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x:
        heapq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1: 
            print(heapq.heappop(heap)[1])
        else:
            print(0)