import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

arr = {}
for i in range(n + m):
    name = input()

    if name in arr:
        arr[name] += 1
    else:
        arr[name] = 1

arr = sorted(arr.items())

cnt = 0
names = []
for name in arr:
    if name[1] > 1:
        names.append(name[0])
        cnt += 1

print(cnt)
print('\n'.join(names))