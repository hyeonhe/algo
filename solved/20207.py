import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input)

array = []

for i in range(n):
    input_data = map(int, input().strip())
    array.append(input_data[1] - input_data[0] + 1)

