t = int(input())

for k in range(t):
    r, s = input().split()
    r = int(r)
    s = list(s)
    for i in range(len(s)):
        print(s[i] * r, end='')
    print()