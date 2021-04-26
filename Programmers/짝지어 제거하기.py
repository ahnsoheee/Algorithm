def solution(s):
    stack = []
    for w in s:
        if len(stack) == 0:
            stack.append(w)
        else:
            if stack[-1] == w:
                stack.pop()
            else:
                stack.append(w)
    if len(stack) == 0:
        return 1
    else: 
        return 0