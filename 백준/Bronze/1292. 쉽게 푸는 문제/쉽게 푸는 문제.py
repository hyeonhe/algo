import sys

def input():
  return sys.stdin.readline().rstrip()
  
a, b = map(int, input().split())

n = 1
count = 0

array = []
for i in range(b):
  count += 1
  array.append(n)

  if count == n:
    n += 1
    count = 0

print(sum(array[a-1:b]))