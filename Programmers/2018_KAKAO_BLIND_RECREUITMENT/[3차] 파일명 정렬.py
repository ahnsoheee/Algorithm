import re

def solution(files):
    answer = []
    head, number, tail = '', '', ''
    
    for file in files:
        answer.append(re.split(r'([0-9]+)', file))

    answer = sorted(answer, key = lambda x: (x[0].lower(), int(x[1])))
        
    return [''.join(a) for a in answer]