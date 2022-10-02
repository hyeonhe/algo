import sys

word = sys.stdin.readline().rstrip()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = {}
for i in alpha:
    # cnt.append(word.count(i))
    cnt[i] = word.count(i)

if cnt['dz='] < cnt['z=']:
    cnt['z='] -= cnt['dz=']
elif cnt['dz='] == cnt['z=']:
    cnt['z='] = 0

answer = len(word)
for i, v in cnt.items():
    # answer = answer - len(i) * v + v
    answer = answer - v * (len(i) - 1)

print(answer)