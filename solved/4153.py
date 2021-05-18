while True:
    a, b, c = sorted(map(int, input().split()))
    if a == 0:
        break
    elif c*c == b*b + a*a:
        print("right")
    else:
        print("wrong")
