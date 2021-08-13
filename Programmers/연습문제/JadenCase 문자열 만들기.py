def solution(s):
    answer = ''
    s = s.lower()
    word = s.split(' ')
    for w in word:
        answer += w.capitalize() + ' '
        
    return answer[:-1]