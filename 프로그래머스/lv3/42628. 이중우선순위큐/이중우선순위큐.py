def solution(operations):
    answer = []
    queue = []
    for command in operations:
        if command == 'D 1':
            if len(queue) != 0:
                queue.remove(max(queue))
            else:
                continue
        elif command == 'D -1':
            if len(queue) != 0:
                queue.remove(min(queue))
            else:
                continue
        else:
            i, num = command.split()
            queue.append(int(num))

    if queue == []:
        answer = [0, 0]
    else:
        answer.append(max(queue))
        answer.append(min(queue))
    return answer
    