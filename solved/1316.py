import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
cnt = n
for i in range(n):
    word = input()
    chr = {}
    for j in range(len(word)):
        if word[j] not in chr:
            chr[word[j]] = j
        elif chr[word[j]] + 1 == j:
            chr[word[j]] = j
        else:
            cnt -= 1
            break
    chr = {}

print(cnt)
