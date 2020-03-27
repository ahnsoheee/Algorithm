#No. 1065

import sys

N = int(sys.stdin.readline())
cnt = 0

for i in range(1, N+1):
    num = list(str(i)) 

    for j in range(len(num)):
        num[j] = int(num[j])

    if len(num) == 1:
        cnt += 1
    elif len(num) == 2:
        cnt += 1
    else:
        for j in range(len(num)-2):    
            if (num[j+1] - num[j]) == (num[j+2] - num[j+1]):
                cnt += 1
            else:
                break

print(cnt)
