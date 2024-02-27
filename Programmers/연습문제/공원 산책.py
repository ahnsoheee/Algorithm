# 공원 산책

def solution(park, routes):
    x, y = 0, 0
    sx, sy = len(park), len(park[0])
    
    for i in range(sx):
        for j in range(sy):
            if park[i][j] == 'S':
                x, y = i, j
                break
                
    
    for route in routes:
        r = route.split(" ")
        a, b = r[0], int(r[1])
        
        nx, ny = x, y
        flag = True
        
        for _ in range(b):
            if a == "N":
                nx -= 1
            elif a == "S":
                nx += 1
            elif a == "W":
                ny -= 1
            elif a == "E":
                ny += 1
        
            if 0 <= nx < sx and 0 <= ny < sy and park[nx][ny] != 'X':
                continue
            else:
                flag = False
                break
        
        if flag == True:
            x, y = nx, ny
            
    return [x, y]