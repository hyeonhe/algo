import heapq
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x:
        heapq.heappush(heap, x)
    else:
        if len(heap) >= 1: 
            print(heapq.heappop(heap))
        else:
            print(0)