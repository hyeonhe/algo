import sys

word = sys.stdin.readline().rstrip()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alpha:
    word = word.replace(i, "@")

print(len(word), word)