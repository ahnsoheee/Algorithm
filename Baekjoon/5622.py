#No.5622

eng = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}

N = list(str(input()))
time = 0

for i in range(len(N)):
    for key in eng:
        if N[i] in eng[key]:
            time += (key + 1)
            
print(time)

