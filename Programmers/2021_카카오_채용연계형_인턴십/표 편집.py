#https://programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, cmd):
    answer = ['O'] * n
    deleted = []
    table = {i: [i-1, i+1] for i in range(n)}
    
    for command in cmd:
        if command[0] == 'D':
            for _ in range(int(command[2:])):
                k = table[k][1]

        elif command[0] == 'U':
            for _ in range(int(command[2:])):
                k = table[k][0]

        elif command[0] == 'C':
            prev, next = table[k]
            answer[k] = 'X'
            deleted.append([k, table[k]])
            
            if prev == -1:
                table[next][0] = prev
                k = next
                
            elif next == n:
                table[prev][1] = next
                k = prev
                
            else:
                table[prev][1] = next
                table[next][0] = prev
                k = next
                
        else:
            i, [prev, next] = deleted.pop()
            answer[i] = 'O'

            if prev == -1:
                table[next][0] = i
            elif next == n:
                table[prev][1] = i
            else:
                table[prev][1] = i
                table[next][0] = i
            
    return "".join(answer)