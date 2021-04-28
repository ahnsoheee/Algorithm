def solution(x):
    answer = True
    num = 0
    
    for n in list(str(x)):
        num += int(n)
    
    if x % num != 0:
        return False
    
    return answer