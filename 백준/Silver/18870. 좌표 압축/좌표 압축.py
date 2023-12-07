import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
numbers = list(map(int, input().split()))

numbers_copy = sorted(set(numbers))

dic = {numbers_copy[i]: i for i in range(len(numbers_copy))}

for i in numbers:
    print(dic[i], end=' ')