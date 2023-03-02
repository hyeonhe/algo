i = 0
while True:
    i += 1
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break

    day = (V // P) * L
    diff = V % P
    if diff > L:
        day += L
    else:
        day += diff
    print(f'Case {i}: {day}')