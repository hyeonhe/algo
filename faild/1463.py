x = int(input())
count = 0

while x != 1:
    if x == 1:
        break
    elif x % 3 == 0:
        x //= 3
        count += 1
        if x == 1:
            break
    elif x % 2 == 0:
        x //= 2
        count += 1
        if x == 1:
            break
    else:
        x -= 1
        count += 1
        if x == 1:
            break

print(count)