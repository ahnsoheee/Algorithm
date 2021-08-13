from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
    while(people):
        if len(people) == 1:
            people.pop()
            
        else:
            heavy = people.pop()
            light = people.popleft()
            if (heavy + light) > limit:
                people.appendleft(light)
        answer += 1
    return answer