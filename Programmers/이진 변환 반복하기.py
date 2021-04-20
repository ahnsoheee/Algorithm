def solution(s):
    answer = [0, 0]

    while(s != '1'):
        answer[0] += 1
        n = ''
        for num in s:
            if num == '1':
                n += '1'
            else: answer[1] += 1
        s = bin(len(n))[2:]
        
    return answer

solution('110010101001')