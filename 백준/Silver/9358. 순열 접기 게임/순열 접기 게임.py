import sys
import math
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    
    while N > 2:
        for i in range(math.ceil(N / 2)):
            if N % 2 == 1 and i == math.floor(N / 2):
                arr[i] *= 2
            else:
                arr[i] += arr[N-i-1]
                
        N = math.ceil(N / 2)
        
    if arr[0] > arr[1]:
        print(f'Case #{t+1}: Alice')
    else:
        print(f'Case #{t+1}: Bob')