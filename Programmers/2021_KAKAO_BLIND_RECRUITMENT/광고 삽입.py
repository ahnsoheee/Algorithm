def time2sec(play_time):
    h, m, s = play_time.split(':')
    return int(h)*3600 + int(m)*60 + int(s)

def sec2time(sec):
    h = sec // 3600
    h = '0' + str(h) if h < 10 else str(h)
    sec = sec % 3600
    m = sec // 60
    m = '0' + str(m) if m < 10 else str(m)
    sec = sec % 60
    s = '0' + str(sec) if sec < 10 else str(sec)
    
    return h + ':' + m + ':' + s

def solution(play_time, adv_time, logs):
    answer = ''
    play_time = time2sec(play_time)
    adv_time = time2sec(adv_time)
    time = [0 for _ in range(play_time + 1)]
    
    for log in logs:
        start, end = log.split('-')
        time[time2sec(start)] += 1
        time[time2sec(end)] -= 1
    
    # i초일 때 시청자 수
    for i in range(1, play_time + 1):
        time[i] = time[i-1] + time[i]
    
    # 누적 시청자 수
    for i in range(1, play_time + 1):
        time[i] = time[i-1] + time[i]
    
    # 시청자 수가 가장 많은 구간 탐색
    max_cnt = time[adv_time-1]
    max_time = 0
    
    for i in range(adv_time, play_time):
        if max_cnt < time[i] - time[i-adv_time]:
            max_cnt = time[i] - time[i-adv_time]
            max_time = i - adv_time + 1

    answer = sec2time(max_time)
    
    return answer