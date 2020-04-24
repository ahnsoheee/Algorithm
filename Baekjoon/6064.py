#No.6064 '카잉 달력'

import sys

T = int(sys.stdin.readline())

def gcd(a, b):
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    return b

def lcm(a, b):
    return a*b//gcd(a,b)
    
for i in range(0, T):
    M, N, x, y = map(int, input().split())
    l = lcm(M, N)
    tmpY = x-1
    count = x-1

    while (1):
        tmpY = count % N
        
        if tmpY == y-1:
            print(count + 1)
            break
        else:
            count += M

            if count > l:
                print(-1)
                break
