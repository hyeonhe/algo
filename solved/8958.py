n = int(input())

for i in range(n):
    a = list(input())

    # 각 테스트 케이스의 점수
    answer = 0
    # 연속해서 맞췄을 때 점수를 세기 위한 변수
    count = 0

    for j in a:
        if j == 'O':
            count += 1
            answer += count
        elif j == 'X':
            count = 0

    print(answer)