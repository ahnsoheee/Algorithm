def solution(lottos, win_nums):
    answer = []
    tmp = [0, 0]
    
    for lotto in lottos:
        if lotto == 0:
            tmp[0] += 1
            
        elif lotto in win_nums:
            tmp[0] += 1
            tmp[1] += 1
    
    for t in tmp:
        if t == 6:
            answer.append(1)
        elif t == 5:
            answer.append(2)
        elif t == 4:
            answer.append(3)
        elif t == 3:
            answer.append(4)
        elif t == 2:
            answer.append(5)
        else:
            answer.append(6)
            
    return answer