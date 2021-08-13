def solution(d, budget):
    answer = 0
    d.sort()
    
    for c in d:
        budget -= c
        
        if budget >= 0:
            answer += 1
        else:
            return answer
        
    return answer