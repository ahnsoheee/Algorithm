import re

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub('[^0-9a-z\.\-\_]', '', answer)
    answer = re.sub('[.]+', '.', answer)
    if answer.startswith('.'):
        answer = answer[1:]
    if answer.endswith('.'):
        answer =  answer[:-1]
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if answer.endswith('.'):
            answer = answer[:-1]
    if len(answer) <= 2:
        answer += answer[-1] * (3-len(answer))

    return answer