# 20220531
import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    command = sys.stdin.readline().rstrip()
    if command == 'pop':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(0 if len(stack) else 1)
    elif command == 'top':
        print(stack[-1] if len(stack) else -1)
    else:
        x = int(command[5:])
        stack.append(x)