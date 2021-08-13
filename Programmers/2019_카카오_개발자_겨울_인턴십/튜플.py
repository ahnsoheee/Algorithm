def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s = sorted(s,key = lambda x: len(x))
    
    for num in s:
        num = num.split(',')
        for n in num:
            if int(n) not in answer:
                answer.append(int(n))
            
    return answer