#No.2217 '로프'

import sys

N = int(sys.stdin.readline())

rope = [int(sys.stdin.readline()) for _ in range(N)]
rope.sort(reverse = True)
res = []

for i in range(N):
    res.append(rope[i]*(i+1))
print(max(res))
