# No. 1676 '팩토리얼 0의 개수'

import sys

N = int(sys.stdin.readline())
i = 1
ans = 0

while (i * 5 <= N):
  ans += (N // (i * 5))
  i *= 5

print(ans)
