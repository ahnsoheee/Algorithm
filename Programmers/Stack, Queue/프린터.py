def solution(priorities, location):
    answer = 0
    priority = []
    
    for i in range(len(priorities)):
        priority.append((priorities[i], i))
    
    while(priority):
        max_p = max(priority)
        p = priority.pop(0)
        
        if p[0] != max_p[0]:
            priority.append(p)
        else:
            answer += 1
            if p[1] == location:
                break
            
    return answer