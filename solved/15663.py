from itertools import permutations
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = list(map(int, input().split()))

# 순열을 이용하여 배열 만들기
array = permutations(a, m)
# 중복을 제거하고 리스트로 형변환
array = list(set(array))
# 정렬하기
array.sort()

# 배열 출력하기
for i in array:
    for j in i:
        print(j, end=' ')
    print()