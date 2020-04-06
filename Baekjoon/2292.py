import sys

N = int(sys.stdin.readline())

count = 0
result = 1
seq = 1

if N == 1:
    print(result)

else:
    while(seq < N):
        count += 6
        seq += count
        result += 1

    print(result)
