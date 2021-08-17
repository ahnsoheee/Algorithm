def isBalanced(u):
    stack = []
    for i in range(len(u)):
        if u[i] == '(':
            stack.append(u[i])
        else:
            if len(stack) == 0: return False
            stack.pop()
            
    return True

def reverse(v):
    res = ''
    for i in range(len(v)):
        if v[i] == '(':
            res += ')'
        else:
            res += '('
            
    return res

def solution(p):
    answer = ''
    
    if p == '': return p
    
    u, v = '', ''
    cnt = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
            
    if isBalanced(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse(u[1:-1])
    