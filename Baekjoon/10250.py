#N0.10250

import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    if N % H == 0:
        print(H*100 + (N//H))
    else:
        print(N % H * 100 + (N//H) + 1)
