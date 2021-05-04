t = int(input())

aScore = 100
bScore = 100
for i in range(t):
    a, b = map(int, input().split())
    if a > b:
        bScore -= a
    elif a < b:
        aScore -= b

print(aScore)
print(bScore)
