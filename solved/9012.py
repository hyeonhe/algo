import sys
def input():
    return sys.stdin.readline().rstrip()

t = int(input())
stack = []

for _ in range(t):
    str = input()
    for i in str:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
    if stack:
        print('NO')
    else:    
        print('YES')
    stack = []