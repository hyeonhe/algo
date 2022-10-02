n = input()
a = 0
while len(n) >= 10:
    print(n[a:a+10])
    n = n[a+10:]
print(n[a:])
