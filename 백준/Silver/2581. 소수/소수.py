m = int(input())
n = int(input())
limit = 10000

array = [i for i in range(limit + 1)]
array[1] = 0

for i in range(2, int(limit ** 1/2 + 1)):
    if array[i] != 0:
        j = 2
        while i * j <= limit:
            array[i * j] = 0
            j += 1

answer = set(array[m:n + 1])
if 0 in answer:
    answer.remove(0)

if answer == set():
    print(-1)
else:
    print(sum(answer))
    print(min(answer))
