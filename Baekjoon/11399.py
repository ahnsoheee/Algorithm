#No.11399 - ATM

N = int(input())

people = sorted(list(map(int, input().split())))

result = time = 0
for i in range(0, N):
    time += people[i]
    result += time
print(result)
