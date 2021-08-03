def solution(price, money, count):
    result = 0
    
    for i in range(1, count+1):
        result += price * i
    
    if result > money:
        return result - money
    
    return 0