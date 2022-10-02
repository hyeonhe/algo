from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    # 함수
    p = input()
    # 배열의 길이
    n = int(input())
    array = input()
    queue = deque(array[1:-1].split(','))

    if n == 0:
        queue = []

    # 뒤집는 횟수
    flag = 0

    for cmd in p:
        # 에러 발생 변수
        error = 0
        if cmd == 'R':
            flag += 1
        elif cmd == 'D':
            if len(queue) == 0:
                print('error')
                error = 1
                break

            # 뒤집는 횟수가 짝수이면 첫번째 수 버리기
            if flag % 2 == 0:
                queue.popleft()
            # 홀수이면 마지막 수 버리기
            else:
                queue.pop()

    # 뒤집는 횟수가 홀수이면 뒤집기
    if flag % 2 == 1:
        queue.reverse()

    if error == 0:
        print('[' + ','.join(queue) + ']')