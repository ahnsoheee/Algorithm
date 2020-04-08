#No.7568

import sys

input = sys.stdin.readline
N = int(input())

people = [list(map(int, input().split())) for _ in range(N)]

result = []

for w, h in people:
    cnt = 1
    for a, b in people:
        if (w < a) and (h < b):
            cnt += 1
    result.append(cnt)

for i in range(N):
    print(result[i], end = ' ')
