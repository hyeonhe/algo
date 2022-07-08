import sys

def input():
    return sys.stdin.readline().rstrip()

f0 = [0] * 41
f1 = [0] * 41

t = int(input())

f0[0] = 1
f1[1] = 1

for _ in range(t):
    n = int(input())
    for i in range(2, n+1):
        if f0[i] == 0 and f1[i] == 0:
            f0[i] = f0[i-1] + f0[i-2]
            f1[i] = f1[i-1] + f1[i-2]
    print(f0[n], f1[n])