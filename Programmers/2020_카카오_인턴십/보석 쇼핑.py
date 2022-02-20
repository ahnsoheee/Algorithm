# https://programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    answer = [0, len(gems)-1]
    l, r = 0, 0
    types = len(set(gems))
    check = {gems[0]: 1}

    while r < len(gems) and l < len(gems):
        if len(check) == types: # 모든 보석을 포함했는지
            if r - l < answer[1] - answer[0]: # 더 좋은 결과인지 확인
                answer = [l, r]
            if check[gems[l]] == 1:
                del check[gems[l]]
            else:
                check[gems[l]] -= 1
            l += 1
        else:
            r += 1
            if r == len(gems):
                break
                
            if gems[r] not in check:
                check[gems[r]] = 1
            else:
                check[gems[r]] += 1
            
    answer[0] += 1
    answer[1] += 1
    
    return answer