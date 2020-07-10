# 모의고사

def solution(answers):
    answer = []
    
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    res = [0, 0, 0]
    
    for i in range(len(answers)):
        ans = answers[i]
        
        if (s1[i % 5] == ans):
            res[0] += 1
        if (s2[i % 8] == ans):
            res[1] += 1
        if (s3[i % 10] == ans):
            res[2] += 1
    
    if sum(res) == 0:
        return answer
    
    else:
        for i in range(3):
            if res[i] == max(res):
                answer.append(i+1)
                
    return answer
