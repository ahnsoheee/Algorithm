#N0. 1110

import sys

N = int(sys.stdin.readline())

new = N
count = 0

while(new != N or count == 0):
    one = new % 10
    ten = new // 10
    s = one + ten
    new = int(str(one)+str(s%10))
    count += 1

print(count)

