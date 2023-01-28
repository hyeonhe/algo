import sys
input = sys.stdin.readline

n = int(input())
_dict = dict()
for _ in range(n):
    name, log = input().split()
    if log == 'enter':
        _dict[name] = log
    else:
        if name in _dict:
            del _dict[name]
    
print('\n'.join(sorted(_dict.keys(), reverse=True)))