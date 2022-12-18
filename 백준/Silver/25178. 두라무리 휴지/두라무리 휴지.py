n = int(input())
a = input()
b = input()

n1, n2, n3 = False, False, False

if sorted(a) == sorted(b):
    n1 = True

if a[0] == b[0] and a[-1] == b[-1]:
    n2 = True

for i in 'aeiou':
    a = a.replace(i, '')
    b = b.replace(i, '')

if a == b:
    n3 = True

if n1 and n2 and n3:
    print('YES')
else:
    print('NO')