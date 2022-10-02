import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
# 후위표기식 입력받기
abc = list(input())
stack = []
num_list = []

for _ in range(n):
    num_list.append(int(input()))

for i in abc:
    if 'A' <= i <= 'Z':
        stack.append(num_list[ord(i) - 65])
    else:
        a = stack.pop()
        b = stack.pop()
        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(b - a)
        elif i == '*':
            stack.append(a * b)
        elif i == '/':
            stack.append(b / a)

print(format(stack.pop(), '.2f'))