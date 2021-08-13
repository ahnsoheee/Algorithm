# 단어 변환

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    answer = 0
    start = [begin]

    while(len(words) != 0):
        for s in start:
            tmp = []
            for word in words:
                cnt = 0
                for i in range(len(word)):
                    if s[i] != word[i]:
                        cnt += 1
                    if cnt == 2:
                        break
                if cnt == 1:
                    tmp.append(word)
                    words.remove(word)
        answer += 1
        if target == "".join(tmp):
            break
        else:
            start = tmp
    return answer
