#No.1316

N = int(input())
cnt = N

for i in range(N):
    word = list(input())
    s = list(set(word))
    err = 0

    for j in s:
        idx = []
        if err == 0: 
            for k in range(len(word)):
                if j == word[k]:
                    idx.append(k)

            for k in range(len(idx)-1):
                if (idx[k+1] - idx[k]) != 1:
                    err = 1
                    break
        else:
            break
        
    if err == 1:
        cnt -= 1
        
print(cnt)
