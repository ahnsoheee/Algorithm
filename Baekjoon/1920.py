#N0.1920

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A = sorted(A)

result = []
def binarySerach(A, x, low, high):
    if low > high:
        return 0

    else:
        mid = (low+high) // 2
        
        if x  == A[mid]:
            return 1
        elif x < A[mid]:
            return (binarySerach(A, x, low, mid -1))
        else:
            return(binarySerach(A, x, mid+1, high))

for i in range(M):
    print(binarySerach(A, B[i], 0, N-1))
