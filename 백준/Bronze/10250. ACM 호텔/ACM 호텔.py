T = int(input())
for i in range(T):
    h, w, n = map(int, input().split())

    if n % h == 0:
        floor = h
    elif h == 1:
        floor = 1
    else:
        floor = n % h

    ans = str(floor)
    if n % h == 0:
        ho = n//h
    else:
        ho = n//h + 1
    if ho//10 == 0:
        ans += '0'
    ans += str(ho)

    print(int(ans))