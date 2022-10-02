n = int(input())

for i in range(n):
    a = list(input())

    answer = 0
    count = 0

    for j in a:
        if j == 'O':
            count += 1
            answer += count
        elif j == 'X':
            count = 0

    print(answer)