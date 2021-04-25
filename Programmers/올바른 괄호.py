def solution(s):
    answer = True
    stack = []
    
    for w in s:
        if w == '(':
            stack.append(w)
        elif w == ')' and len(stack) != 0:
            stack.pop()
        else:
            return False  
        
    if len(stack) != 0:
        return False
    
    return True