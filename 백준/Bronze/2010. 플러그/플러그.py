import sys
input = sys.stdin.readline
n = int(input())
ans = 0
ans += sum(list(int(input()) for _ in range(n)))
ans -= n
print(ans + 1)