import sys
input = sys.stdin.readline

n = input()
_set = set(map(int, input().split()))
m = input()
_list = list(map(int, input().split()))

print(*[1 if i in _set else 0 for i in _list], sep='\n')