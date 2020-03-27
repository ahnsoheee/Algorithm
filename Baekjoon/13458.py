#No. 13458

import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

B, C = map(int, sys.stdin.readline().split())

result = [0] * N

for i in range(N):
    if A[i] <= B:
        result[i] += 1
    else:
        result[i] += 1
        A[i] = A[i] - B

        if A[i] % C == 0:
            result[i] += (A[i] // C)
        else:
            result[i] += (A[i] // C + 1)
        
print(sum(result))
