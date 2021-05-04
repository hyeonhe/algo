# n, x = map(int, input().split)
# listA = list(map(int, input().split()))

# for i in range(n):
#     if listA[i] < x:
#         print(listA[i], end=' ')

# listS = [i for i in range(n) if listA < x]


a, b = map(int, input().split())
score = [x for x in input().split() if int(x) < b]
print(' '.join(score))
