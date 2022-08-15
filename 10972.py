from itertools import permutations
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
permutation = list(map(int, input().split()))

array = list(permutations(list(range(1, n+1)), n))

print(array)
print(len(array))

while 
# for i in range(len(array)):
    
#     if list(array[i]) == permutation:
#         if len(array) - 1 == i:
#             print(-1)
#         else:
#             for j in array[i+1]:
#                 print(j, end=' ')