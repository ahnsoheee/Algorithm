def grade(score):
    if score >= 90: return 'A'
    elif score >= 80 and score < 90: return 'B'
    elif score >= 70 and score < 80: return 'C'
    elif score >= 50 and score < 70: return 'D'
    return 'F'
    
def solution(scores):
    answer = ''
    length = len(scores)
    for col in range(length):
        score = []
        for row in range(length):
            score.append(scores[row][col])
        
        result = sum(score)
        max_score = max(score)
        min_score = min(score)
        if max_score == scores[col][col] and score.count(max_score) == 1:
            result -= max_score
            result = result / (length-1)
        elif min_score == scores[col][col] and score.count(min_score) == 1:
            result -= min_score
            result = result / (length-1)
        else:
            result = result / length
            
        answer += grade(result)
        
    return answer