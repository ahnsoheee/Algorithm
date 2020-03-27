#No.1157

word = input()

s = list(word.lower())

alpha = list(set(s)) 

cnt = {} 

for i in range(len(alpha)):
    cnt[alpha[i]] = s.count(alpha[i])
    
result = []

for key in cnt.keys():
    if cnt[key] == max(cnt.values()):
        result.append(key)

if len(result) > 1:
    print('?')
else:
    print(result[0].upper())
