def solution(N, stages):
    answer = []
    s = {}
    stages = sorted(stages)
    for n in range(1, N+1):
        s[n] = 0
    user = len(stages)
    prev = 1
    for i in range(1, N+1):
        if i >= prev and user != 0:
            cnt = stages.count(i)
            s[i] = cnt / user
            prev += 1
            user -= cnt
    
    s = sorted(s.items(), key = lambda x: x[1], reverse = True)

    for key in s:
        answer.append(key[0])
        
    return answer