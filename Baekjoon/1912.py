#No.1912 '연속합'

import sys

n = int(sys.stdin.readline())

seq = list(map(int, sys.stdin.readline().split()))

dp = [seq[0]]
for i in range(1, n):
    dp.append(max(dp[i-1] + seq[i], seq[i]))

print(max(dp))
