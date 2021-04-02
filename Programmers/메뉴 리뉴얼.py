from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = [] 
    
    for c in course:
        menu = []
        for order in orders:
            menu += (combinations(sorted(order), c))
        counter = Counter(menu)
        if len(counter) != 0 and max(counter.values()) != 1:
            for cnt in counter:
                if counter[cnt] == max(counter.values()):
                    answer.append(''.join(cnt))
    answer = sorted(answer)
    return answer