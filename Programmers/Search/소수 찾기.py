import itertools

def solve(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

def solution(numbers):
    answer = []
    arr = []
    
    for i in range(1, len(numbers)+1):
        arr.extend(list(map(''.join, itertools.permutations(numbers, i))))
    arr = list(set(arr))
    
    for num in arr:
        n = int(num)
        if solve(n):
            answer.append(n)

    return len(set(answer))