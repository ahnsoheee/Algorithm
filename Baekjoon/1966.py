#No.1966 '프린터 큐'

import sys

for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())

    weight = list(map(int, sys.stdin.readline().split()))

    res = 1
    index = [i for i in range(N)]

    while(1):
        if (index[0] == M) and (weight[index[0]] == max(weight)):
            break
        else:
            if weight[index[0]] == max(weight):
                weight[index[0]] = -1
                index.remove(index[0])
                res += 1
            else:
                index.append(index[0])
                index.remove(index[0])

    print(res)
