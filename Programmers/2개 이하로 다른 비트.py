def solution(numbers):
    answer = []
    
    for number in numbers:
        binary = list('0' + bin(number)[2:])
        
        if number % 2 == 0:
            binary[-1] = '1'
        else:
            idx = ''.join(binary).rfind('0')
            binary[idx] = '1'
            binary[idx + 1] = '0'
        
        answer.append(int(''.join(binary), 2))
        
    return answer