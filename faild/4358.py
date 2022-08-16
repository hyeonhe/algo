import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

trees = defaultdict(int)

cnt = 0
while True:
    tree = input()
    if not tree:
        break
    trees[tree] += 1
    cnt += 1

tree_key = list(trees.keys())
tree_key.sort()

for tree in trees:
    # print(tree, round(trees[tree] / cnt * 100, 4))
    print('%s %.4f' %(tree, trees[tree]/cnt*100))