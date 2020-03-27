#No. 1764

import sys

N, M = map(int, sys.stdin.readline().split())

A = []
B = [] 

for i in range(N):
    A.append(sys.stdin.readline().rstrip())

for i in range(M):
    B.append(sys.stdin.readline().rstrip())

name = sorted(list(set(A) & set(B)))

print(len(name))
for i in range(len(name)):
    print(name[i])

