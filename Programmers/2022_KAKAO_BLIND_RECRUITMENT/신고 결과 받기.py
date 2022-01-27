def solution(id_list, report, k):
        
    answer = []
    reported, result = {}, {}
    
    for id in id_list:
        reported[id] = []
        result[id] = 0
        
    for r in set(report):
        r = r.split(" ")
        reported[r[1]].append(r[0])
        
    for key, value in reported.items():
        if len(value) >= k:
            for id in value:
                result[id] += 1
    
    for id in id_list:
        answer.append(result[id])
    
    
    return answer