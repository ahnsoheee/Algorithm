#N0.2579

import sys

N = int(sys.stdin.readline())

score = [int(sys.stdin.readline()) for _ in range(N)]
res = []

if N > 2:
    res.append(score[0])
    res.append(res[0] + score[1])
    res.append(max(res[0] + score[2], score[1]+score[2]))

    for i in range(3, N):
        res.append(max(res[i-3] + score[i-1] + score[i], res[i-2] + score[i]))

    print(res[-1])
    
elif N == 2:
    print(max(score[0] + score[1], score[1]))
else:
    print(score[0])
