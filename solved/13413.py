import sys

def input():
    return sys.stdin.readline().rstrip()
t = int(input())

for i in range(t):
    n = int(input())
    str1 = list(input())
    str2 = list(input())
    cnt1 = 0
    cnt2 = 0
    
    for i in range(n):
        if str1[i] != str2[i]:
            if str1[i] == 'W':
                cnt1 += 1
            else:
                cnt2 += 1
    print(max(cnt1, cnt2))