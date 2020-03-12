#N0.2798

import sys

N, M = map(int, sys.stdin.readline().split())

card = list(map(int, sys.stdin.readline().split()))

num = []

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if card[i] + card[j] + card[k] <= M:
                num.append(card[i] + card[j] + card[k])

print(max(num))

