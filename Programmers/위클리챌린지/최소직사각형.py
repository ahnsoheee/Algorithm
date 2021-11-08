def solution(sizes):
    answer = 0
    x, y = 0, 0
    
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        x, y = max(x, size[0]), max(y, size[1])
        
   
    return x * y