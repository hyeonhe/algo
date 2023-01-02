import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    stack = []
    s = input()
    if s == '.':
        break
    
    balance = True
    for i in s:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                balance = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                balance = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if not stack and balance:
        print('yes')
    else:
        print('no')