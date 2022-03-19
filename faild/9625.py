# https://www.acmicpc.net/problem/9625
# 피보나치 수열이래.. 그리고 시간초과
k = int(input())
# 'B'는 'BA'로 'A'는 'B'로 바뀜
word = 'A'
for i in range(k):
    word = word.replace('A', 'C')
    word = word.replace('B', 'BA')
    word = word.replace('C', 'B')

print(word.count('A'), word.count('B'))
