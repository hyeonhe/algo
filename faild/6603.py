import random
s = input()
k = s[0]
s = sorted(set(s[2:]))
s.remove(' ')
print(k, s)

print(random.choice(s))

# 나중에 풀래
