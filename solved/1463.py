# 다이나믹 프로그래밍 드뎌 공부함!
n = int(input())

# 메모이제이션 n+1 크기의 리스트 만들기
d = [0] * (n + 1)

# n은 1보다 크거나 같음 
# n이 1일 경우 연산이 필요 없으므로 0 출력
for i in range(2, n + 1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)


print(d[n])