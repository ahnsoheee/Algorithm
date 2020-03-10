#No.1904

import sys
N = int(sys.stdin.readline())

a = 1
b = 0 
for i in range(N):
    temp = a % 15746
    a = (a + b) % 15746
    b = temp

print(a)
