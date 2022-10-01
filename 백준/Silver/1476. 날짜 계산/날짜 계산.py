import sys

def input():
    return sys.stdin.readline().rstrip()

e, s, m = map(int, input().split())

e1, s1, m1 = 1, 1, 1
count = 1
while e != e1 or s != s1 or m != m1:
    count += 1
    e1 += 1
    s1 += 1
    m1 += 1
    if e1 > 15:
        e1 = 1
    if s1 > 28:
        s1 = 1
    if m1 > 19:
        m1 = 1

print(count)