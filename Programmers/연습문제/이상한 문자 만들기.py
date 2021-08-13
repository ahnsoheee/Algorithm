def solution(s):
    answer = ''
    word = s.split(' ')

    for w in word:
        for i in range(len(w)):
            if i % 2 == 0:
                answer += w[i].upper()
            else:
                answer += w[i].lower()
        answer += ' '
        
    return answer[:-1]