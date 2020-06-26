#1759 '암호 만들기'

import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())

string = list(map(str, sys.stdin.readline().split()))
string = sorted(string)
com = list(combinations(string, L))

col = ['a', 'e', 'i', 'o', 'u']

for s in com:
    tmp = 0
    for i in range(L):
        if s[i] in col:
            tmp += 1
        
    if tmp >= 1 and L-tmp >= 2:
        print(''.join(s))
