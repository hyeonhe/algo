n = input()
# a = 0
while len(n) >= 10:
    print(n[0:10])
    n = n[10:]
print(n)
