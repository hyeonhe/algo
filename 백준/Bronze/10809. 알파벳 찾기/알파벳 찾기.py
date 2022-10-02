import sys

def input():
    return sys.stdin.readline().rstrip()

s = list(input())
abc = [-1] * 26

for i in range(len(s)):
    
    if abc[ord(s[i]) - 97] == -1:
        abc[ord(s[i]) - 97] = i

for i in abc:
    print(i, end=' ')