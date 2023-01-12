a = dict()
for i in range(8):
   a[int(input())] = i + 1

b = a.keys()
b = sorted(b, reverse=True)

idx = []
for i in range(5):
    idx.append(a[b[i]])

idx.sort()

print(sum(b[:5]))
print(' '.join(map(str, idx)))