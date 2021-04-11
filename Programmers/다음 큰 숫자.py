def check(n):
    return list(bin(n)).count('1')

def solution(n):
    answer = n
    res = check(answer)
    
    while(1):
        answer += 1
        if check(answer) == res:
            break
        
    return answer