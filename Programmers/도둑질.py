def solution(money):
    answer = 0
    length = len(money)
    dp = [0] * length
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    
    for i in range(2, length-1):
        dp[i] = max(dp[i-2] + money[i], dp[i-1])
    
    answer = max(dp)
    
    dp[0] = 0
    dp[1] = money[1]
    
    for i in range(2, length):
        dp[i] = max(dp[i-2] + money[i], dp[i-1])

    answer = max(answer, max(dp))
    
    return answer