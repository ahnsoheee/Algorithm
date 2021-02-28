def solution(n, lost, reserve):
    answer = 0
    students = [1] * n
    
    for i in lost:
        students[i-1] -= 1
    
    for i in reserve:
        students[i-1] += 1
        
    for i in range(n):
        if students[i] == 0:
            if i != 0 and students[i-1] >= 2:
                students[i] += 1
                students[i-1] -= 1
            elif i != n-1 and students[i+1] >= 2:
                students[i] += 1
                students[i+1] -= 1
    
    for i in range(n):
        if students[i] > 0:
            answer += 1
            
    return answer