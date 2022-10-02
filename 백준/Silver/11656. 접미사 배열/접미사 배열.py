s = input()

tail = []

for i in range(len(s)):
    tail.append(s[i:])

tail.sort()

for i in tail:
    print(i)