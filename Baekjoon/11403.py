#No. 11403 '경로 찾기'


import sys

N = int(sys.stdin.readline())

s = []
check = [0] * N

def dfs(v):
    for i in range(N):
        if check[i] == 0 and s[v][i] == 1:
            check[i] = 1
            dfs(i)

for i in range(N):
    s.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    dfs(i)
    
    for j in range(N):
        if check[j] == 1:
            print(1, end = ' ')
        else:
            print(0, end = ' ')
    print()
    check = [0] * N
