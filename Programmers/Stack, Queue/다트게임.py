def solution(dartResult):
    answer = 0
    score = []
    dartResult = dartResult.replace('10', 'A')
    
    for result in list(dartResult):
        if result.isdigit() or result == 'A':
            if result == 'A':
                score.append(10)
            else:
                score.append(int(result))
        elif result == 'D':
            score.append(score.pop() ** 2)
        elif result == 'T':
            score.append(score.pop() ** 3)
        elif result == '*':
            num = score.pop()
            if len(score):
                score[-1] *= 2
            score.append(2 * num)
        elif result == '#':
            score[-1] *= -1
                
    return sum(score)