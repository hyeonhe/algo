import sys

def input():
    return sys.stdin.readline().rstrip()
    
n = int(input())
s = []
op = []
count = 1
temp = True

for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        op.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False
        break
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)