import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
word = []

for i in range(n):
    word.append(input())

word = list(set(word))
word.sort()
word.sort(key = len)

print("\n".join(word))