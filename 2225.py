# 점화식을 도출..
import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())





# from itertools import product
# num = list(range(0, n+1))
# array = list(product(num, repeat = k))
# cnt = 0

# for i in array:
#     if sum(i) == n:
#         cnt += 1

# print(cnt)