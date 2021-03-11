import sys

n, k = map(int, sys.stdin.readline().split())

coin = sorted(list(int(sys.stdin.readline()) for _ in range(n)))
dp = [10001] * (k+1)
dp[0] = 0

for i in range(1, k+1):
  for c in coin:
    if i-c < 0: 
      break
    dp[i] = min(dp[i], dp[i-c]+1)

if dp[k] == 10001:
  print(-1)
else:
  print(dp[k])