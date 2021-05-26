t = int(input())
scores = list(map(int, input().split()))

sMax = max(scores)

for i in range(t):
    scores[i] = scores[i] / sMax * 100

print(sum(scores)/t)
