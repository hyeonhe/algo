n = int(input())
array = list(map(int, input().split()))
array.sort()
answer = 0

for i in range(n):
    for j in range(i + 1):
        answer += array[j]

print(answer)