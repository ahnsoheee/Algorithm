#No. 2875 '대회 or 인턴'

import sys

N, M, K = map(int, sys.stdin.readline().split())
res = 0

while(N + M >= K) and N >= 0 and M >= 0:
    N -= 2
    M -= 1
    res += 1

print(res-1)
