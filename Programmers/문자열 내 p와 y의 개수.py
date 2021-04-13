def solution(s):
    p, y = 0, 0
    
    for a in s:
        if a == 'p' or a == 'P':
            p += 1
        elif a == 'y' or a == 'Y':
            y += 1

    if p != y:
        return False
    
    return True