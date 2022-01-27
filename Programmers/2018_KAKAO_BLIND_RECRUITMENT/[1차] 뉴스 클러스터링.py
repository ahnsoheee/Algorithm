def solution(str1, str2):
    answer = 0
    str1_set = []
    str2_set = []
    str1 = str1.lower()
    str2 = str2.lower()
    
    for i in range(len(str1)-1):
        splited = str1[i:i+2]
        if splited.isalpha():
            str1_set.append(splited)
    
    for i in range(len(str2)-1):
        splited = str2[i:i+2]
        if splited.isalpha():
            str2_set.append(splited)
            
    intersection = []
    union = []
    
    for str1 in str1_set:
        for str2 in str2_set:
            if str1 in str2 and str1 not in intersection:
                cnt = min(str1_set.count(str1), str2_set.count(str1))
                for _ in range(cnt):
                    intersection.append(str1) 
            
            if str1 not in union:
                if str2 not in union:
                    cnt = max(str1_set.count(str1), str2_set.count(str1))
                    for _ in range(cnt):
                        union.append(str1) 
    
    # str2 합집합에 추가
    for str2 in str2_set:
        if str2 not in union:
            [union.append(str2) for _ in range(str2_set.count(str2))]

    if (len(intersection) or len(union)) == 0:
        return 65536
    
    else:
        answer = int((len(intersection) / len(union)) * 65536)
    return answer