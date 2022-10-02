import sys

def input():
    return sys.stdin.readline().rstrip()

k = int(input())

a = [1, 0]
b = [0, 1]

if k == 1:
    print(a[1], b[1])
else:
    for i in range(2, k+1):
        a.append(a[-1] + a[-2])
        b.append(b[-1] + b[-2])

    print(a[-1], b[-1])