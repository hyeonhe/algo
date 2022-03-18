a, b = map(int, input().split())
a -= 1 # 좌표 평면으로 접근하려면 1을 빼준다.
b -= 1
print(abs(a//4-b//4) + abs(a%4-b%4))