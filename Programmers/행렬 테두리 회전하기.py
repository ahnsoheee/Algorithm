def solution(rows, columns, queries):
    answer = []
    
    s = []
    i = 1
    
    for _ in range(rows):
        tmp = []
        for _ in range(columns):
            tmp.append(i)
            i += 1
        s.append(tmp)
        
    for query in queries:
        num = 10001
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        
        # 상
        for y in range(1, y2-y1+1):
            num = min(num, s[x1][y1])
            tmp = s[x1][y1+y]
            s[x1][y1+y] = s[x1][y1]
            s[x1][y1] = tmp
        
        # 우
        for x in range(1, x2-x1+1):
            num = min(num, s[x1][y1])
            tmp = s[x1+x][y2]
            s[x1+x][y2] = s[x1][y1]
            s[x1][y1] = tmp
        
        #하
        for y in range(1, y2-y1+1):
            num = min(num, s[x1][y1])
            tmp = s[x2][y2-y]
            s[x2][y2-y] = s[x1][y1]
            s[x1][y1] = tmp
             
        #좌
        for x in range(1, x2-x1+1):
            num = min(num, s[x1][y1])
            tmp = s[x2-x][y1]
            s[x2-x][y1] = s[x1][y1]
            s[x1][y1] = tmp
           
        answer.append(num)
    return answer