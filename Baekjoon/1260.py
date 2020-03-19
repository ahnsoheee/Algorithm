#No.1260

N, M, V = map(int, input().split())

s = [[0] * N for i in range(N)]
check = [0 for i in range(N)]

def dfs(v):    
   check[v-1] = 1
   print(v, end = ' ')
   for i in range(N):
      if(check[i] == 0 and s[v-1][i] == 1):
         dfs(i+1)
      
      
def bfs(v):
   check[v-1] = 0
   queue = [v]
   while(queue):
      v = queue[0]
      print(v, end = ' ')
      del queue[0]
      for i in range(N):
         if check[i] == 1 and s[v-1][i] == 1:
            queue.append(i+1)
            check[i] = 0

for i in range(M):
    r, c = map(int, input().split())
    s[r-1][c-1] = 1
    s[c-1][r-1] = 1

dfs(V)
print()
bfs(V)
