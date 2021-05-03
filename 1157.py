a = list(input())
b = list(sorted(set(a)))
c = sorted(a)
print(a)
print(b)
print(c)

alpha = {}
for j in range(len(c)):
    count = 0
    for i in range(len(b)):
        if b[i] == c[j]:
            count += 1
        alpha = {b[i]: count}

print(alpha)
