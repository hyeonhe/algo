import sys
input = sys.stdin.readline

n = int(input())
_dict = dict()
for _ in range(n):
    name, log = input().split()
    _dict[name] = log

_dict = sorted(_dict.items(), key = lambda item: item[0], reverse=True)

for item in _dict:
    if item[1] == 'enter':
        print(item[0])