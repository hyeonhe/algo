from collections import Counter
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
num = []

for i in range(n):
    num.append(int(input()))

# 오름차순 정렬
num.sort()
# 산술평균 반올림해서 출력
print(round(sum(num) / n))
# 중앙값 출력
print(num[n // 2])

# 최빈값 출력
# 최빈값이 2개 이상이면 최빈값 중 두 번째로 작은 값 출력
c = Counter(num).most_common()

if len(c) > 1:
    if int(c[0][1]) == int(c[1][1]):
        print(c[1][0])
    else:
        print(c[0][0])
else:
    print(c[0][0])

# 범위 출력
print(num[-1] - num[0])