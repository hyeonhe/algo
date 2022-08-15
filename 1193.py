# 포기할래!
x = int(input())

cnt = 1
while x > cnt:
    x -= cnt
    cnt += 1

    if cnt % 2 == 0:
        a = x
        b = cnt - x + 1