#No.2748 - Fibonacci

n = int(input())

seq = [0, 1]
for i in range(2, n+1):
    seq.append(seq[i-1] + seq[i-2])
    
print(seq[n])
