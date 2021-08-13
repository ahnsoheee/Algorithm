def check(s):
    stack = []
    for w in s:
        if w in ['[', '{', '(']:
            stack.append(w)
        elif w == ']' and (len(stack) == 0 or stack.pop() != '['):
            return 0
        elif w == '}' and (len(stack) == 0 or stack.pop() != '{'):
            return 0
        elif w == ')' and (len(stack) == 0 or stack.pop() != '('):
            return 0
    
    if len(stack) != 0:
        return 0

    return 1

        
def solution(s):
    answer = check(s)
    for _ in range(len(s)-1):
        s = s[1:] + s[0]
        answer += check(s)
        
    return answer