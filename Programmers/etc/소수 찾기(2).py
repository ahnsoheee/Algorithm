import math

def solution(n):
    answer = 0
    arr = [1] * (n+1)
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i]:
            for j in range(2*i, n+1, i):
                arr[j] = 0
    for i in range(2, n+1):
        if arr[i]:
            answer += 1
    return answer