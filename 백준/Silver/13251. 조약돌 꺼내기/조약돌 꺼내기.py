m = int(input())
n = list(map(int, input().split()))
k = int(input())

answer = 0
total = sum(n)

for i in n:
    mul = 1
    for j in range(k):
        mul *= (i - j)
    answer += mul

for i in range(k):
    answer /= (total - i)

print(answer)