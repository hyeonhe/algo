x = input()
cnt = 0
n = 0

while len(x) > 1:
    for i in x:
        n += int(i)
    x = str(n)
    n = 0
    cnt += 1

print(cnt)

if int(x) % 3 == 0:
    print("YES")
else:
    print("NO")