def replace_code(code):
    code = code.replace('C#', 'c')
    code = code.replace('D#', 'd')
    code = code.replace('F#', 'f')
    code = code.replace('G#', 'g')
    code = code.replace('A#', 'a')

    return code


def solution(m, musicinfos):
    answer = ''
    result = []
    idx = 0

    for musicinfo in musicinfos:
        idx += 1
        info = musicinfo.split(',')
        start = info[0].split(':')
        end = info[1].split(':')

        time = (int(end[0]) - int(start[0])) * 60 + int(end[1]) - int(start[1])

        code = replace_code(info[3])
        code = code * (time // len(code)) + code[:time % len(code)]

        if replace_code(m) in code:
            result.append([info[2], time, idx])

    if len(result) == 1:
        return result[0][0]

    elif len(result) == 0:
        return "(None)"

    else:
        print(result)
        result = sorted(result, key=lambda x: (-x[1], x[2]))
        return result[0][0]
