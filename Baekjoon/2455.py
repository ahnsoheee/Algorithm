#No.2455 '지능형 기차'

import sys

people = [0]
for _ in range(4):
    N, M = map(int, sys.stdin.readline().split())

    people.append(M-N + people[-1])
print(max(people))
