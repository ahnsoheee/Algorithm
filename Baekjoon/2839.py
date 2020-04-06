#No.2839

import sys

N = int(sys.stdin.readline())

result = 0

while(N > 0):
    if N % 5 == 0:
        result += (N//5)
        N -= (N//5)*5

    else:
        N -= 3
        result += 1

if(N < 0):
    print(-1)
else: 
    print(result)
