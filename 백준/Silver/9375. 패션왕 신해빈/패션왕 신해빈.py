from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    wear = []
    for i in range(n):
        a, b = input().split()
        wear.append(b)
        
    wear = Counter(wear)

    answer = 1
    for i in wear:
        answer *= wear[i] + 1

    print(answer - 1)