def solution(n):
    if n < 3: return n

    dp = [1, 1]
    for i in range(2, n+1):
        dp.append(dp[i-2] + dp[i-1])
        
    return dp[n] % 1234567