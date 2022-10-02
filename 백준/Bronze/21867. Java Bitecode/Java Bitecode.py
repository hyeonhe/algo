n = int(input())
s = list(input())
ans = ''

for i in range(n):
    if s[i] in 'JAV':
        continue
    else:
        ans += s[i]

if len(ans) == 0:
    print('nojava')
else:
    print(ans)