#No.11729

import sys

N = int(sys.stdin.readline())
K = 1

def Hanoi(N, start, tmp, end):
    if (N == 1):
        print(start, end)

    else:
        Hanoi(N-1, start, end, tmp)
        print(start, end)
        Hanoi(N-1, tmp, start, end)

for i in range(N-1):
    K = 2*K + 1

print(K)
Hanoi(N, 1, 2, 3)
