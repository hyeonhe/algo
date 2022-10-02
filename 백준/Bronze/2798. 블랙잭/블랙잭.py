from itertools import combinations
n, m = map(int, input().split())
card = list(map(int, input().split()))
card.sort()

nums = list(combinations(card, 3))
answer = 0
for i in range(len(nums)):
    a = sum(nums[i])
    if a <= m and a > answer:
        answer = a

print(answer)