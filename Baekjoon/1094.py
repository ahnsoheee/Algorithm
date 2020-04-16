#No.1094 '막대기'

import sys

X = int(sys.stdin.readline())

binary = bin(X)
tmp = list(map(str, binary))
print(tmp.count('1'))
