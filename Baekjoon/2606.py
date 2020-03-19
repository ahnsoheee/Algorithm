#No.2606

import sys

N = int(sys.stdin.readline())
T = int(sys.stdin.readline())

s = [[0] * N for i in range(N)]
check = [0 * N for i in range(N)]
virus = []

def dfs(v):
   virus.append(v)
   check[v-1] = 1
   for i in range(N):
      if check[i] == 0 and s[v-1][i] == 1:
         dfs(i+1)
         
   

for i in range(T):
   r, c = map(int, sys.stdin.readline().split())

   s[r-1][c-1] = 1
   s[c-1][r-1] = 1

dfs(1)
print(len(virus) - 1)
