def solution(numbers, hand):
    answer = ''
    keypad = [[1, 4, 7, '*'], [2, 5, 8, 0], [3, 6, 9, '#']]
    
    pl = [0, 3]
    pr = [2, 3]
    
    for num in numbers:
        if num in keypad[0]:
            answer += 'L'
            pl = [0, keypad[0].index(num)]
        elif num in keypad[2]:
            answer += 'R'
            pr = [2, keypad[2].index(num)]
        else:
            idx = keypad[1].index(num)
            
            l = abs(pl[0] - 1) + abs(pl[1] - idx)
            r = abs(pr[0] - 1) + abs(pr[1] - idx)
            print('abs', idx, l, r)
            if l == r:
                if hand == 'right':
                    answer += 'R'
                    pr = [1, idx]
                else:
                    answer += 'L'
                    pl = [1, idx]
            elif l > r:
                answer += 'R'
                pr = [1, idx]
            else:
                answer += 'L'
                pl = [1, idx]
                
    return answer