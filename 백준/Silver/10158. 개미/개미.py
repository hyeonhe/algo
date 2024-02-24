import sys
import math

def input():
    return sys.stdin.readline().rstrip()

w, h = map(int, input().split(' '))
p, q = map(int, input().split(' '))
t = int(input())

x = (p+t) % (w*2)
y = (q+t) % (h*2)

print(w - abs(w-x), h - abs(h-y))