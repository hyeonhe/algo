nine = []

for i in range(9):
    a = int(input())
    nine.append(a)

rest = sum(nine) - 100
print(rest)

for i in range(1, rest):
    k = rest-i
    if i and k in nine:
        nine.remove(i)
        nine.remove(k)
# sorted(nine)

# for i in range(len(nine)):
#     print(nine[i])
