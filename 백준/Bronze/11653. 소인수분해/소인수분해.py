n = int(input())
bool = True

while bool:
    for i in range(1, n+1):
        if n % i == 0:
            if i == 1:
                continue
            else:
                n = n // i
                print(i)
                break
    if n == 1:
        bool = False
        break