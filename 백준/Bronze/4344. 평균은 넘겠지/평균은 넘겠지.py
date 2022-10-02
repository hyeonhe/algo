import sys

def input():
    return sys.stdin.readline().rstrip()

c = int(input())

for i in range(c):
    s = list(map(int, input().split()))
    score = s[1:]

    avg = sum(score) / s[0]
    cnt = 0
    for i in score:
        if i > avg:
            cnt += 1
    
    b = format(cnt / s[0] * 100, '.3f')

    print(f'{b}%')