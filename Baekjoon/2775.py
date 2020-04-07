#N0.2775

import sys

T = int(sys.stdin.readline())

for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    a = [i for i in range(1, n+1)]

    for j in range(k):
        for k in range(1, n):
            a[k] += a[k-1]
    
    print(a[n-1])
