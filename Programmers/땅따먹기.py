import copy

def solution(land):
    answer = 0
    length = len(land)
    dp = copy.deepcopy(land)
    
    for i in range(1, length):
        for j in range(4):
            for k in range(4):
                if k != j:
                    dp[i][j] = max(dp[i][j], land[i][j] + dp[i-1][k])
                    
    answer = max(dp[length-1])
    return answer