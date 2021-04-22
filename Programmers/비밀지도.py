def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        map1 = list(bin(arr1[i])[2:].zfill(n))
        map2 = list(bin(arr2[i])[2:].zfill(n))
        
        res = ''
        for j in range(n):
            if map1[j] == '1' or map2[j] == '1':
                res += '#'
            else:
                res += ' '
                
        answer.append(res)
    
    return answer