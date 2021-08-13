def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    
    for skill_tree in skill_trees:
        tmp = []
        for s in skill_tree:
            if s in skill:
                tmp.append(s)
        
        res = 1
        
        for i in range(len(tmp)): 
            if tmp[i] != skill[i]:
                res = False
                break
              
        if res == 1:
            answer += 1
            
    return answer