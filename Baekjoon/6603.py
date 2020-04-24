#No.6603 '로또'

import sys

def lotto(n, k):

    if k == 6:
        for i in range(6):
            print(ans[i], end = ' ')
        print()
        return
    
    for i in range(n, seq[0]+1):
        ans[k] = seq[i]
        lotto(i+1, k+1)

while(1):
    seq = list(map(int, sys.stdin.readline().split()))
    ans = [0] * 6

    if seq[0] == 0:
        break
    
    lotto(1, 0)
    print()
