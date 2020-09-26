# 두 개 뽑아서 더하기


from itertools import combinations

def solution(numbers):
    answer = []
    
    com = list(combinations(numbers, 2))
    
    for num in com:
        answer.append(sum(num))
    answer = list(set(answer))
    answer = sorted(answer)
    return answer
