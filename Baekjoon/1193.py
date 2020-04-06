#No.1193

import sys

X = int(sys.stdin.readline())

count = 1
result = 1
seq = 1
d = 1

if X == 1:
    print('1/1')

else:
    while(seq < X):
        count += 1
        seq += count
        d *= -1

    if(d == -1):
        print(count+1-(seq - X + 1), end = '')
        print('/', end = '')
        print(seq - X + 1)

    else:
        print(seq - X + 1, end = '')
        print('/', end = '')
        print(count+1-(seq - X + 1))
