#No.8958

import sys

N = int(sys.stdin.readline())

for i in range(N):
    s = list(str(sys.stdin.readline()))

    cnt = 0
    score = 0

    for i in range(len(s)):
        if s[i] == 'O':
            cnt += 1
            score += cnt

        else:
            cnt = 0
        

    print(score)
