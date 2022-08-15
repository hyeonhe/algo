def solution(new_id):
    answer = ''


#     1단계
    new_id = new_id.lower()

#     2단계
    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer += i

#     3단계
    answer = list(answer)
    cnt = 0
    for i in range(len(answer)):
        if answer[i] == '.' and cnt == 0:
            cnt += 1
        elif answer[i] == '.':
            answer[i] = ' '
        else:
            cnt = 0

#     4단계
    if len(answer) > 0 and answer[0] == '.':
        answer.remove(answer[0])
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    answer = "".join(answer)
    answer = answer.replace(" ", "")

#     5단계
    if answer == '':
        answer = 'a'

#     6단계
    if len(answer) >= 16:
        answer = answer[:15]

    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]

#     7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer