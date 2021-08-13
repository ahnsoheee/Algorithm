import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    answer = 0
    for i in range(len(works)):
        works[i] *= -1
        
    heapq.heapify(works)
    
    for i in range(n):
        heapq.heappush(works, heapq.heappop(works) + 1) 
    
    for work in works:
        answer += pow(work, 2)
        
    return answer