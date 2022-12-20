import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
pattern = input().split('*')
left = pattern[0]
right = pattern[1]

for i in range(n):
    file = input()
    if len(file) >= len(left) + len(right):
        if left == file[:len(left)] and right == file[-len(right):]:
            print("DA")
        else:
            print("NE")
    else:
        print('NE')