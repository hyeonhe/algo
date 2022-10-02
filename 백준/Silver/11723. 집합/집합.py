import sys

def input():
    return sys.stdin.readline().rstrip()

set_s = []

m = int(input())

for i in range(m):
    com = input()

    if com != 'all' and com != 'empty':
        com, x = com.split()
        x = int(x)

    if com == 'add':
        if x not in set_s:
            set_s.append(x)
    elif com == 'remove':
        if x in set_s:
            set_s.remove(x)
    elif com == 'check':
        if x in set_s:
            print(1)
        else:
            print(0)
    elif com == 'toggle':
        if x in set_s:
            set_s.remove(x)
        else:
            set_s.append(x)
    elif com == 'all':
        set_s = list(range(1, 21))
    elif com == 'empty':
        set_s = []