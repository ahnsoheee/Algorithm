#No.2309 '일곱 난쟁이'

import sys

l = [int(sys.stdin.readline()) for _ in range(9)]
l.sort()
s = sum(l)

def solve(l):
    for i in range(8):
        for j in range(i+1, 9):
            if s - l[i] - l[j] == 100:
                for k in range(9):
                    if (l[k] != l[i]) and (l[k] != l[j]):
                        print(l[k])
                return

solve(l)
