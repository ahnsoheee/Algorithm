import math

def solution(progresses, speeds):
    answer = []
    progress = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    
    idx = 0
    for i in range(len(progress)):  
        if progress[i] > progress[idx]:
            answer.append(i-idx)
            idx = i
    answer.append(len(progress) - idx)
    return answer