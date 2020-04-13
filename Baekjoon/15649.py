#N0.15649

#1

import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

num = [i for i in range(1,N+1)]

result = permutations(num, M)
for i in result:
    print(' '.join(map(str, i)))
    
    
#2

import sys

N, M = map(int, sys.stdin.readline().split())

def permutation(index, n, m):
    if index == m:
        #print(' '.join(map(str, res)))
        print(*res)
        return

    for i in range(1, n+1):
        if(visited[i-1] == 0):
            visited[i-1] = 1
            res[index] = i
            permutation(index+1, n, m)
            visited[i-1] = 0

res = [0] * M
visited = [0] * N
permutation(0, N, M)
