n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = 0

for i in arr:
    cnt += 1
    i -= b
    if i > 0:
        cnt += i // c
        if i % c != 0:
            cnt += 1

print(cnt)