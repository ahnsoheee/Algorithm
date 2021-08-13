def solution(genres, plays):
    answer = []
    dic = {}
    album = {}
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = plays[i]
            album[genres[i]] = [[plays[i], i]]
        else:
            dic[genres[i]] += plays[i]
            album[genres[i]].append([plays[i], i])
            
    dic = sorted(dic.items(), key=(lambda x:x[1]), reverse = True)
    
    for genre in dic:
        tmp = album[genre[0]]
        tmp = sorted(tmp, key=lambda x:x[0], reverse = True)
        
        if len(tmp) > 1:
            answer.append(tmp[0][1])
            answer.append(tmp[1][1])
        else:
            answer.append(tmp[0][1])
            
    return answer