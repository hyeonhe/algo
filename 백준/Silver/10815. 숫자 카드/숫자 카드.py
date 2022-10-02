import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
card1 = list(map(int, input().split()))
m = int(input()) 
card2 = list(map(int, input().split()))

card1.sort()

def binary(array, start, end, target):
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in card2:
    print(binary(card1, 0, len(card1) - 1, i), end=' ')