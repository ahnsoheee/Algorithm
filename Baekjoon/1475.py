#No. 1475 '방 번호'

import sys

N = str(sys.stdin.readline())
N = N.replace('9', '6')

res = 0

for i in range(9):
    cnt = N.count(str(i))
    
    if i == 6:
        cnt = (cnt // 2 + cnt % 2)

    if res < cnt:
        res = cnt
        
print(res)
