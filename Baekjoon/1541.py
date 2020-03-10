#No.1541

expression = input().split('-')

part = []
for e in expression:
    temp = list(map(int, e.split('+')))
    part.append(sum(temp))

result = part[0]
for i in range(1, len(part)):
    result -= part[i]

print(result)
