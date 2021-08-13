# 위장

def solution(clothes):
    answer = 1
    clothe = {}
    
    for i in range(len(clothes)):
        if clothes[i][1] not in clothe:
            clothe[clothes[i][1]] = 1
        else:
            tmp = clothe[clothes[i][1]]
            tmp += 1
            clothe[clothes[i][1]] = tmp
            
    for c in clothe:
        answer *= (clothe[c] + 1)
        
    answer -= 1
    
    return answer
