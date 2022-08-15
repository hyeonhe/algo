import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    sentence = input()
    if sentence == '.':
        break
    