#No.14889 '스타트와 링크'

import sys
from itertools import combinations

N = int(sys.stdin.readline())

s = []
for _ in range(N):
    s.append(list(map(int, sys.stdin.readline().split())))

people = [i for i in range(N)]
com_people = list(combinations(people, N//2))
length = len(com_people)//2
com = com_people[0:length]

res = 100
for i in range(length):
    check = [0] * N    
    temp1 = 0
    temp2 = 0
    for j in range(N//2):
        check[com[i][j]] = 1
        for k in range(N//2):
            if j != k:
                temp1 += s[com[i][j]][com[i][k]]

    remain = []
    
    for j in range(N):
        if check[j] == 0:
            remain.append(j)
    
    for j in range(N//2):
        for k in range(N//2):
            if j != k:
                temp2 += s[remain[j]][remain[k]]
    
   
    res = min(res, abs(temp1 - temp2))
    
print(res)
