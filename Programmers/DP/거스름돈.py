def solution(n, money):
    dp = [[0] * (n+1) for _ in range(len(money)+1)]
    dp[0][0] = 1
    
    for i in range(1, len(money)+1):
        for j in range(n+1):
            if money[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-money[i-1]]
                
    return dp[-1][-1]