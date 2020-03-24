import sys

C = int(sys.stdin.readline())

for i in range(C):
    s = list(map(int, sys.stdin.readline().split()))
    N = s[0]

    avg = sum(s[1:])/N
    cnt = 0
    
    for j in range(1, N+1):
        if avg < s[j]:
            cnt += 1
    
    print('%0.3f' %round(cnt/N*100, 3) + '%')
