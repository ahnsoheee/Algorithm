def solution(enroll, referral, seller, amount):
    answer = []
    tree = { '-': 'root' }
    profit = { '-': 0 }
    
    for i in range(len(enroll)):
        child = enroll[i]
        tree[child] = referral[i]
        profit[child] = 0

    for i in range(len(seller)):
        child = seller[i]
        parent = tree[child]
        money = amount[i] * 100
        profit[child] += money
        cost = money // 10
        
        while cost != 0:
            profit[child] -= cost
            profit[parent] += cost
            money = cost
            child = parent
            parent = tree[child]
            cost = money // 10
            
            if parent == 'root': 
                break
    
    for person in enroll:
        answer.append(profit[person])
        
    return answer