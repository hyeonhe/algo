# def factorial(num):
#     if num == 1 or 0:
#         return 1
#     else:

#         return factorial(num-1) * num


# def fac(num):
#     fac = {}
#     return factorial(num)

import math

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(math.factorial(m) // math.factorial(n) // math.factorial(m-n))
