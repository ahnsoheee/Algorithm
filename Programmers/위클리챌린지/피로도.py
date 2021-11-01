from itertools import permutations

def solution(k, dungeons):
    result = []
    
    for permutation in permutations([i for i in range(len(dungeons))]):
        value, answer = k, 0   
        
        for i in permutation:
            if dungeons[i][0] <= value:
                answer += 1
                value -= dungeons[i][1]

        result.append(answer)
        
    return max(result)