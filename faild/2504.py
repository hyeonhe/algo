string = input()
stack = []
answer = 0


for i in range(len(string)):
    if string[i] == '(' or string[i] == '[':
        stack.append(string[i])
    elif stack == [] and (string[i] == ')' or string[i] == ']'):
        answer = 0
        break
    elif string[i-1] == '(' and string[i] == ')':
