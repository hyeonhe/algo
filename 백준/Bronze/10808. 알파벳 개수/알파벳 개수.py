from collections import Counter
s = input()

count = Counter(s)

for i in range(ord('a'), ord('z') + 1):
    print(count[chr(i)], end = ' ')