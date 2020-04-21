#No.2156 '포도주 시식'

import sys

n = int(sys.stdin.readline())

s = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] * n
dp[0] = s[0]

for i in range(1, n):
    if i == 1:
        dp[1] = s[0] + s[1]
    elif i == 2:
        dp[2] = max(s[0]+s[2], s[1]+s[2])
    elif i == 3:
        dp[i] = max(dp[i-2], dp[i-3]+s[i-1]) + s[i]
    else:
        dp[i] = max(dp[i-2], dp[i-3]+s[i-1], dp[i-4] + s[i-1]) + s[i]
print(max(dp))
