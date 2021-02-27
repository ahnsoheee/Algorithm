def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        i, j, k = commands[i][0], commands[i][1], commands[i][2]
        tmp = sorted(array[i-1:j])
        answer.append(tmp[k-1])
    return answer