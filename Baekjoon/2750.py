#N0.2750

import sys

N = int(sys.stdin.readline())

num = [int(sys.stdin.readline()) for _ in range(N)]

def bubbleSort(num, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if (num[j] > num[j+1]):
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp

bubbleSort(num, N)

for i in range(N):
    print(num[i])
