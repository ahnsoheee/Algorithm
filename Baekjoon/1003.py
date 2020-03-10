#No.1003 - Fibonacci

T = int(input())

for i in range(T):
    N = int(input())
    
    zero = 1
    one = 0

    for j in range(N):
        temp = one
        one = one + zero
        zero = temp
        
    print(zero, one)
