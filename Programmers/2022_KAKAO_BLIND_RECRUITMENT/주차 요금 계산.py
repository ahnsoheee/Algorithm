# https://programmers.co.kr/learn/courses/30/lessons/92341

import math

def toMin(time):
    h, m = map(int, time.split(":"))
    
    return h * 60 + m

def solution(fees, records):
    answer, result = [], []
    check = {}
    car_num = []
    
    for record in records:
        record = record.split(" ")
        time, num = record[0], record[1]
        
        if num not in check:
            check[num] = [time]
        else:
            check[num].append(time)
    
        if num not in car_num:
            car_num.append(num)
            
    car_num.sort()
    for num in car_num:
        time = 0
        times = check[num]
        
        for i in range(0, len(times)-1, 2):
            IN = toMin(times[i])
            OUT = toMin(times[i+1])
            
            time += OUT - IN

        if len(times) % 2 == 1:
            IN = toMin(times[-1])
            time += toMin("23:59") - IN
        
        if (time < fees[0]):
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (math.ceil((time-fees[0])/fees[2])) * fees[3])

    return answer