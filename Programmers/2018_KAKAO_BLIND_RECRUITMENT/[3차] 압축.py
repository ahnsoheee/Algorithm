def solution(msg):
    answer = []
    _dict = {}
    k = 27

    for i in range(26):
        _dict[chr(65+i)] = i+1

    w, c = 0, 1
    while True:
        if c == len(msg):
            answer.append(_dict[msg[w: c]])
            break
        if msg[w: c+1] not in _dict:
            _dict[msg[w: c+1]] = k
            answer.append(_dict[msg[w: c]])
            w = c
            k += 1

        c += 1

    return answer
