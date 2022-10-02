import sys

def input():
    return sys.stdin.readline().rstrip()

nine = []
for i in range(9):
    nine.append(int(input()))

nine.sort()
rest = sum(nine) - 100

for i in nine:
    if i and rest - i in nine:
        nine.remove(i)
        nine.remove(rest-i)
        break


for i in nine:
    print(i)