import itertools


def solution(relation):
    row = len(relation)
    col = len(relation[0])
    idx = [i for i in range(col)]
    combinations = []

    for i in range(1, col+1):
        combinations.extend(itertools.combinations(idx, i))  # 모든 속성 인덱스의 조합

    unique = []
    for combination in combinations:
        values = []  # 속성에 해당하는 값

        for row in relation:
            tmp = []  # 조합에 해당하는 속성의 값을 리스트로 묶음
            for i in range(len(combination)):
                tmp.append(row[combination[i]])
            values.append(tmp)

        cnt = True  # 유일성 체크
        for value in values:
            if values.count(value) != 1:
                cnt = False
                break

        if cnt:  # 유일성이 만족되면 최소성 체크
            flag = True
            for key in unique:
                if set(key).issubset(combination):  # 조합이 유일성을 만족하는 키들 중에 부분집합인지
                    flag = False  # 부분집합이면 최소성 불만족
            if flag:  # 최소성 만족
                unique.append(combination)

    return len(unique)


solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
         "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])
